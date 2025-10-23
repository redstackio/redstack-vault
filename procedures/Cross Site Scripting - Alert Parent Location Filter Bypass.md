---
id: b21ca177-b989-47a3-9291-40fb6883ee8a
name: Cross Site Scripting - Alert Parent Location Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.659989+00:00'
updated_at: '2023-04-10T20:21:38.483205+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass document blacklist]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Cross Site Scripting - Alert Parent Location Filter Bypass

## Summary

Cross Site Scripting (XSS) is a type of attack where malicious code is injected into a web page, allowing an attacker to execute arbitrary code in the victim's browser. This specific procedure focuses on bypassing a document blacklist by using the 'Alert Parent Location' command. This technique can

## Description

# Description

Cross Site Scripting (XSS) is a type of attack where malicious code is injected into a web page, allowing an attacker to execute arbitrary code in the victim's browser. This specific procedure focuses on bypassing a document blacklist by using the 'Alert Parent Location' command. This technique can be used to trick the victim into clicking on a malicious link, which can lead to the attacker stealing sensitive information or taking control of the victim's browser. This procedure can be used by an attacker to gain access to a victim's sensitive data or to gain control over their browser.

Technical Explanation: The 'Alert Parent Location' command is used to display an alert message with the URL of the parent window. By using this command, an attacker can bypass a document blacklist and execute arbitrary code in the victim's browser. This technique can be used to steal sensitive information or to take control of the victim's browser.

Business Value: This procedure can be used by attackers to gain access to a victim's sensitive data or to gain control over their browser. This can lead to financial loss, reputational damage, and legal liability for the victim and their organization.

 

## Requirements

1. Access to a vulnerable web page

1. Knowledge of the 'Alert Parent Location' command

 

## Defense

1. Implement input validation and output encoding to prevent XSS attacks

1. Implement a Content Security Policy (CSP) to restrict the sources of executable scripts

1. Regularly update and patch web applications to address known vulnerabilities

 

## Objectives

1. Bypass document blacklist to execute arbitrary code in the victim's browser

1. Trick the victim into clicking on a malicious link

1. Steal sensitive information or take control of the victim's browser

 

# Instructions

1. This command will create a div element with id 'x' and then execute a script that will show an alert with the parent location of the third parent node of the div element.

 



**Code**: [[<div id = "x"></div><script>alert(x.parentNode.par]]



> The script uses the parentNode property to navigate up the DOM tree and access the location property of the parent of the parent of the parent of the div element with id 'x'. The last line of the script uses bracket notation to access the 'document' property of the 'window' object.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Bypass document blacklist]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


