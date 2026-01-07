# The XSS ATTACK
*Darling, why is there a sneaky little rat in your pocket ?*

## What is it ?

The **Cross-Site Scripting** is a code injection attack which consists of sending via a web request some HTML and Js code. 

## How does it works ?
This code will be stored in database and used later, in front side. Because it contain script tags, it will not be interpretted as value, but as part of the HTML structure, and the Js inside will be executed. Pirate usually use this kind of attack to insert permanently in the web app a script requiring admin rights, and when an administrator will open the hosting page, the malicious script will quietly be executed with no restriction.

## The Blackbox Test
To spot an XSS attack opportunity, search for a page where an input will be later print oon screen. If in this input, you enter `<i>Test<i>` and "Test" appears to be in italics, it means `<i>` is not interpreted as a string but as an html element.

## How do you counter it ?

The best way to prevent an XSS attack is to escape special characters sent via requests, to interpret them as characters. 