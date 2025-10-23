---
id: 8028cdc0-349d-4f2e-80f6-c34f825ff619
name: XXE File Retrieval via Base64 Encoding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.168196+00:00'
updated_at: '2023-04-10T20:24:41.523411+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Create Account|T1136 - Create Account]]'
tags:
- '[[Classic XXE Base64 encoded]]'
- '[[Exploiting XXE to retrieve files]]'
- '[[XML External Entity]]'
---

# XXE File Retrieval via Base64 Encoding

## Summary

This procedure involves exploiting the XML External Entity (XXE) vulnerability to retrieve files from a target system through Base64 encoding. This technique can be used to retrieve sensitive files that may contain credentials, configuration files, or other sensitive information. Attackers can use 

## Description

# Description

This procedure involves exploiting the XML External Entity (XXE) vulnerability to retrieve files from a target system through Base64 encoding. This technique can be used to retrieve sensitive files that may contain credentials, configuration files, or other sensitive information. Attackers can use this information to further their attack and gain unauthorized access to the target system.

To exploit this vulnerability, attackers can inject malicious XML code into an application that uses an XML parser. The malicious code can then execute a request to retrieve a file from the target system. The retrieved file is then encoded in Base64 format and sent back to the attacker's system.

 

## Requirements

1. Access to a vulnerable application that uses an XML parser

 

## Defense

1. Implement input validation and sanitization to prevent malicious XML code injection

1. Use a web application firewall (WAF) to detect and block malicious requests

1. Disable external entity parsing in the XML parser configuration to prevent XXE attacks

 

## Objectives

1. Retrieve sensitive files from the target system

 

# Instructions

1. The provided XML data contains a DOCTYPE declaration with an external entity reference that can be manipulated to inject arbitrary content into the XML document.

 



**Code**: [[<!DOCTYPE test [ <!ENTITY % init SYSTEM "data://te]]



> This vulnerability can be exploited to perform XML External Entity (XXE) attacks, which can lead to sensitive information disclosure or server-side request forgery (SSRF) attacks. It is recommended to properly validate and sanitize all XML input data to prevent XXE vulnerabilities.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Create Account|T1136 - Create Account]]

## Tags

- [[Classic XXE Base64 encoded]]
- [[Exploiting XXE to retrieve files]]
- [[XML External Entity]]


