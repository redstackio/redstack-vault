---
id: 5f598a00-a8b5-49ab-bf78-4d46cddcc41e
name: Exfiltration Over Symmetric Encrypted Non-C2 Protocol
type: sub-technique
mitre_id: T1048.001
mitre_url: null
created_at: '2023-04-06T00:31:26.392646+00:00'
updated_at: '2023-04-06T00:31:26.392646+00:00'
parent_technique: '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over
  Alternative Protocol]]'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
---

# Exfiltration Over Symmetric Encrypted Non-C2 Protocol

**MITRE ID**: T1048.001

**Parent Technique**: [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

This is a sub-technique of T1048 - Exfiltration Over Alternative Protocol.

## Summary

Adversaries may steal data by exfiltrating it over a symmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Symmetric encryption algorithms are those 

## Description

Adversaries may steal data by exfiltrating it over a symmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Symmetric encryption algorithms are those that use shared or the same keys/secrets on each end of the channel. This requires an exchange or pre-arranged agreement/possession of the value used to encrypt and decrypt data. 

Network protocols that use asymmetric encryption often utilize symmetric encryption once keys are exchanged, but adversaries may opt to manually share keys and implement symmetric cryptographic algorithms (ex: RC4, AES) vice using mechanisms that are baked into a protocol. This may result in multiple layers of encryption (in protocols that are natively encrypted such as HTTPS) or encryption in protocols that not typically encrypted (such as HTTP or FTP). 

## Tactics

This sub-technique is used in the following tactics:

- [[Exfiltration|TA0010 - Exfiltration]]
