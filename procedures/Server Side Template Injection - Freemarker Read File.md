---
id: 95711378-5247-47c0-956e-b348bf95e0b0
name: Server Side Template Injection - Freemarker Read File
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.031899+00:00'
updated_at: '2023-04-10T20:23:39.230491+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Freemarker]]'
- '[[Freemarker - Read File]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection - Freemarker Read File

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server-side. Freemarker is a Java-based template engine that is often used in web applications. This procedure specifically targets the ability to read files on the server using Freemar

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server-side. Freemarker is a Java-based template engine that is often used in web applications. This procedure specifically targets the ability to read files on the server using Freemarker. An attacker can use this technique to read sensitive files, such as configuration files, that may contain credentials or other sensitive information. 

To execute this procedure, the attacker would first need to identify that the web application is using Freemarker as a template engine. They would then need to identify an injection point, such as a form field, where they can inject their payload. Once the payload is injected, the attacker can read files on the server using the Freemarker `include` directive.

This procedure can be used to gain access to sensitive information stored on the server, which can be used to further compromise the system or exfiltrate data.

 

## Requirements

1. Knowledge of the target web application's use of Freemarker

1. Identification of an injection point

 

## Defense

1. Ensure that the web application is up-to-date with the latest version of Freemarker, which may include patches for known vulnerabilities

1. Implement input validation and sanitization techniques to prevent injection attacks

1. Use file system permissions to restrict access to sensitive files and directories

 

## Objectives

1. Read sensitive files on the server

1. Gather information for further attacks

 

# Instructions

1. This command retrieves the location of the class file of a product object. Replace 'path_to_the_file' with the actual path to the file on your system.

 



**Code**: [[${product.getClass().getProtectionDomain().getCode]]



> The 'product' in the command refers to a product object in the code. This command retrieves the location of the class file of the product object and returns the bytes in the form of an array. The 'join()' function is used to convert the byte array to ASCII format. This command can be useful for debugging and troubleshooting purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Freemarker]]
- [[Freemarker - Read File]]
- [[Server Side Template Injection]]


