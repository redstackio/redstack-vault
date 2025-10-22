---
id: f5c78304-d779-47ea-b6ef-a96f147b7cc0
name: Encrypted Channel
type: technique
mitre_id: T1573
mitre_url: null
created_at: '2023-04-06T00:31:26.804346+00:00'
updated_at: '2023-04-06T03:56:32.252871+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[Cobalt Strike Lateral Movement via Beacon Remote Exploits and Executes]]'
- '[[Git Source Code Leakage]]'
- '[[OpenSSL Reverse Shell]]'
- '[[SAML Injection for Authentication Bypass]]'
---

# Encrypted Channel

**MITRE ID**: T1573

## Description

Adversaries may employ a known encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration files.

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (4)

- [[Cobalt Strike Lateral Movement via Beacon Remote Exploits and Executes]]
- [[Git Source Code Leakage]]
- [[OpenSSL Reverse Shell]]
- [[SAML Injection for Authentication Bypass]]
