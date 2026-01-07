# Exploitation du fichier robots.txt pour accéder à du contenu sensible


Le fichier `robots.txt` est une convention visant à indiquer aux robots d'exploration (web crawlers) quelles parties d'un site web ne doivent pas être explorées. 

Son objectif est d'éviter de surcharger son site de demandes et d'optimiser le référencement SEO.

Il est accessible publiquement à la racine du site (ex: `http://site.com/robots.txt`)

Il liste les répertoires et fichiers que les robots ne devraient pas explorer, et donc peut involontairement révéler l'existence de contenu potentiellement sensible


## Détection de la vulnérabilité

Accéder au fichier `robots.txt` à la racine du site : `http://localhost:8080/robots.txt`

On observe :
```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```
User-agent designe les robots d'exploration

Les directives `Disallow` pointant vers des répertoires sensibles et cachés

On voit ici que les robots ne devraient pas accéder aux repertoires /whatever/ et /.hidden/

## Description de l'attaque

Accédons au répertoire /.hidden/ `http://localhost:8080/.hidden/`

On voit au'il contient de nombreux sous-dossiers imbriqués, chacun contenant des fichiers `README`.

On lance un script Python pour parcourir récursivement tous les sous-dossiers et lire le contenu de chaque `README` :
```
python3 ./read_me_harvester.py > result.txt
```

Le flag est caché dans l'un de ces fichiers et est révélé par le script.

## Risques liés à l'exploitation de cette faille

**Divulgation d'information** : Révélation de l'emplacement de contenu sensible ou caché

**Accès à des données non publiques** : Fichiers de configuration, backups, fichiers administratifs accessibles

**Reconnaissance pour attaques futures** : Cartographie de la structure du site pour identifier d'autres vulnérabilités

**Exposition de contenus sensibles** : Documents, données ou fonctionnalités qui devraient être protégés

**Fausse sécurité** : L'équipe pense que le contenu est protégé alors qu'il est publiquement accessible

## Protection contre la vulnérabilité

### Ne jamais utiliser robots.txt comme mécanisme de sécurité
- `robots.txt` est une recommandation, pas une protection
- Ne pas y lister des répertoires contenant du contenu réellement sensible

### Implémenter de vraies restrictions d'accès
- Utiliser l'authentification HTTP (Basic Auth, OAuth, etc.)
- Configurer les permissions serveur (fichiers `.htaccess`, nginx, Apache)
- Bloquer l'accès aux répertoires sensibles au niveau du serveur web

### Ne pas stocker de contenu sensible dans des répertoires accessibles
- Placer les fichiers sensibles en dehors du document root
- Utiliser des noms de répertoires non prédictibles
- Supprimer ou déplacer les fichiers de développement/debug en production

### Sources
- [Robots-txt.com](https://robots-txt.com/)
- [Google - Créer un fichier robots.txt](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt?hl=fr)
- [PortSwigger - Robots.txt file](https://portswigger.net/kb/issues/00600600_robots-txt-file)