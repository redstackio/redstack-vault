---
id: 583f7656-ad3a-458e-b823-3d423fe856bb
name: Asymmetric Cryptography
type: sub-technique
mitre_id: T1573.002
mitre_url: null
created_at: '2023-04-06T00:31:26.844403+00:00'
updated_at: '2023-04-06T00:31:26.844403+00:00'
parent_technique: '[[Encrypted Channel|T1573 - Encrypted Channel]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Asymmetric Cryptography

**MITRE ID**: T1573.002

**Parent Technique**: [[Encrypted Channel|T1573 - Encrypted Channel]]

This is a sub-technique of T1573 - Encrypted Channel.

## Summary

Adversaries may employ a known asymmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Asymmetric cryptography, also known as public key cryptography, uses a keypair per party: one public that can be

## Description

Adversaries may employ a known asymmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Asymmetric cryptography, also known as public key cryptography, uses a keypair per party: one public that can be freely distributed, and one private. Due to how the keys are generated, the sender encrypts data with the receiver’s public key and the receiver decrypts the data with their private key. This ensures that only the intended recipient can read the encrypted data. Common public key encryption algorithms include RSA and ElGamal.

For efficiency, many protocols (including SSL/TLS) use symmetric cryptography once a connection is established, but use asymmetric cryptography to establish or transmit a key. As such, these protocols are classified as [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002).

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
