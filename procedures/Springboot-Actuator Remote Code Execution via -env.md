---
id: ef678905-d54a-42c2-a449-fc177ed529e2
name: Springboot-Actuator Remote Code Execution via /env
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.759083+00:00'
updated_at: '2023-04-10T20:22:31.727673+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Insecure Management Interface]]'
- '[[Remote Code Execution via `/env`]]'
- '[[Springboot-Actuator]]'
- '[[Steps]]'
---

# Springboot-Actuator Remote Code Execution via /env

## Summary

Springboot-Actuator is a useful tool for monitoring and managing Spring Boot applications. However, if it is not properly secured, it can also be used by attackers to execute arbitrary code on the victim's machine. The vulnerability arises from the fact that the /env endpoint of Springboot-Actuator

## Description

# Description

Springboot-Actuator is a useful tool for monitoring and managing Spring Boot applications. However, if it is not properly secured, it can also be used by attackers to execute arbitrary code on the victim's machine. The vulnerability arises from the fact that the /env endpoint of Springboot-Actuator allows unauthenticated access and can be used to inject malicious code.

An attacker can exploit this vulnerability by sending a specially crafted POST request to the /refresh endpoint with the malicious code as the payload. This will cause the victim's machine to execute the code and potentially give the attacker full control of the system. This vulnerability can be used to steal sensitive data, install malware, or launch further attacks against the victim's network.

The business value of this attack is that it can be used to gain access to sensitive data and systems, which can be used for financial gain, espionage, or sabotage.

## Requirements

1. Access to the victim's Spring Boot application

1. Knowledge of the victim's Springboot-Actuator configuration

## Defense

1. Secure the Springboot-Actuator by disabling the /env endpoint or requiring authentication for access.

1. Implement strict input validation to prevent injection attacks.

1. Monitor the network for suspicious activity and block IP addresses that are attempting to exploit this vulnerability.

## Objectives

1. Execute arbitrary code on the victim's machine

1. Gain access to sensitive data and systems

# Instructions

1. Send POST request to /refresh endpoint

**Code**: [[POST /refresh HTTP/1.1
Host: victim.example:8090
C]]

> The payload should contain the malicious code that will be executed on the victim's machine. The attacker should modify the payload to contain their own code.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Tags

- [[Insecure Management Interface]]
- [[Remote Code Execution via `/env`]]
- [[Springboot-Actuator]]
- [[Steps]]
