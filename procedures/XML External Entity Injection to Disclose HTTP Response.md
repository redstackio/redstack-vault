---
id: 9c567193-5133-4a9b-bca6-a42f1601f287
name: XML External Entity Injection to Disclose HTTP Response
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.729985+00:00'
updated_at: '2023-04-10T20:24:42.660186+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Disclose HTTP Response:]]'
- '[[Windows Local DTD and Side Channel Leak to disclose HTTP response/file contents]]'
- '[[XML External Entity]]'
---

# XML External Entity Injection to Disclose HTTP Response

## Summary

XML External Entity (XXE) Injection is a type of attack against an application that parses XML input. The attacker can inject specially crafted XML that can be used to disclose sensitive data, execute remote code, or perform denial of service attacks. In this case, the attacker is using XXE Injecti

## Description

# Description

XML External Entity (XXE) Injection is a type of attack against an application that parses XML input. The attacker can inject specially crafted XML that can be used to disclose sensitive data, execute remote code, or perform denial of service attacks. In this case, the attacker is using XXE Injection to disclose HTTP response or file contents. The attack is performed by injecting a specially crafted XML file that contains a reference to an external entity that points to the file or HTTP response that the attacker wants to disclose. When the XML parser processes the XML input, it will fetch the external entity and include its content in the XML output. This can be used to disclose sensitive information such as passwords, user data, or confidential business information.

## Requirements

1. Access to a vulnerable application that parses XML input

1. Knowledge of the XML syntax and XXE Injection technique

## Defense

1. Implement input validation and sanitization to prevent XXE Injection attacks

1. Disable XML external entity processing in the parser configuration

1. Use a web application firewall (WAF) to detect and block XXE Injection attacks

## Objectives

1. Disclose HTTP response or file contents

# Instructions

1. Modify the XML document to prevent external entities from being included.

**Code**: [[<!DOCTYPE doc [
    <!ENTITY % local_dtd SYSTEM "f]]

> The XML document contains an external entity injection vulnerability that allows an attacker to read arbitrary files on the server. To fix this vulnerability, the XML document should be modified to prevent external entities from being included. This can be done by disabling the use of external entities in the XML parser or by using a whitelist approach to only allow specific entities to be included.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Tags

- [[Disclose HTTP Response:]]
- [[Windows Local DTD and Side Channel Leak to disclose HTTP response/file contents]]
- [[XML External Entity]]
