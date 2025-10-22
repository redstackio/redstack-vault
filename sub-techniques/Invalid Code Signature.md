---
id: d1de99e1-d4e6-40b0-a9d7-7758b2c94515
name: Invalid Code Signature
type: sub-technique
mitre_id: T1036.001
mitre_url: null
created_at: '2023-04-06T00:31:26.769463+00:00'
updated_at: '2023-04-06T00:31:26.769463+00:00'
parent_technique: '[[Masquerading|T1036 - Masquerading]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Invalid Code Signature

**MITRE ID**: T1036.001

**Parent Technique**: [[Masquerading|T1036 - Masquerading]]

This is a sub-technique of T1036 - Masquerading.

## Summary

Adversaries may attempt to mimic features of valid code signatures to increase the chance of deceiving a user, analyst, or tool. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. Adversaries can copy the metadata 

## Description

Adversaries may attempt to mimic features of valid code signatures to increase the chance of deceiving a user, analyst, or tool. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. Adversaries can copy the metadata and signature information from a signed program, then use it as a template for an unsigned program. Files with invalid code signatures will fail digital signature validation checks, but they may appear more legitimate to users and security tools may improperly handle these files.(Citation: Threatexpress MetaTwin 2017)

Unlike [Code Signing](https://attack.mitre.org/techniques/T1553/002), this activity will not result in a valid signature.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
