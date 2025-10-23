---
id: c666e481-49c6-48a2-b70f-57f0bbe4907f
name: Mutated XSS with HTML Tag Recreation and DOMPurify Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.260303+00:00'
updated_at: '2023-04-10T20:21:54.780476+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
tags:
- '[[Cross Site Scripting]]'
- '[[Mutated XSS]]'
commands:
- '[[Get innerHTML of an element]]'
---

# Mutated XSS with HTML Tag Recreation and DOMPurify Bypass

## Summary

Mutated XSS is a type of XSS attack where the attacker injects malicious code into a web page that is then executed by the victim's browser. This specific procedure utilizes the HTML tag recreation and DOMPurify bypass techniques to evade defenses and execute the malicious code. The HTML tag recrea

## Description

# Description

Mutated XSS is a type of XSS attack where the attacker injects malicious code into a web page that is then executed by the victim's browser. This specific procedure utilizes the HTML tag recreation and DOMPurify bypass techniques to evade defenses and execute the malicious code. The HTML tag recreation technique involves the attacker recreating a valid HTML tag that is then interpreted by the browser as a script tag. The DOMPurify bypass technique involves manipulating the DOM to bypass the DOMPurify sanitization library. This attack can result in the attacker gaining access to sensitive information, such as session cookies, and can also allow the attacker to perform actions on behalf of the victim, such as sending phishing emails.

 

## Requirements

1. Access to a vulnerable web application

1. Ability to inject code into the web application

1. Knowledge of HTML tag recreation and DOMPurify bypass techniques

 

## Defense

1. Implement input validation and output encoding to prevent injection attacks

1. Use a Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page

1. Regularly update and patch web applications and libraries to address known vulnerabilities

 

## Objectives

1. Inject malicious code into a web page

1. Evade defenses and execute the malicious code

1. Gain access to sensitive information

1. Perform actions on behalf of the victim

 

# Instructions

1. To recreate HTML tags using browser quirks, follow these steps:
1. Identify the HTML tag that needs to be recreated.
2. Create a new element using JavaScript.
3. Set the innerHTML property of the new element to the HTML code that needs to be recreated.
4. Append the new element to the parent element that contained the original HTML code.

Example:

var originalElement = document.getElementById('original-element');
var newElement = document.createElement('div');
newElement.innerHTML = '<p>Recreated HTML tag</p>';
originalElement.appendChild(newElement);

 



**Code**: [[element.innerHTML]]



> Sometimes, due to browser quirks or other issues, HTML tags may not be properly rendered on a web page. In such cases, it may be necessary to recreate the HTML tags using JavaScript. This can be achieved by creating a new element using JavaScript, setting its innerHTML property to the HTML code that needs to be recreated, and appending it to the parent element that contained the original HTML code.



**Command** ([[Get innerHTML of an element]]):

```bash
element.innerHTML
```



2. To execute this attack, an attacker can use the Mutated XSS payload in the 'data' field as input to a vulnerable website. The payload is designed to bypass the DOMPurify component on Google Search, allowing the attacker to execute arbitrary JavaScript code on the victim's browser.

 



**Code**: [[<noscript><p title="</noscript><img src=x onerror=]]



> The 'data' field contains the Mutated XSS payload that is used to bypass the DOMPurify component on Google Search. The 'lang' field specifies the programming language used in the payload, which is JavaScript in this case. The 'text' field provides additional information about the attack, including the name of the researcher who discovered it, Masato Kinugawa, and links to technical blogposts with more details. The 'instruction' field provides step-by-step instructions on how to execute this attack. The 'explain' field explains the purpose and significance of each field in the JSON object.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

## Commands Used

- [[Get innerHTML of an element]]

## Tags

- [[Cross Site Scripting]]
- [[Mutated XSS]]


