---
id: 8094db2d-16df-4e85-a0ff-df2d7ddafac8
name: Wrapper Data LFI/RFI
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.378288+00:00'
updated_at: '2023-04-10T20:22:17.995529+00:00'
tags:
- '[[File Inclusion]]'
- '[[LFI / RFI using wrappers]]'
- '[[Wrapper data://]]'
---

# Wrapper Data LFI/RFI

## Summary

Wrapper data:// is a protocol that allows inclusion of data directly in the URL. This can be abused to perform Local File Inclusion (LFI) and Remote File Inclusion (RFI) attacks. In LFI attacks, the attacker can include files from the local system, while in RFI attacks, the attacker can include fil

## Description

# Description

Wrapper data:// is a protocol that allows inclusion of data directly in the URL. This can be abused to perform Local File Inclusion (LFI) and Remote File Inclusion (RFI) attacks. In LFI attacks, the attacker can include files from the local system, while in RFI attacks, the attacker can include files from a remote system. This technique can be used by an attacker to execute arbitrary code on the target system or to bypass security controls. This can be achieved by encoding the payload in base64 and passing it as a parameter in the URL.

 

## Requirements

1. Access to the target system

1. Knowledge of the target system's file structure

1. Ability to encode payloads in base64

 

## Defense

1. Implement input validation and sanitization techniques to prevent injection attacks

1. Use a web application firewall to detect and block malicious requests

1. Disable or restrict the use of data:// wrapper

 

## Objectives

1. To include and execute arbitrary code on the target system

1. To bypass security controls and gain unauthorized access to sensitive data

 

# Instructions

1. 1. Encode the PHP shell payload in base64
2. Pass the encoded payload as a parameter in the URL using the data:// wrapper
3. Execute the command to include and execute the PHP shell

 



**Code**: [[http://example.net/?page=data://text/plain;base64,]]



> The payload is encoded in base64 and passed as a parameter in the URL using the data:// wrapper. The PHP shell will be included and executed on the target system, allowing the attacker to execute arbitrary code.

2. 1. Encode the PHP script payload in base64
2. Pass the encoded payload as a parameter in the URL using the data:// wrapper
3. Execute the command to include and execute the PHP script

 



**Code**: [[http://example.com/index.php?page=data:application]]



> The payload is encoded in base64 and passed as a parameter in the URL using the data:// wrapper. The PHP script will be included and executed on the target system, allowing the attacker to trigger an XSS and bypass the Chrome Auditor.

## Tags

- [[File Inclusion]]
- [[LFI / RFI using wrappers]]
- [[Wrapper data://]]


