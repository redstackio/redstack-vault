---
id: 0ca0ae5d-a1e2-4731-9348-ee8c86c05e8d
name: Polyglot XSS Attack using SVG Image Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.289114+00:00'
updated_at: '2023-04-10T20:21:55.843753+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cross Site Scripting]]'
- '[[Polyglot XSS]]'
---

# Polyglot XSS Attack using SVG Image Injection

## Summary

Polyglot XSS Attack using SVG Image Injection is a technique used by attackers to inject malicious code into a vulnerable web application. The attack involves injecting malicious code into an SVG image, which is then uploaded to the web application. Once the image is displayed on a victim's browser

## Description

# Description

Polyglot XSS Attack using SVG Image Injection is a technique used by attackers to inject malicious code into a vulnerable web application. The attack involves injecting malicious code into an SVG image, which is then uploaded to the web application. Once the image is displayed on a victim's browser, the injected code is executed, allowing the attacker to steal sensitive data or take control of the victim's machine.

From a technical perspective, this attack works by taking advantage of the fact that SVG images can contain executable code. The attacker crafts an SVG image that contains the malicious code and uploads it to the web application. When the victim's browser loads the image, the code is executed, allowing the attacker to achieve their goals.

From a business perspective, this attack can have serious consequences, including the theft of sensitive data or the compromise of critical systems. It is important for organizations to take steps to protect themselves against this type of attack.

## Requirements

1. Access to a vulnerable web application

1. Ability to craft a malicious SVG image

## Defense

1. Ensure that all web applications are up-to-date and free of known vulnerabilities

1. Implement content security policies to prevent the execution of malicious code

1. Regularly scan web applications for vulnerabilities and immediately address any issues found

## Objectives

1. Inject malicious code into a vulnerable web application

1. Execute code on a victim's machine

1. Steal sensitive data or take control of the victim's machine

# Instructions

1. This command is used to perform a Polyglot XSS attack. The code is designed to bypass input validation mechanisms and execute malicious code in the victim's browser.

**Code**: [[jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert]]

> The code utilizes multiple techniques to bypass input validation mechanisms, including obfuscation, encoding, and the use of multiple comment types. The code can be injected into vulnerable web applications through various means, such as input fields or URLs. Once executed, the code can perform a variety of malicious actions, such as stealing sensitive information or executing arbitrary code on the victim's machine.

2. This command is used to perform a Polyglot XSS attack. It involves injecting malicious code into a vulnerable web page that can execute in multiple languages. The code can execute in both client and server-side contexts and can steal sensitive information or perform actions on behalf of the user.

