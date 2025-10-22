---
id: 793cc2aa-8b11-4f43-b267-a9523b413c15
name: Blind XXE Out-of-Band Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.366002+00:00'
updated_at: '2023-04-10T20:24:38.722211+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Create Account|T1136 - Create Account]]'
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
tags:
- '[[Basic Blind XXE]]'
- '[[Exploiting blind XXE to exfiltrate data out-of-band]]'
- '[[XML External Entity]]'
commands:
- '[[View Password File]]'
---

# Blind XXE Out-of-Band Data Exfiltration

## Summary

Blind XXE Out-of-Band Data Exfiltration is a technique used by attackers to extract sensitive data from a target system using XML External Entity (XXE) injection. This technique is called 'blind' because it does not return any data to the attacker's system, but rather sends the data out-of-band to 

## Description

# Description

Blind XXE Out-of-Band Data Exfiltration is a technique used by attackers to extract sensitive data from a target system using XML External Entity (XXE) injection. This technique is called 'blind' because it does not return any data to the attacker's system, but rather sends the data out-of-band to a location controlled by the attacker. This is useful for attackers who cannot establish a direct connection to the target system, or who wish to avoid detection by security controls that monitor network traffic.

To execute this attack, the attacker first injects a malicious XML payload into a vulnerable application that parses XML input. The payload contains a reference to an external entity that points to a location controlled by the attacker. When the application processes the XML input, it sends a request to the attacker's server to retrieve the external entity. The attacker can then intercept this request and use it to exfiltrate data from the target system.

The business value of this attack is that it allows an attacker to steal sensitive data from a target system without being detected. This can lead to data breaches, financial loss, and damage to the target's reputation. The technical explanation of this attack involves sending malicious XML payloads to exploit vulnerable XML parsers, which can allow attackers to retrieve sensitive data from the target system.

## Requirements

1. Access to a vulnerable application that parses XML input

1. Ability to inject malicious XML payloads

1. Ability to intercept network traffic

## Defense

1. Implement input validation and sanitization techniques to prevent XXE injection attacks

1. Use a Web Application Firewall (WAF) to detect and block malicious traffic

1. Monitor network traffic for unusual activity, such as large amounts of data being sent to external locations

## Objectives

1. Exfiltrate sensitive data from a target system

1. Avoid detection by security controls that monitor network traffic

# Instructions

1. To extract data using out-of-band techniques, you can send requests to a controlled server or service that will receive the data. In this example, we are using a Burp Collaborator server to receive data via an XML external entity (XXE) attack.

**Code**: [[<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY %]]

> The 'data' field contains an XML payload that includes an external entity reference to a Burp Collaborator server. When the XML parser processes the payload, it will make a request to the specified server, which will receive the request and log the interaction. By monitoring the requests made to the Burp Collaborator server, we can extract data that was not directly outputted in the page. This technique can be used to bypass input validation and filtering, and to extract sensitive information such as credentials or configuration files.

2. To view the content of the password file, use the 'cat' command followed by the file path. For example: cat /etc/passwd

**Code**: [[/etc/passwd]]

> The '/etc/passwd' file stores user account information, such as usernames, user IDs, home directories, and default shells. This file is commonly used by system administrators to manage user accounts and permissions.

**Command** ([[View Password File]]):

```bash
/etc/passwd
```

3. The XML External Entity (XXE) attack is a type of attack against an application that parses XML input. An attacker can use it to send specially crafted XML input to the application, which will be then parsed and executed by the XML parser. This can lead to the disclosure of confidential data, denial of service, server-side request forgery, and other types of attacks.

**Code**: [[<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCT]]

> In the given data, the attacker has defined two entities, %xxe and callhome, in the DTD section. The %xxe entity is defined to point to the /etc/passwd file on the server. The callhome entity is defined to make a request to a malicious website with the %xxe entity as a parameter. When the XML parser processes the XML input, it will substitute the entities and execute the contents of the %xxe entity, resulting in the disclosure of the contents of the /etc/passwd file and the execution of the callhome entity, which can be used to exfiltrate the data to a remote server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Exfiltration|TA0010 - Exfiltration]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Create Account|T1136 - Create Account]]
- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Commands Used

- [[View Password File]]

## Tags

- [[Basic Blind XXE]]
- [[Exploiting blind XXE to exfiltrate data out-of-band]]
- [[XML External Entity]]
