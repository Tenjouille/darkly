# Exploitation de la vulnérabilité de récupération de mot de passe (Hidden Field Manipulation)

## Description de la vulnérabilité

Cette vulnérabilité combine deux failles : la **manipulation de champs cachés** (Hidden Field Manipulation) et une mauvaise implémentation de la fonctionnalité de récupération de mot de passe. Le formulaire contient un champ caché avec une valeur codée en dur côté client, permettant à un attaquant de détourner l'envoi de l'email de récupération.

**Principe** :
- Les champs cachés (`<input type="hidden">`) sont visibles dans le code HTML
- Ces champs peuvent être modifiés côté client avant soumission du formulaire
- Le serveur fait confiance aux données du champ caché sans validation
- L'adresse email de destination est contrôlée par le client, pas le serveur


## Détection de la vulnérabilité

Inspecter le code source de la page `http://localhost:8080/?page=recover` avec les DevTools.

Le formulaire de récupération contient :
```html
<form action="#" method="POST">
    <input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
    <input type="submit" name="Submit" value="Submit">
</form>
```

Présence d'un champ caché (`type="hidden"`) contenant une information critique (email) codée en dur dans le HTML : `webmaster@borntosec.com`

L'adresse email de récupération est stockée dans un champ caché HTML modifiable par l'utilisateur, permettant à un attaquant de détourner l'email de réinitialisation vers sa propre adresse.

Deux méthodes possibles pour modifier la valeur:

**Méthode 1 : Modification directe dans les DevTools**
- Clic droit sur le champ → "Edit as HTML"
- Changer `value="webmaster@borntosec.com"` en `value="attacker@malicious.com"`

**Méthode 2 : Console JavaScript**
```javascript
document.querySelector('input[name="mail"]').value = "attacker@malicious.com";
```

Soumettre le formulaire avec la nouvelle valeur. Le serveur envoie l'email de récupération à l'adresse modifiée par l'attaquant, révélant le flag.

Un attaquant peut détourner la récupération de mot de passe d'un utilisateur légitime vers sa propre adresse email, obtenant ainsi accès au compte.

## Risques liés à l'exploitation de cette faille

**Prise de contrôle de compte** : L'attaquant peut recevoir le lien de réinitialisation et accéder au compte de la victime

**Usurpation d'identité** : Accès complet au compte permettant de se faire passer pour l'utilisateur légitime

**Vol de données personnelles** : Accès aux informations sensibles du compte compromis

**Escalade de privilèges** : Si le compte ciblé est administrateur, accès privilégié à tout le système

**Attaques en chaîne** : Utilisation du compte compromis pour mener d'autres attaques (phishing, propagation, etc.)

## Protection contre la vulnérabilité

### Ne jamais stocker d'informations critiques dans des champs cachés
- Les champs cachés sont visibles et modifiables par l'utilisateur
- Ne jamais faire confiance aux données provenant du client
- Stocker les informations sensibles uniquement côté serveur (session, base de données)

### Utiliser des tokens de réinitialisation sécurisés
- Générer un token aléatoire cryptographiquement sûr
- Associer le token à l'utilisateur dans la base de données
- Limiter la durée de validité du token (15-60 minutes)
- Token à usage unique (invalider après utilisation)

### Validation côté serveur
- Toujours valider et vérifier les données côté serveur
- Ne jamais faire confiance aux données envoyées par le client
- Vérifier que l'email existe dans la base de données
- Utiliser les sessions pour stocker l'identifiant de l'utilisateur

### Mesures de sécurité supplémentaires
- **Rate limiting** : Limiter le nombre de tentatives de récupération par IP
- **CAPTCHA** : Ajouter un CAPTCHA pour éviter l'automatisation
- **Logging** : Logger toutes les demandes de réinitialisation pour détecter les abus
- **Email de notification** : Notifier l'utilisateur à son adresse enregistrée qu'une réinitialisation a été demandée
- **Prévention de l'énumération** : Retourner le même message que l'email existe ou non


### Sources
- [PortSwigger - Password Reset Poisoning](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning)
- OWASP - Forgot Password Cheat Sheet
- CWE-640: Weak Password Recovery Mechanism 
