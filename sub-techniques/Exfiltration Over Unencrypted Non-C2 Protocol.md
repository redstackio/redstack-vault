---
id: c20ef4f7-3257-4256-9cc2-330cd784ade7
name: Exfiltration Over Unencrypted Non-C2 Protocol
type: sub-technique
mitre_id: T1048.003
mitre_url: null
created_at: '2023-04-06T00:31:27.232940+00:00'
updated_at: '2023-04-06T00:31:27.232940+00:00'
parent_technique: '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over
  Alternative Protocol]]'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[AWS S3 Download by Authenticated User]]'
- '[[IAM-Based Authentication Data Exfiltration via RDS]]'
- '[[RDS Password-based Authentication Data Exfiltration]]'
- '[[Remote File Read via Jinja2 Server-Side Template Injection]]'
---

# Exfiltration Over Unencrypted Non-C2 Protocol

**MITRE ID**: T1048.003

**Parent Technique**: [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

This is a sub-technique of T1048 - Exfiltration Over Alternative Protocol.

## Summary

Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Adversaries may opt to obfuscate this data, without 

## Description

Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Adversaries may opt to obfuscate this data, without the use of encryption, within network protocols that are natively unencrypted (such as HTTP, FTP, or DNS). This may include custom or publicly available encoding/compression algorithms (such as base64) as well as embedding data within protocol headers and fields. 

## Tactics

This sub-technique is used in the following tactics:

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures

There are 4 procedures using this sub-technique:

- [[AWS S3 Download by Authenticated User]]
- [[IAM-Based Authentication Data Exfiltration via RDS]]
- [[RDS Password-based Authentication Data Exfiltration]]
- [[Remote File Read via Jinja2 Server-Side Template Injection]]
