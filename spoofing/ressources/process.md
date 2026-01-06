# Exploitation de la vulnérabilité Header Spoofing

## Description de la vulnérabilité

Le Header Spoofing (usurpation d'en-têtes HTTP) consiste à modifier les en-têtes HTTP d'une requête pour tromper le serveur sur l'origine ou la nature de la requête. Les en-têtes HTTP comme `Referer` et `User-Agent` peuvent être facilement falsifiés côté client.

**Principe** :
- Les en-têtes HTTP sont contrôlés par le client et peuvent être modifiés
- Le serveur fait confiance à ces en-têtes sans validation appropriée
- L'attaquant peut usurper son origine (`Referer`) ou son identité client (`User-Agent`)

**La vulnérabilité** : Le serveur accorde l'accès à des ressources sensibles en se basant uniquement sur la valeur des en-têtes HTTP, sans validation côté serveur ni authentification robuste.

## Détection de la vulnérabilité

En inspectant le code source HTML de la page dans les DevTools, on trouve des commentaires intéressants :

```html
<!--
You must come from : "https://www.nsa.gov/".
-->
```
Référence à l'en-tête HTTP `Referer` qui définit l'adresse depuis laquelle la requête a été effectuée.

```html
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```
Référence à l'en-tête `User-Agent` qui identifie le client faisant la requête (navigateur, robot ou application).

**Indicateurs de vulnérabilité :**
- Commentaires HTML révélant les en-têtes attendus
- Contrôle d'accès basé uniquement sur les en-têtes HTTP
- Absence de mécanisme d'authentification robuste
- Messages d'erreur ou indices dans le code source

## Description de l'attaque

### Inspection de la page
Ouvrir la page `http://localhost:8080/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f` dans le navigateur et inspecter le code source avec DevTools.

### Analyse des en-têtes actuels
Dans les DevTools (onglet Network), observer les en-têtes HTTP de la requête :
```
Referer: http://localhost:8080/index.php
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36...
```

### Identification des valeurs attendues
Les commentaires HTML indiquent que le serveur attend :
- `Referer: https://www.nsa.gov/`
- `User-Agent: ft_bornToSec`

### Falsification des en-têtes avec curl
Utiliser curl pour envoyer une requête avec les en-têtes modifiés :
```bash
curl -X GET \
  -H "Referer: https://www.nsa.gov/" \
  -A "ft_bornToSec" \
  "http://127.0.0.1:8080/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
```

**Explication des options curl :**
- `-X GET` : Méthode HTTP utilisée (GET)
- `-H "Referer: ..."` : Définit l'en-tête HTTP `Referer`
- `-A "..."` : Définit l'en-tête `User-Agent`

### Exploitation
La requête avec les en-têtes falsifiés trompe le serveur qui croit que la requête provient de `https://www.nsa.gov/` et utilise le navigateur `ft_bornToSec`. Le serveur accorde l'accès et révèle le flag.

## Risques liés à l'exploitation de cette faille

1. **Contournement de restrictions d'accès** : Accès à des ressources normalement protégées en falsifiant l'origine de la requête
2. **Usurpation d'identité** : Se faire passer pour un client légitime ou un bot d'indexation autorisé
3. **Bypass de contrôles de sécurité** : Contourner des filtres basés sur le User-Agent ou le Referer
4. **Exploitation de confiance mal placée** : Accès à des fonctionnalités réservées à certains domaines ou clients
5. **Automatisation d'attaques** : Facilite le scraping, le fuzzing ou d'autres attaques automatisées

## Protection contre la vulnérabilité

### Ne jamais faire confiance aux en-têtes HTTP pour la sécurité
- Les en-têtes `Referer` et `User-Agent` peuvent être falsifiés facilement
- Ne pas utiliser ces en-têtes comme mécanisme de contrôle d'accès principal
- Implémenter une authentification et autorisation robustes (tokens, sessions, OAuth)

### Validation côté serveur
- Toujours valider et vérifier les données côté serveur
- Combiner plusieurs mécanismes de sécurité (pas seulement les en-têtes)
- Utiliser des tokens CSRF pour valider l'origine des requêtes

### Implémenter une authentification forte
- Utiliser des systèmes d'authentification modernes (JWT, OAuth2, sessions sécurisées)
- Ne pas se fier uniquement aux métadonnées de la requête
- Vérifier les permissions côté serveur pour chaque action sensible

### Logging et monitoring
- Enregistrer les tentatives d'accès suspectes
- Détecter les patterns d'attaque (changements fréquents de User-Agent)
- Alerter sur les accès depuis des sources inattendues

### Sources
OWASP
Wikipedia
Claude
