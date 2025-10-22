---
id: 0931a1c6-7556-4fd1-96fd-d52dd166fbc0
name: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
type: sub-technique
mitre_id: T1048.002
mitre_url: null
created_at: '2023-04-06T00:31:26.554670+00:00'
updated_at: '2023-04-06T00:31:26.554670+00:00'
parent_technique: '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over
  Alternative Protocol]]'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[AWS KMS Decrypt Exfiltration]]'
- '[[IAM-Based Authentication Data Exfiltration via RDS]]'
---

# Exfiltration Over Asymmetric Encrypted Non-C2 Protocol

**MITRE ID**: T1048.002

**Parent Technique**: [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

This is a sub-technique of T1048 - Exfiltration Over Alternative Protocol.

## Summary

Adversaries may steal data by exfiltrating it over an asymmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Asymmetric encryption algorithms are tho

## Description

Adversaries may steal data by exfiltrating it over an asymmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Asymmetric encryption algorithms are those that use different keys on each end of the channel. Also known as public-key cryptography, this requires pairs of cryptographic keys that can encrypt/decrypt data from the corresponding key. Each end of the communication channels requires a private key (only in the procession of that entity) and the public key of the other entity. The public keys of each entity are exchanged before encrypted communications begin. 

Network protocols that use asymmetric encryption (such as HTTPS/TLS/SSL) often utilize symmetric encryption once keys are exchanged. Adversaries may opt to use these encrypted mechanisms that are baked into a protocol. 

## Tactics

This sub-technique is used in the following tactics:

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[AWS KMS Decrypt Exfiltration]]
- [[IAM-Based Authentication Data Exfiltration via RDS]]
