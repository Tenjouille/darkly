# Advanced XXS Attack

The GET URL to access this page allows different type of data. So like the basic XSS Attack, we want to load through URL a malicious script that can be used later on.

But if you enter classic html tags in the URL param, right and left chevrons are encoded. To bypass it, you can use the URL **data** tool (cf. data.md). 

It allows us to specify that we are trying to load a text/html data type. This way our script is well executed, but doesn't revealed the flag.

Encoding it in base64 was the answer. The app receive the malicious code, decrypt it and execute it.

## Mitigation

As the other XSS exemple, escaping special characters prevents any wrong input.
