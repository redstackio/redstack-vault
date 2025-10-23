---
id: f709e346-bac4-410d-9f65-faa55fb9f8eb
name: XXE Injection in SOAP Messages
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.594347+00:00'
updated_at: '2023-04-10T20:24:46.919915+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Protocol Tunneling|T1572 - Protocol Tunneling]]'
tags:
- '[[XML External Entity]]'
- '[[XXE in exotic files]]'
- '[[XXE inside SOAP]]'
---

# XXE Injection in SOAP Messages

## Summary

XXE Injection in SOAP Messages is a technique used by attackers to exploit vulnerabilities in XML parsers that can be used to read and manipulate sensitive data. This technique can be used to exfiltrate data, execute arbitrary code on the server or gain unauthorized access to sensitive information.

## Description

# Description

XXE Injection in SOAP Messages is a technique used by attackers to exploit vulnerabilities in XML parsers that can be used to read and manipulate sensitive data. This technique can be used to exfiltrate data, execute arbitrary code on the server or gain unauthorized access to sensitive information. By injecting malicious XML entities into a SOAP message, attackers can bypass security controls and execute malicious commands on the server. This technique is commonly used in web applications that use SOAP-based web services.

 

## Requirements

1. Access to a web application that uses SOAP-based web services

1. Knowledge of XXE Injection

 

## Defense

1. Implement input validation and sanitization techniques to prevent XXE Injection attacks

1. Use a web application firewall to detect and block malicious requests

1. Disable external entity processing in XML parsers

 

## Objectives

1. Inject malicious XML entities into a SOAP message

1. Bypass security controls and execute malicious commands on the server

1. Exfiltrate sensitive data from the server

 

# Instructions

1. The above XML data contains an external entity injection vulnerability. It is achieved by defining an external entity with a URL that points to an attacker controlled server. When the XML is parsed, the server will be requested and the response will be included in the XML document. This can lead to sensitive data disclosure or even remote code execution.

 



**Code**: [[<soap:Body>
  <foo>
    <![CDATA[<!DOCTYPE doc [<!]]



> To prevent this vulnerability, it is recommended to disable external entity parsing or to use a whitelist approach where only known safe external entities are allowed to be parsed.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Protocol Tunneling|T1572 - Protocol Tunneling]]

## Tags

- [[XML External Entity]]
- [[XXE in exotic files]]
- [[XXE inside SOAP]]


