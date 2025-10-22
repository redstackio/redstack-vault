---
id: 1f0c1441-39ec-44a5-a1c6-5338be6f934c
name: XXE File Retrieval with PHP Wrapper
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.190304+00:00'
updated_at: '2023-04-10T20:24:40.736454+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Exploiting XXE to retrieve files]]'
- '[[PHP Wrapper inside XXE]]'
- '[[XML External Entity]]'
---

# XXE File Retrieval with PHP Wrapper

## Summary

This procedure targets a vulnerability in XML parsers that allows an attacker to use XML External Entity (XXE) injection to retrieve sensitive files from a target system. Specifically, this procedure exploits a PHP wrapper inside XXE to retrieve Base64 encoded resources from a remote server. The at

## Description

# Description

This procedure targets a vulnerability in XML parsers that allows an attacker to use XML External Entity (XXE) injection to retrieve sensitive files from a target system. Specifically, this procedure exploits a PHP wrapper inside XXE to retrieve Base64 encoded resources from a remote server. The attacker crafts a malicious XML file containing an external entity that references the PHP wrapper and the remote server. When the XML file is processed by the vulnerable parser, the wrapper is executed and the resource is retrieved. This can be used to steal sensitive data or execute arbitrary code on the target system.

## Requirements

1. Access to a vulnerable XML parser on the target system

1. Knowledge of the file path and name of the sensitive file to retrieve

1. Access to a remote server to host the Base64 encoded resource

## Defense

1. Implement input validation and sanitization on all XML input to prevent XXE injection

1. Disable or restrict access to vulnerable XML parsers

1. Use firewalls and intrusion detection systems to monitor and block suspicious network traffic

## Objectives

1. Retrieve sensitive files from the target system

1. Execute arbitrary code on the target system

# Instructions

1. Exploit the XML parser's ability to include external entities or files to retrieve sensitive information or execute system commands.

**Code**: [[<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filt]]

> The XML External Entity Injection (XXE) attack is a type of attack against applications that parse XML input. It occurs when an attacker is able to inject an XML document with external entities or files that can be processed by the XML parser. If the XML parser does not have appropriate security configurations, it will include the external entities, which can be used to retrieve sensitive information or execute system commands. To prevent this type of attack, applications should disable external entities or use a secure XML parser.

2. Use this command to retrieve a base64 encoded resource from a remote server using the XXE injection vulnerability.

**Code**: [[<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCT]]

> This command exploits the XXE injection vulnerability to retrieve a resource from a remote server. The resource is then encoded in base64 format and returned as a string. The resource can be any file type such as a PHP script or a configuration file. This command can be used to gain unauthorized access to sensitive information or execute arbitrary code on the remote server.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Exploiting XXE to retrieve files]]
- [[PHP Wrapper inside XXE]]
- [[XML External Entity]]
