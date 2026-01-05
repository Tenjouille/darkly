# Exploitation des vulnérabilités liées aux cookies

## Description de la vulnérabilité

Un cookie est une donnée stockée par le navigateur qui permet de maintenir l'état d'une session entre des requêtes HTTP successives. Il identifie qu'un ensemble de requêtes provient du même navigateur ou utilisateur.

**Caractéristiques des cookies :**
- Stockage côté client (dans le navigateur)
- Définis côté serveur via l'en-tête HTTP : `Set-Cookie: <nom-cookie>=<valeur-cookie>`
- Transmis automatiquement avec chaque requête HTTP vers le domaine concerné

**La vulnérabilité :** Les cookies peuvent être manipulés côté client, permettant à un attaquant de modifier des informations d'authentification ou d'autorisation si elles ne sont pas correctement protégées.

## Détection de la vulnérabilité

Dans les DevTools du navigateur (onglet Network > Request Headers ou onglet Application > Cookies), on peut observer le cookie `I_am_admin` avec une valeur encodée : `68934a3e9455fa72420237eb05902327`

En décodant cette valeur sur un site comme https://www.dcode.fr/fr, on identifie le chiffrement MD5 :
- `68934a3e9455fa72420237eb05902327` = hash MD5 de `false`

**Indicateurs de vulnérabilité :**
- Cookie contenant des informations d'autorisation (is_admin, role, etc.)
- Utilisation de hash MD5 (algorithme obsolète et non sécurisé pour cet usage)
- Absence de signature ou validation côté serveur
- Cookie modifiable côté client

## Description de l'attaque

### Identification du cookie vulnérable
Inspection des cookies dans les DevTools pour identifier `I_am_admin=68934a3e9455fa72420237eb05902327`

### Analyse de l'encodage
Décodage du hash MD5 pour comprendre la valeur : `false`

### Manipulation du cookie
Calcul du hash MD5 de `true` : `b326b5062b2f0e69046810717534cb09`

### Injection de la nouvelle valeur
Modification du cookie `I_am_admin` avec la nouvelle valeur hashée de `true`

### Exploitation
Rechargement de la page ou envoi de nouvelles requêtes HTTP. Les requêtes sont maintenant exécutées avec les privilèges admin, révélant le flag.

## Risques liés à l'exploitation de cette faille

1. **Usurpation d'identité** : Un attaquant peut se faire passer pour un administrateur ou un autre utilisateur
2. **Élévation de privilèges** : Accès à des fonctionnalités réservées aux administrateurs
3. **Vol de données personnelles** : Accès non autorisé à des informations sensibles
4. **Compromission de l'intégrité** : Modification de données critiques du système
5. **Attaque MITM (Man-In-The-Middle)** : Interception et modification des cookies lors des échanges client-serveur sur HTTP non sécurisé

## Protection contre la vulnérabilité

### Ne jamais stocker d'informations critiques côté client
- Les autorisations doivent être vérifiées côté serveur uniquement
- Utiliser des sessions côté serveur avec un ID de session aléatoire et cryptographiquement sûr

### Utiliser des tokens signés
- JWT (JSON Web Tokens) avec signature cryptographique
- HMAC pour signer les cookies et vérifier leur intégrité

### Attributs de sécurité des cookies
- **`HttpOnly`** : Empêche l'accès aux cookies via JavaScript (protection contre XSS)
- **`Secure`** : Le cookie n'est transmis que sur HTTPS
- **`SameSite=Strict`** ou `SameSite=Lax` : Protection contre les attaques CSRF

### Gestion des sessions
- Limiter la durée de vie d'une session (timeout)
- Régénérer l'ID de session après authentification
- Invalider les sessions côté serveur lors de la déconnexion

### Chiffrement et hashing
- Ne jamais utiliser MD5 pour la sécurité (obsolète et vulnérable)
- Utiliser des algorithmes modernes (SHA-256, bcrypt, Argon2)
- Chiffrer les données sensibles avec des clés secrètes côté serveur

### HTTPS obligatoire
- Forcer l'utilisation de HTTPS pour éviter l'interception des cookies en clair
- Implémenter HSTS (HTTP Strict Transport Security)

### Exemple de configuration sécurisée
```http
Set-Cookie: session_id=<token_aléatoire>; HttpOnly; Secure; SameSite=Strict; Max-Age=3600; Path=/
```