---
id: 9cfa19b9-5bf4-43ef-a849-5472d46f8ce8
name: PHP Deserialization - Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.310055+00:00'
updated_at: '2023-04-06T03:55:59.323721+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[General concept]]'
- '[[PHP Deserialization]]'
---

# PHP Deserialization - Code Execution

## Summary

PHP deserialization vulnerabilities arise when an application accepts user input that contains serialized PHP objects, which can be manipulated to execute arbitrary code on the server. This can lead to complete compromise of the server and sensitive data theft. In this specific case, the PHPObjectI

## Description

# Description

PHP deserialization vulnerabilities arise when an application accepts user input that contains serialized PHP objects, which can be manipulated to execute arbitrary code on the server. This can lead to complete compromise of the server and sensitive data theft. In this specific case, the PHPObjectInjection class is vulnerable to code injection via the 'inject' variable. An attacker can craft a malicious payload to execute arbitrary code on the server. This vulnerability can be exploited by an attacker who has access to user input fields in the application, such as a form or URL parameter. Business impact of this vulnerability includes data theft, server compromise, and reputational damage.

## Requirements

1. Access to user input fields in the application, such as a form or URL parameter.

1. Knowledge of PHP object serialization and deserialization.

1. A tool to craft malicious payloads, such as a Python script or Burp Suite.

## Defense

1. Validate and sanitize user input before accepting it.

1. Use a secure serialization format, such as JSON or XML.

1. Implement input validation and output encoding to prevent code injection attacks.

## Objectives

1. Exploit the PHP deserialization vulnerability to execute arbitrary code on the server.

1. Gain access to sensitive data on the server.

1. Compromise the server and establish a foothold for further attacks.

# Instructions

1. This PHP code defines a PHPObjectInjection class that is vulnerable to code injection via the 'inject' variable. The __wakeup() method is called when an object is unserialized and is used to execute the injected code. The 'r' parameter is used to pass serialized objects to the script.

**Code**: [[<?php 
    class PHPObjectInjection{
        publi]]

> An attacker can craft a malicious payload and pass it to the 'r' parameter to execute arbitrary code on the server.

2. This payload uses the PHPObjectInjection class to execute the 'whoami' command on the server. The payload is crafted by serializing the object and passing it to the 'r' parameter.

**Code**: [[# Basic serialized data
a:2:{i:0;s:4:"XVWA";i:1;s:]]

> An attacker can craft a payload to execute any arbitrary command on the server by modifying the 'inject' variable.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[General concept]]
- [[PHP Deserialization]]
