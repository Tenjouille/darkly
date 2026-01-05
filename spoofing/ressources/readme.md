# SPOOFING

## Description de la vulnérabilité

L'usurpation d'adresse IP (en anglais : IP spoofing ou IP address spoofing) est une technique de piratage informatique utilisée en informatique qui consiste à envoyer des paquets IP en utilisant une adresse IP source qui n'a pas été attribuée à l'ordinateur qui les émet. Le but peut être de masquer sa propre identité lors d'une attaque d'un serveur, ou d'usurper en quelque sorte l'identité d'un autre équipement du réseau pour bénéficier des services auxquels il a accès.
Wiki : [https://fr.wikipedia.org/wiki/Usurpation_d%27adresse_IP#:~:text=L'usurpation%20d'adresse%20IP,l'ordinateur%20qui%20les%20%C3%A9met.]

**Principe** :
- [Point clé 1]
- [Point clé 2]
- [Point clé 3]

**La vulnérabilité** : [Explication en 1-2 phrases de la faille exploitable]

## Détection de la vulnérabilité

[Comment identifier cette vulnérabilité - outils utilisés, ce qu'on observe]

**Indicateurs de vulnérabilité :**
- [Indicateur 1]
- [Indicateur 2]
- [Indicateur 3]

## Description de l'attaque

### [Nom de l'étape 1]
j'inspecte la page http://localhost:8080/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f dans DevTools. Je vois que le code contient des commentaires qui peuvent donner des informations : 
<!--
You must come from : "https://www.nsa.gov/".
-->
Refercne a l'en tete http Referer qui definit l'adresse a partir de laquelle la requete a ete demandee

<!--
	Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
Reference a 'ent ete User-agent 
qui identitie le client qui fait la requete (navigateur, robot ou application)
Si on regarde les header htpp definit dans la request url, on voit 

Refer = http://localhost:8080/index.php
User-Agent = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36

les commentaires nous suggerent de changer la valeur de ces headers 

### [Nom de l'étape 2]
[Description de ce qui est fait]

### [Nom de l'étape 3]
[Description de ce qui est fait]

### Exploitation
[Action finale et résultat obtenu (flag, accès, etc.)]

## Risques liés à l'exploitation de cette faille

1. **[Type de risque 1]** : [Description du danger]
2. **[Type de risque 2]** : [Description du danger]
3. **[Type de risque 3]** : [Description du danger]
4. **[Type de risque 4]** : [Description du danger]

## Protection contre la vulnérabilité

### [Nom de la protection 1]
- [Mesure de protection]
- [Mesure de protection]

### [Nom de la protection 2]
- [Mesure de protection]
- [Mesure de protection]

### [Nom de la protection 3]
- [Mesure de protection]
- [Mesure de protection]

### Exemple de configuration sécurisée
```[langage]
[Exemple de code ou configuration sécurisée]
```

curl -X GET -H "Referer: https://www.nsa.gov/" -A "ft_bornToSec" "127.0.0.1:8080?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" > spoof.html


curl 
-X => methode de tranfert de donnees
-H => definir les en-tete (header) http
-A => definit l'entete User-agent 