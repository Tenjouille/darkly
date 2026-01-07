# The HTPASSWD File

*If the king unfortunately drop his crown at your feet, would you take it ??* 👑 

## What is it ?

HTPASSWD allows the creation and maintenance of text files where are stored basic authentification credentials for HTTP users. Its data follows a key:value pattern : user:password.

Passwords are hashed using bcrypt, a modified version of MD5

## How do you exploit this file.

By having access to every confidential data stored in this file, you can get usernames, and may be crack weak passwords.

## How do you counter it ?

Never put this file in the Web Server URI space. It must not be accessible from a browser.
And once again use a strong password, to prevent any bruteforce decryption of your password.