---
id: 9c2d0bae-5f35-4537-bb12-d15e99f200d8
name: Windows Local DTD and Side Channel Leak to Disclose HTTP Response/File Contents
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.708053+00:00'
updated_at: '2023-04-10T20:24:46.513357+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Disclose local file]]'
- '[[Windows Local DTD and Side Channel Leak to disclose HTTP response/file contents]]'
- '[[XML External Entity]]'
---

# Windows Local DTD and Side Channel Leak to Disclose HTTP Response/File Contents

## Summary

This procedure involves exploiting a vulnerability in XML parsers that allows an attacker to disclose local files. By injecting malicious code into an XML file, an attacker can cause the parser to disclose the contents of a local file. This can be used to exfiltrate sensitive information from a vic

## Description

# Description

This procedure involves exploiting a vulnerability in XML parsers that allows an attacker to disclose local files. By injecting malicious code into an XML file, an attacker can cause the parser to disclose the contents of a local file. This can be used to exfiltrate sensitive information from a victim's system, such as HTTP response or file contents. This attack can be particularly effective if the victim is running an outdated or vulnerable version of an XML parser.

To execute this attack, the attacker must have access to the victim's system and be able to inject malicious code into an XML file. The attacker must also have knowledge of the location of the file they wish to disclose. This attack can be used by threat actors to gain access to sensitive information, such as user credentials or confidential documents.

## Requirements

1. Access to the victim's system

1. Ability to inject malicious code into an XML file

## Defense

1. Ensure that XML parsers are up-to-date and not vulnerable to exploitation

1. Implement strict input validation and sanitization to prevent injection attacks

1. Monitor network traffic for suspicious activity, such as large data transfers or unusual XML file requests

## Objectives

1. Disclose the contents of a local file

1. Exfiltrate sensitive information from a victim's system

# Instructions

1. This command is used to exploit XML External Entity (XXE) vulnerabilities. The attacker sends a malicious XML file to the server that contains an external entity reference to a file on the server. When the server processes the XML file, it reads the contents of the referenced file and includes it in the response. This can lead to sensitive information disclosure, denial of service, or even remote code execution. 

**Code**: [[<!DOCTYPE doc [
    <!ENTITY % local_dtd SYSTEM "f]]

> The 'data' field contains the payload for the XXE attack. The payload includes a reference to a local DTD file that defines an external entity 'file' that points to a file on the server. The payload also includes an entity 'eval' that defines another entity 'error' that reads the contents of the 'file' entity and sends it to an external server. Finally, the payload defines an entity 'test' that is not used, but it is necessary to close the DTD definition. The 'lang' field specifies that the payload is in XML format. The 'text' field provides the source of the payload. The 'instruction' field explains how to use the payload to exploit the XXE vulnerability. 

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Tags

- [[Disclose local file]]
- [[Windows Local DTD and Side Channel Leak to disclose HTTP response/file contents]]
- [[XML External Entity]]
