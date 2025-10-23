---
id: 3429d7c2-c581-4908-9d8d-be58e8c90cfb
name: SSRF via XXE Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.246064+00:00'
updated_at: '2023-04-10T20:24:43.415381+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[External Remote Services|T1133 - External Remote Services]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Exploiting XXE to perform SSRF attacks]]'
- '[[XML External Entity]]'
---

# SSRF via XXE Injection

## Summary

This procedure involves exploiting XXE to perform Server-Side Request Forgery (SSRF) attacks. An attacker can send a specially crafted XML file to a vulnerable application that processes XML input. The XML file contains an external entity that references an external resource, which can be a URL. Wh

## Description

# Description

This procedure involves exploiting XXE to perform Server-Side Request Forgery (SSRF) attacks. An attacker can send a specially crafted XML file to a vulnerable application that processes XML input. The XML file contains an external entity that references an external resource, which can be a URL. When the application processes the XML file, it resolves the external entity and makes a request to the specified URL, effectively performing an SSRF attack. This can allow an attacker to access internal resources that are not directly accessible from the internet, such as databases or internal web applications.

From a technical perspective, XXE injection is possible when an application parses XML input without disabling external entities. The attacker can craft an XML file that contains an external entity with a specially crafted value that can be used to perform an SSRF attack. The business value of this attack is that it allows an attacker to bypass network security controls and access sensitive internal resources.


 

## Requirements

1. Access to a vulnerable application that processes XML input

1. Knowledge of XXE injection techniques

 

## Defense

1. Disable external entities in XML parsers

1. Implement input validation and sanitization to prevent XXE injection

1. Monitor network traffic for suspicious requests and investigate any SSRF-like behavior

 

## Objectives

1. Perform an SSRF attack to access internal resources

1. Bypass network security controls

 

# Instructions

1. To prevent XXE injection, disable external entity processing in the XML parser or use a whitelist approach to only allow known safe entities.

 



**Code**: [[<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCT]]



> XML External Entity (XXE) Injection is a type of attack that exploits the way XML parsers process external entities. An attacker can define an external entity that references sensitive files or resources on the server, which can then be included in the parsed XML document. This can lead to disclosure of sensitive information, denial of service, or even remote code execution. To prevent XXE injection, it is important to disable external entity processing in the XML parser or use a whitelist approach to only allow known safe entities.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[External Remote Services|T1133 - External Remote Services]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Tags

- [[Exploiting XXE to perform SSRF attacks]]
- [[XML External Entity]]


