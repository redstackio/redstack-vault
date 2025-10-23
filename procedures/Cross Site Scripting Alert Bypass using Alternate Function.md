---
id: 647c366b-78be-4a42-a99d-307e53fcce98
name: Cross Site Scripting Alert Bypass using Alternate Function
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.771887+00:00'
updated_at: '2023-04-10T20:21:46.052356+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass using an alternate way to execute an alert]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Cross Site Scripting Alert Bypass using Alternate Function

## Summary

Cross Site Scripting (XSS) is a type of injection attack where an attacker injects malicious code into a web page viewed by other users. In this specific scenario, the attacker is attempting to bypass a filter that is meant to block alert commands. By using an alternate way to execute an alert, the

## Description

# Description

Cross Site Scripting (XSS) is a type of injection attack where an attacker injects malicious code into a web page viewed by other users. In this specific scenario, the attacker is attempting to bypass a filter that is meant to block alert commands. By using an alternate way to execute an alert, the attacker is able to bypass the filter and execute their payload. The technical details of this attack involve finding and executing a random function starting with 'art' in JavaScript. The business value of this attack is that an attacker can steal user credentials, inject malware, or perform other malicious activities.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of JavaScript

1. Ability to inject code into a web page

 

## Defense

1. Implement input validation and sanitization to prevent XSS attacks

1. Use Content Security Policy (CSP) to restrict the sources of content that can be executed

1. Regularly update and patch web applications to prevent known vulnerabilities

 

## Objectives

1. Bypass alert filters

1. Execute malicious payloads

1. Steal user credentials

 

# Instructions

1. To execute these commands, simply copy and paste them into the JavaScript console of your browser.

 



**Code**: [[window['alert'](0)
parent['alert'](1)
self['alert']]



> This JSON object contains JavaScript commands that can be executed in the browser's JavaScript console. The commands use the window object and its various properties to display alerts to the user. The commands also demonstrate the use of array methods such as map, find, every, filter, findIndex, and forEach. To execute these commands, simply copy and paste them into the JavaScript console of your browser.

2. To count the number of global variables in JavaScript, run the following command:

 



**Code**: [[c=0; for(i in self) { if(i == "alert") { console.l]]



> This command uses a for loop to iterate over all of the global variables in JavaScript and counts the number of variables. The count is logged to the console. This can be useful for debugging and understanding the scope of your variables.

3. The 'alert' command is used to display a message to the user in a pop-up dialog box. The message can be a string, a number, or any other value. The syntax of the command is as follows:

alert(message)

Here, 'message' is the text or value that you want to display in the dialog box. The 'alert' command is commonly used for displaying error messages, warnings, or other important information to the user.

 



**Code**: [[Object.keys(self)[5]
// "alert"
self[Object.keys(s]]



> The 'alert' command takes a single argument, which is the message that you want to display in the dialog box. This message can be a string, a number, or any other value. When the command is executed, a pop-up dialog box will appear on the screen with the message displayed in it. The user will have to click the 'OK' button to dismiss the dialog box and continue using the application.

4. To use this command, first run the code provided to bind the function alert to a new function a(). Then, to execute the alert function, use the code provided and replace the argument "1" with the message you want to display.

 



**Code**: [[a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i))]]



> This command allows you to find and execute the alert function in JavaScript. The regular expression used in the code searches for any function whose name starts with an 'a', followed by one or more of the letters 'r', 'e', or 'l', and ends with a 't'. Once the function is found, it is bound to a new function called 'a'. To execute the alert function, use the code provided and replace the argument "1" with the message you want to display.

5. This command executes a random function starting with 'art' in JavaScript.

 



**Code**: [[a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i))]]



> The 'a' function defined in this command returns the index of the first function in the global scope that starts with 'art'. The 'self' object refers to the global scope in JavaScript. The 'Object.keys(self)' method returns an array of all the property names in the global scope. The 'a()' function is used to find the index of the first function that starts with 'art'. Finally, the function at the index returned by 'a()' is executed with the argument '1'.

6. This command is used for executing a Cross-Site Scripting (XSS) attack on a target website. The 'prompt' function is used to display a message box with the domain of the website. The 'document.location' function is then used to execute JavaScript code that displays an alert message to the user. The 'java\tscript', 'java\rscript', and 'java\tscript' arguments are used to bypass certain security measures that may be in place.

 



**Code**: [[prompt`${document.domain}`
document.location='java]]



> Cross-Site Scripting (XSS) attacks are a type of security vulnerability that allows an attacker to inject malicious code into a web page viewed by other users. This can be used to steal sensitive information, such as login credentials or credit card numbers, or to perform other malicious actions on behalf of the user. It is important to ensure that web applications are properly secured against XSS attacks by validating user input and properly encoding output.

7. These commands are used to display alert messages on the screen using JavaScript. The commands are:
1. eval('ale'+'rt(0)')
2. Function("ale"+"rt(1)")()
3. new Function`al\ert\`6\``
4. constructor.constructor("aler"+"t(3)")()
5. [].filter.constructor('ale'+'rt(4)')()
6. top["al"+"ert"](5)
7. top[8680439..toString(30)](7)
8. top[/al/.source+/ert/.source](8)
9. top['al\x65rt'](9)
10. open('java'+'script:ale'+'rt(11)')
11. location='javascript:ale'+'rt(12)'
12. setTimeout`alert\u0028document.domain\u0029`
13. setTimeout('ale'+'rt(2)')
14. setInterval('ale'+'rt(10)')
15. Set.constructor('ale'+'rt(13)')()
16. Set.constructor`al\x65rt\x2814\x29```

 



**Code**: [[eval('ale'+'rt(0)');
Function("ale"+"rt(1)")();
ne]]



> The commands use various ways to execute the alert() function in JavaScript. These commands can be used by attackers to display malicious messages on the screen of the victim's browser. It is important to be cautious while running any JavaScript commands from untrusted sources.

8. To use this command, follow the steps below:
1. Create an iframe element using the document.createElement() method.
2. Set the onload property of the iframe to a function that triggers the alert.
3. Append the iframe to the document using the document.appendChild() method.
4. Call the XSSObject.proxy() method with the window object, the name of the function you want to proxy (in this case, 'alert'), the name of the report function (in this case, 'window.alert'), and a boolean value indicating whether or not to execute the original function (in this case, false).

 



**Code**: [[var i = document.createElement("iframe");
i.onload]]



> This command can be used to bypass security measures that prevent the use of certain functions, such as the alert() function in JavaScript. By creating an iframe element and setting its onload property to trigger the alert, you can bypass these security measures. Additionally, by using the XSSObject.proxy() method, you can bypass security measures that prevent the direct use of certain functions. This method creates a proxy function that can be used instead of the original function, allowing you to execute the function without triggering security measures.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Bypass using an alternate way to execute an alert]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


