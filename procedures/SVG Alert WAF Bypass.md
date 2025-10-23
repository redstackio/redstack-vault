---
id: 4505ebdf-a885-416a-b8b6-a43867f2cbb6
name: SVG Alert WAF Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.523203+00:00'
updated_at: '2023-04-10T20:21:50.928459+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Multilayer Encryption|T1079 - Multilayer Encryption]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
- '[[Incapsula WAF Bypass by [@daveysec](https://twitter.com/daveysec/status/1126999990658670593)
  - 11th May 2019]]'
---

# SVG Alert WAF Bypass

## Summary

The SVG Alert WAF Bypass is a technique that can be used to bypass certain WAFs that are configured to block certain types of malicious payloads. By using an SVG file, which is a vector image format that allows for interactivity and scripting, attackers can execute malicious code on the victim's br

## Description

# Description

The SVG Alert WAF Bypass is a technique that can be used to bypass certain WAFs that are configured to block certain types of malicious payloads. By using an SVG file, which is a vector image format that allows for interactivity and scripting, attackers can execute malicious code on the victim's browser without being detected by the WAF. This technique was specifically tested against the Incapsula WAF and was found to be successful.

From an offensive perspective, this technique can be used to bypass security controls and deliver payloads that would otherwise be blocked. From a technical perspective, the attacker creates an SVG file that contains a payload and then sends it to the target. When the target's browser loads the SVG file, the payload is executed. From a business perspective, this technique can be used to gain access to sensitive information or to execute unauthorized actions on the target's system.

 

## Requirements

1. Access to a target that is protected by a WAF

1. Ability to create an SVG file with a payload

 

## Defense

1. Ensure that the WAF is configured to detect and block SVG files that contain scripts

1. Regularly update the WAF's rules to include new types of attacks

1. Monitor network traffic for any suspicious activity that may indicate a WAF bypass attempt

 

## Objectives

1. Bypass WAFs that are configured to block certain types of malicious payloads

1. Deliver payloads that would otherwise be blocked

 

# Instructions

1. The SVG Alert command is used to display an alert message on the screen using an SVG element.

 



**Code**: [[<svg onload=$.globalEval("alert()");>]]



> This command can be used to test the security of a web page by injecting malicious code into the SVG element. The 'onload' attribute is used to execute the 'alert()' function as soon as the SVG element is loaded on the page. The '$.globalEval()' function is used to execute the 'alert()' function in the global context of the page, which allows it to bypass any local scope restrictions. It is important to note that this command can be used for malicious purposes and should only be used for testing and educational purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Multilayer Encryption|T1079 - Multilayer Encryption]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Common WAF Bypass]]
- [[Cross Site Scripting]]
- [[Incapsula WAF Bypass by [@daveysec](https://twitter.com/daveysec/status/1126999990658670593) - 11th May 2019]]


