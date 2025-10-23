---
id: 93d73f96-13fe-47be-912e-a2472f6e3812
name: HTML5 Tag Based Cross Site Scripting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.825734+00:00'
updated_at: '2023-04-10T20:21:39.879286+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in HTML/Applications]]'
- '[[XSS using HTML5 tags]]'
---

# HTML5 Tag Based Cross Site Scripting

## Summary

HTML5 tag based Cross Site Scripting (XSS) is a type of web-based attack that targets the users of a web application. In this attack, the attacker injects malicious code into the HTML5 tags of a web page, which is then executed by the user's browser. This allows the attacker to steal sensitive info

## Description

# Description

HTML5 tag based Cross Site Scripting (XSS) is a type of web-based attack that targets the users of a web application. In this attack, the attacker injects malicious code into the HTML5 tags of a web page, which is then executed by the user's browser. This allows the attacker to steal sensitive information, such as login credentials or session tokens, from the victim. This attack can be used to bypass security controls, such as firewalls and intrusion detection systems, and can be difficult to detect.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of HTML5 tag based XSS payloads

1. Victim interaction with the malicious web page

 

## Defense

1. Implement input validation and sanitization to prevent malicious code injection

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page

1. Regularly update and patch web applications to address known vulnerabilities

 

## Objectives

1. Inject malicious code into the HTML5 tags of a web page

1. Execute the malicious code on the victim's browser

1. Steal sensitive information from the victim

 

# Instructions

1. This JSON object contains a list of XSS attack payloads that can be used to test the security of a web application. The payloads include various HTML tags and JavaScript events that can be used to execute malicious code on the victim's browser. Each payload can be injected into an input field or a URL parameter to test the application's vulnerability to XSS attacks.

 



**Code**: [[<body onload=alert(/XSS/.source)>
<input autofocus]]



> The payload includes various HTML tags and JavaScript events that can be used to execute malicious code on the victim's browser. For example, the 'onload' event is triggered when the page finishes loading, and the 'alert' function is used to display an alert box with the message 'XSS'. The 'autofocus' attribute is used to automatically focus on an input field, and the 'onfocus' event is triggered when the field receives focus. The 'onerror' event is triggered when an error occurs while loading an image or a video, and can be used to execute JavaScript code. The 'ontouchstart', 'ontouchend', and 'ontouchmove' events are triggered when a user touches the screen, and can be used to execute JavaScript code on mobile devices.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Cross Site Scripting]]
- [[XSS in HTML/Applications]]
- [[XSS using HTML5 tags]]


