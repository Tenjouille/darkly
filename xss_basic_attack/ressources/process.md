# XSS Attack

## Check if there is a breach to exploit.

In the comment section enter as "Name" and "Message" :

```
<i>Test</i>
```

The Message section is not display in italics. The Name section has a lenght of 10 characters max. By inspecting the HTML page, you can disable this restriction. By trying again, your new post displays your name in italics. So the name field is vulnerable to XSS attacks.

## Use the script tag

After getting rid of the maxlenght restriction in then devTool, you can enter in the Name field : 
```
<Script>alert('Hello world')</Script>
```
An alert popup will now open everytime you will open the comment section.


## Use the anchor tag

After getting rid of the maxlenght restriction in then devTool, you can enter in the Name field : 
```
<a href="www.google.com">Click ME !</a>
```

You can click on "Click ME to access to the extern link you entered in the anchor tag.

**Both script and anchor tags are unwanted behaviors for a comment page. And give you the flag.**
