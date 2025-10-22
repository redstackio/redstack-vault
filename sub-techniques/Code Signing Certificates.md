---
id: 184eb674-6b1b-483b-a805-5eff52b4c861
name: Code Signing Certificates
type: sub-technique
mitre_id: T1588.003
mitre_url: null
created_at: '2023-04-06T00:31:27.112023+00:00'
updated_at: '2023-04-06T00:31:27.112023+00:00'
parent_technique: '[[Obtain Capabilities|T1588 - Obtain Capabilities]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Code Signing Certificates

**MITRE ID**: T1588.003

**Parent Technique**: [[Obtain Capabilities|T1588 - Obtain Capabilities]]

This is a sub-technique of T1588 - Obtain Capabilities.

## Summary

Adversaries may buy and/or steal code signing certificates that can be used during targeting. Code signing is the process of digitally signing executables and scripts to confirm the software author and guarantee that the code has not been altered or corrupted. Code signing provides a level of authen

## Description

Adversaries may buy and/or steal code signing certificates that can be used during targeting. Code signing is the process of digitally signing executables and scripts to confirm the software author and guarantee that the code has not been altered or corrupted. Code signing provides a level of authenticity for a program from the developer and a guarantee that the program has not been tampered with.(Citation: Wikipedia Code Signing) Users and/or security tools may trust a signed piece of code more than an unsigned piece of code even if they don't know who issued the certificate or who the author is.

Prior to [Code Signing](https://attack.mitre.org/techniques/T1553/002), adversaries may purchase or steal code signing certificates for use in operations. The purchase of code signing certificates may be done using a front organization or using information stolen from a previously compromised entity that allows the adversary to validate to a certificate provider as that entity. Adversaries may also steal code signing materials directly from a compromised third-party.

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]