**Code**: [[">><marquee><img src=x onerror=confirm(1)></marque]]

> The 'data' field contains the payload of the attack which is a combination of HTML, JavaScript, and other web technologies. The payload is designed to bypass security measures and execute in multiple contexts. The 'lang' field specifies the programming language used in the payload. The 'text' field provides a brief description of the attack. The 'instruction' field provides details on how to execute the attack and what its effects are.

3. This command is used to perform a polyglot XSS attack on a vulnerable website. The attack payload is a combination of multiple languages and is designed to bypass input validation and execute malicious code on the victim's browser.

**Code**: [[" onclick=alert(1)//<button ‘ onclick=alert(1)//> ]]

> The 'data' field contains the payload for the polyglot XSS attack. It is a combination of HTML, JavaScript, and CSS code that can be executed by the browser. The 'lang' field specifies the language used in the attack payload, which in this case is JavaScript. The 'text' field provides additional information about the attack. The 'instruction' field explains how to use this command to perform a polyglot XSS attack. The 'name' field provides a descriptive name for this command.

4. The command is designed to execute a cross-site scripting (XSS) attack on a vulnerable website. The attack is carried out by injecting malicious code into a web page. The code is executed by unsuspecting users who visit the page, allowing the attacker to steal sensitive information or take control of the user's computer.

**Code**: [[';alert(String.fromCharCode(88,83,83))//';alert(St]]

> The 'data' field contains the malicious code that is injected into the website. The code is designed to execute an alert message that displays the string 'XSS'. The code is written in a way that is compatible with multiple programming languages, making it difficult for web developers to defend against. The 'lang' field specifies that the code is written in JavaScript. The 'text' field provides additional information about the attack. The 'instruction' field provides details on how to carry out the attack, including identifying vulnerable websites and inserting the malicious code. The 'explain' field provides further information on the purpose and potential impact of the attack.

5. This is a type of Cross-Site Scripting (XSS) attack that is capable of executing on multiple platforms and in multiple contexts. The attack is designed to bypass security measures by using a combination of HTML, CSS, and JavaScript code to execute malicious commands. 

**Code**: [[';alert(String.fromCharCode(88,83,83))//';alert(St]]

> The attacker can inject the malicious code into a vulnerable website or web application, and when a victim visits the site, the code is executed in their browser. The code can be used to steal sensitive information, such as login credentials, or to perform actions on behalf of the user, such as making unauthorized purchases or sending spam emails.

6. This is a polyglot XSS attack payload. It is designed to execute a malicious script that can steal sensitive information or perform other malicious activities. The payload is written in a way that it can be interpreted by multiple languages, making it difficult to detect and prevent. It can be used in various contexts, such as in a web application's input fields, comments section, or even in an email message. It is important to sanitize user input to prevent such attacks.

**Code**: [[-->'"/></sCript><svG x=">" onload=(co\u006efirm)``]]

> The payload consists of a string of characters that are designed to be interpreted differently by different languages. The payload starts with the characters '-->' which are used to comment out the rest of the HTML code. The payload then includes the characters '"/></sCript><svG x=">"' which are interpreted as a closing tag for the script element and the opening tag for an SVG element. The 'onload' attribute of the SVG element is then used to execute the malicious script. The script is obfuscated using the Unicode escape sequence '\u006e' which represents the letter 'n'. This is done to evade detection by security measures that may be looking for specific keywords or patterns in the code. The payload is designed to be cross-site scripting (XSS) attack and can be used to steal sensitive information or perform other malicious activities.

7. This command is used to inject an SVG image into a website. The 'data' field contains the code for the SVG image that will be injected. The 'lang' field specifies the programming language used, which in this case is JavaScript. The 'text' field contains the URL of the image that will be displayed. 

**Code**: [[<svg%0Ao%00nload=%09((pro\u006dpt))()//]]

> The 'name' field should be filled with a name that describes the purpose of this command, which is to inject an SVG image into a website. The 'data' field contains a string of characters that represents the SVG image. The 'lang' field specifies the programming language used, which in this case is JavaScript. The 'text' field contains the URL of the image that will be displayed. The 'instruction' field should provide details on how to use this command, including any necessary arguments. The 'explain' field should provide a more detailed explanation of the command and its purpose.

8. This command is used to perform a Cross-Site Scripting (XSS) attack using a polyglot payload. The payload can be modified and used to exploit vulnerabilities in web applications.

**Code**: [[# by crlf
javascript:"/*'/*`/*--></noscript></titl]]

> The 'data' field contains the actual payload that is used to execute the XSS attack. The 'lang' field specifies the language used in the payload, which in this case is JavaScript. The 'text' field provides a brief description of the payload and its source. The 'instruction' field provides instructions on how to use the command, and the 'explain' field provides a detailed explanation of the payload and its potential impact on web applications.

9. This command executes a Polyglot XSS attack on the target website. The attack can be executed by injecting the provided code into an input field or a URL parameter.

**Code**: [[JavaScript://%250Aalert?.(1)//'/*\'/*"/*\"/*`/*\`/]]

> The provided code is a combination of different XSS attack vectors that can bypass different security filters. The attack can execute arbitrary JavaScript code on the victim's browser and steal sensitive information such as cookies, session tokens, and login credentials. It is important to note that this attack should only be executed on websites with the owner's permission and for testing purposes only.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Cross Site Scripting]]
- [[Polyglot XSS]]
