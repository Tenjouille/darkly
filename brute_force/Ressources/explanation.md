# THE BRUTE FORCE METHOD
*You look at the picture of your boss's dog beside his locked computer. What's its name again ?*

## What is it ??

With the brute force method, **you try every combinations** until you find the good. It's like if you had a 4-digit locked padlock, and you would try to open it with every possible combination from 0000 to 9999 until it unlocks.


## The WhiteBox Test

To exploit this breach, you need a dictionary with different character strings, and you need to find out the URL used by the specific protocol to authentificate. Then create a script looping on the dictionary and returning any output different with the output for a wrong password. Your chances to find a good password and the time the script will take to execute will increase with the size of your dictionary.

## How do you counter it ?

To counter the brute force method, you can set up the following security features :

- Ask for a complex password. If you ask for a minimum password lenght(l), minimum one uppercase letter(up), one lowercase letter(low), one numerical character(num), one special character(spe), there will be at least (26up + 26low + 10num + 32spe)<sup>l</sup> ≈ 4,7 × 10²³ different combinations
- Limit the number of query by minute
- Limit the number of try before banning the source IP address
- Add a CAPTCHA between the authentication and the response.