---
id: 71407a3d-2ed7-4595-b829-596ab937777f
name: JavaScript Alert WAF Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.624751+00:00'
updated_at: '2023-04-10T20:21:36.725557+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Security Support Provider|T1101 - Security Support Provider]]'
tags:
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
- '[[Fortiweb WAF Bypass by @rezaduty - 9th July 2019]]'
---

# JavaScript Alert WAF Bypass

## Summary

The JavaScript Alert WAF Bypass technique is used to evade web application firewalls that are configured to block certain types of payloads, such as XSS attacks. By encoding the payload in a way that the firewall does not recognize, the attacker can bypass the WAF and execute the payload on the tar

## Description

# Description

The JavaScript Alert WAF Bypass technique is used to evade web application firewalls that are configured to block certain types of payloads, such as XSS attacks. By encoding the payload in a way that the firewall does not recognize, the attacker can bypass the WAF and execute the payload on the target system. This technique can be used to steal sensitive information, perform unauthorized actions, or gain access to the target system.

Technical Explanation: The attacker uses JavaScript Alert payload to bypass the WAF. The payload is encoded in a way that the WAF does not recognize it as a malicious payload. The payload is then executed on the target system, allowing the attacker to perform unauthorized actions or gain access to sensitive information.

Business Value: This technique can be used by attackers to bypass web application firewalls and gain access to sensitive information, perform unauthorized actions, or gain access to the target system. This can result in financial loss, reputation damage, and loss of customer trust.

 

## Requirements

1. Access to a web application protected by a WAF

1. Knowledge of the WAF configuration and rules

1. Ability to encode the payload in a way that the WAF does not recognize

 

## Defense

1. Regularly update and configure the WAF to block known attack vectors

1. Implement strict input validation and output encoding to prevent XSS attacks

1. Monitor web traffic for suspicious activity and investigate any detected anomalies

 

## Objectives

1. Bypass the web application firewall

1. Execute the JavaScript Alert payload on the target system

 

# Instructions

1. To create a JavaScript alert, use the following code:

 



**Code**: [[\u003e\u003c\u0068\u0031 onclick=alert('1')\u003e]]



> The code consists of an HTML tag with an onclick attribute that triggers the JavaScript alert function. The '1' argument passed to the function will be displayed as the message in the alert box. You can replace this with any message you want to display.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Security Support Provider|T1101 - Security Support Provider]]

## Tags

- [[Common WAF Bypass]]
- [[Cross Site Scripting]]
- [[Fortiweb WAF Bypass by @rezaduty - 9th July 2019]]


