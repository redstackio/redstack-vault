---
id: d8d46d50-b260-460e-b92b-af4417cc4221
name: CSRF Payload to Set Role to Admin via JSON POST
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.234790+00:00'
updated_at: '2023-04-10T20:21:26.562252+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Control Panel Items|T1196 - Control Panel Items]]'
tags:
- '[[Cross-Site Request Forgery]]'
- '[[JSON POST - Simple Request]]'
- '[[Payloads]]'
---

# CSRF Payload to Set Role to Admin via JSON POST

## Summary

This payload demonstrates how an attacker can use a Cross-Site Request Forgery (CSRF) attack to set a user's role to 'admin' via a JSON POST request. In a CSRF attack, the attacker tricks a victim into unknowingly executing a malicious action on a website they are logged into. In this case, the att

## Description

# Description

This payload demonstrates how an attacker can use a Cross-Site Request Forgery (CSRF) attack to set a user's role to 'admin' via a JSON POST request. In a CSRF attack, the attacker tricks a victim into unknowingly executing a malicious action on a website they are logged into. In this case, the attacker is able to change the victim's role to 'admin' by sending a crafted JSON POST request to the server. This can result in the attacker gaining full control over the victim's account and potentially the entire system.

To execute this attack, the attacker needs to craft a malicious webpage that includes the above script. They then need to trick the victim into visiting the page while they are logged into the target website.

 

## Requirements

1. The victim needs to be logged into the target website

1. The attacker needs to be able to craft a malicious webpage and trick the victim into visiting it

 

## Defense

1. Implement CSRF tokens to ensure that requests are only executed if they originate from a legitimate source

1. Use the 'Content-Type: application/json' header to ensure that JSON POST requests are only accepted from legitimate sources

1. Implement strict access controls and role-based permissions to limit the damage that can be done if an attacker is able to change a user's role

 

## Objectives

1. Change the victim's role to 'admin'

1. Gain full control over the victim's account and potentially the entire system

 

# Instructions

1. Craft a malicious webpage that includes the above script

 



**Code**: [[<script>
var xhr = new XMLHttpRequest();
xhr.open(]]



> This script sends a JSON POST request to the server with the payload '{"role":admin}'. This will set the victim's role to 'admin' if the victim is logged into the target website and visits the attacker's malicious webpage.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Control Panel Items|T1196 - Control Panel Items]]

## Tags

- [[Cross-Site Request Forgery]]
- [[JSON POST - Simple Request]]
- [[Payloads]]


