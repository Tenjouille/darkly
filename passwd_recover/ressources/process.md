Password Recover vulnerability

Inspecton le code source de la page `http://localhost:8080/?page=recover`

Le bouton Submit est wrappe dans un formulaire :
```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```

On remarque une valeur codee en dur dans le code html : `webmaster@borntosec.com`

Il suffit donc de changer cette valeur pour detourner l'envoie des donnees du formulaire, et on trouve le flag

Sources
https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning 
