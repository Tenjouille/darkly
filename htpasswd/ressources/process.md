# STEPS

## Find the htpasswd.

Because we have access to the robots.txt file, and the directory accessibility is enable, we can find the htpasswd file in the /whatever/ directory.

It contains this unique line : `root:437394baff5aa33daa618be47b75cb49`

## Crack the password.

We tried to decrypt the MD5-crypted password using an online tool, it failed.
Insteed, we'll need to use a more powerful tool : hashcat.

Hashcat is the world fastest and most advanced password recovery tool. By giving him a wordlist and a crypt-type, it can tell you if any word in the wordlist corresponds to the hashed sequence.

In a dockerfile, we installed hashcat, downloaded a set of wordlists, and we executed the following command : 
```
hashcat -m 0 437394baff5aa33daa618be47b75cb49 kali-wordlists/rockyou.txt.gz
```

It gave us the password : `qwerty123@`.

## Get the flag

We tried to enter those users info in the basic signin page, it did not worked. So we figure dout it should be an admin password. We tried to open an admin page with the following endpoint `/admin/`, it gave us access to the admin signin page, connecting with our root user granted us the flag.