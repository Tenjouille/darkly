# Exploitation de la vulnérabilité Open Redirect

## Description de la vulnérabilité

L'Open Redirect est une vulnérabilité qui exploite la fonctionnalité des URL de redirection pour rediriger l'utilisateur vers un site malveillant. L'application web ne vérifie pas correctement le contenu du paramètre de redirection et redirigera l'utilisateur vers le site web indiqué dans tous les cas.

**Principe** :
- L'application utilise des paramètres d'URL pour gérer les redirections (ex: `?page=redirect&site=facebook`)
- Aucune validation n'est effectuée sur la destination de redirection
- Un attaquant peut modifier ces paramètres pour rediriger vers n'importe quel site


## Détection de la vulnérabilité

Examiner le code source de la page d'accueil et identifier les liens vers les réseaux sociaux utilisant des paramètres de redirection.
En inspectant le code HTML des icônes de réseaux sociaux en bas de la page d'accueil, on observe :

```html
<a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a>
```

On voit les parametres URL suivants contrôlant les redirections :
- `page=redirect` : Active la fonctionnalité de redirection
- `site=facebook` : Définit la destination de redirection

On constate qu'on peut modifier le parametre `site` pour rediriger sans controle ou blocage vers le site que l'on veut
```
http://localhost:8080/index.php?page=redirect&site=google.com
```
La modification du paramètre `site` vers n'importe quel domaine fonctionne sans validation. Le serveur accepte toute valeur et redirige l'utilisateur vers le site spécifié, révélant le flag.


## Risques liés à l'exploitation de cette faille

1. **Attaques de phishing** : Utilisation du domaine légitime pour rediriger vers des sites de phishing, augmentant la crédibilité de l'attaque
2. **Vol d'identifiants** : Redirection vers des pages de connexion clonées pour capturer les credentials
3. **Atteinte à la réputation** : Le domaine légitime est utilisé pour mener des attaques, nuisant à sa réputation
4. **Distribution de malware** : Redirection vers des sites distribuant des logiciels malveillants
5. **Combinaison avec d'autres attaques** : Peut être couplé avec des injections SQL ou XSS pour injecter du code de redirection malveillante

## Protection contre la vulnérabilité

### Validation stricte des URL de redirection
- Implémenter une whitelist des domaines autorisés
- Valider que la destination appartient à un ensemble prédéfini de sites
- Rejeter toute redirection vers des domaines non autorisés

### Utiliser des identifiants au lieu d'URLs
Utiliser des idnetifiants qui seront mappes cote serveur avec des urls 


### Utiliser des chemins relatifs
- Préférer les chemins relatifs qui seront préfixés côté serveur
- Ne jamais accepter des URLs complètes depuis les paramètres utilisateur

### Avertir l'utilisateur
- Afficher une page intermédiaire informant que l'utilisateur quitte le site
- Montrer l'URL de destination et demander confirmation
- Ajouter un délai avant la redirection automatique

### Validation des frameworks et CMS
- Utiliser les méthodes de validation fournies par les frameworks (Laravel, Symfony, etc.)
- Activer les protections CSRF pour les actions de redirection
- Logger toutes les tentatives de redirection pour détecter les abus

### Sensibilisation des utilisateurs
- Former les utilisateurs à vérifier les URL avant de cliquer
- Vérifier l'orthographe du domaine et les paramètres suspects
- Être vigilant sur les redirections après authentification ou dans les pages d'erreur

### Sources
- [IT-Connect - Vulnérabilité Open Redirect](https://www.it-connect.fr/securite-des-applications-web-vulnerabilite-open-redirect/)
- [Nexa - Open Redirect](https://www.nexa.fr/blog/tout-ce-que-vous-devez-savoir-sur-lopen-redirect-cette-vulnerabilite-de-securite)
- OWASP - Unvalidated Redirects and Forwards
- Claude AI