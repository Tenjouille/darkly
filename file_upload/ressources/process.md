# Exploitation de la vulnérabilité Unrestricted File Upload

## Description de la vulnérabilité

Les vulnérabilités de téléversement de fichiers (file upload) surviennent quand un serveur web permet aux utilisateurs de téléverser des fichiers sans valider correctement leur nom, type, contenu ou taille.

**La vulnérabilité** : Le serveur valide uniquement le type de fichier côté client, mais n'effectue aucune vérification côté serveur. Un attaquant peut contourner ces restrictions en modifiant les métadonnées de la requête HTTP.

## Détection de la vulnérabilité

Sur la page `http://localhost:8080/?page=upload`, un formulaire permet de téléverser des images. Seules les images `.jpeg` semblent acceptées, avec un message d'erreur pour les autres types.

En inspectant le payload de la requête POST dans les DevTools, on observe les Form Data suivants :

```
------WebKitFormBoundarycMbhPBHlnpODOYHV
Content-Disposition: form-data; name="MAX_FILE_SIZE"

100000
------WebKitFormBoundarycMbhPBHlnpODOYHV
Content-Disposition: form-data; name="uploaded"; filename="test.jpeg"
Content-Type: image/jpeg


------WebKitFormBoundarycMbhPBHlnpODOYHV
Content-Disposition: form-data; name="Upload"

Upload
------WebKitFormBoundarycMbhPBHlnpODOYHV--
```

Le type MIME `image/jpeg` est déclaré dans la requête, mais cette information est contrôlée par le client et peut être falsifiée.

## Description de l'attaque

Pour contourner la validation côté client, on utilise `curl` pour modifier les en-têtes de la requête et tester si des validations sont effectuées côté serveur.

On téléverse un fichier PHP en le faisant passer pour une image JPEG en modifiant le type MIME :

```bash
curl -X POST \
  -F "uploaded=@/home/cchapon/darkly/file_upload/ressources/index.php;type=image/jpeg" \
  -F "Upload=Upload" \
  -F "MAX_FILE_SIZE=1000000" \
  http://localhost:8080/?page=upload
```

Le serveur accepte le fichier PHP et retourne une page HTML contenant le flag.

Cela confirme qu'aucune validation du type réel de fichier n'est effectuée côté serveur. Le serveur fait confiance au type MIME déclaré dans la requête sans vérifier le contenu réel du fichier.

## Risques liés à l'exploitation de cette faille

**Prise de contrôle du serveur** : Un attaquant peut téléverser et exécuter un script malveillant (web shell) permettant de prendre le contrôle total du serveur.

**Exécution de code arbitraire** : Les fichiers PHP, ASP, JSP ou autres scripts téléversés peuvent être exécutés par le serveur, permettant d'exécuter n'importe quelle commande.

**Compromission du système** : Accès aux fichiers sensibles, modification de données, installation de backdoors, ou utilisation du serveur pour d'autres attaques.

## Protection contre la vulnérabilité

**Validation côté serveur obligatoire** : Ne jamais faire confiance aux données envoyées par le client. Toujours valider le type réel du fichier côté serveur en analysant son contenu (magic bytes, signature du fichier).

**Vérification du contenu du fichier** : Utiliser des bibliothèques pour vérifier que le fichier correspond réellement à son extension déclarée (par exemple, vérifier les magic bytes d'une image).

**Blacklist des extensions dangereuses** : Bloquer les extensions potentiellement dangereuses comme `.php`, `.shtml`, `.phtml`, `.asp`, `.jsp`, `.sh`, `.exe`, etc.

**Configuration serveur sécurisée** : Configurer le serveur pour ne pas exécuter de scripts dans le répertoire d'upload. Exemple avec `.htaccess` sur Apache

**Stockage hors document root** : Stocker les fichiers uploadés en dehors du document root du serveur web et servir les fichiers via un script de téléchargement.

**Renommer les fichiers** : Renommer systématiquement les fichiers uploadés avec des noms générés aléatoirement, sans préserver l'extension originale dangereuse.

### Sources
- [Decodo - Curl POST File](https://decodo.com/blog/curl-post-file#h2-how_to_upload_a_basic_file)
- [PortSwigger - File Upload Vulnerabilities](https://portswigger.net/web-security/file-upload)
- Claude AI