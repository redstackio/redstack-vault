---
id: c4c56f73-3d85-47e3-86d5-4472dc6237a4
name: Symmetric Cryptography
type: sub-technique
mitre_id: T1573.001
mitre_url: null
created_at: '2023-04-06T00:31:25.750918+00:00'
updated_at: '2023-04-06T00:31:25.750918+00:00'
parent_technique: '[[Encrypted Channel|T1573 - Encrypted Channel]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Symmetric Cryptography

**MITRE ID**: T1573.001

**Parent Technique**: [[Encrypted Channel|T1573 - Encrypted Channel]]

This is a sub-technique of T1573 - Encrypted Channel.

## Summary

Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Symmetric encryption algorithms use the same key for plaintext encryption and ciphertext decryption. Common symme

## Description

Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Symmetric encryption algorithms use the same key for plaintext encryption and ciphertext decryption. Common symmetric encryption algorithms include AES, DES, 3DES, Blowfish, and RC4.

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
