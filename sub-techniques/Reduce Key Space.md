---
id: fde0f3e9-f3d0-4e88-a1f3-c075fcbe7a7e
name: Reduce Key Space
type: sub-technique
mitre_id: T1600.001
mitre_url: null
created_at: '2023-04-06T00:31:25.943869+00:00'
updated_at: '2023-04-06T00:31:25.943869+00:00'
parent_technique: '[[Weaken Encryption|T1600 - Weaken Encryption]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Reduce Key Space

**MITRE ID**: T1600.001

**Parent Technique**: [[Weaken Encryption|T1600 - Weaken Encryption]]

This is a sub-technique of T1600 - Weaken Encryption.

## Summary

Adversaries may reduce the level of effort required to decrypt data transmitted over the network by reducing the cipher strength of encrypted communications.(Citation: Cisco Synful Knock Evolution)

Adversaries can weaken the encryption software on a compromised network device by reducing the key si

## Description

Adversaries may reduce the level of effort required to decrypt data transmitted over the network by reducing the cipher strength of encrypted communications.(Citation: Cisco Synful Knock Evolution)

Adversaries can weaken the encryption software on a compromised network device by reducing the key size used by the software to convert plaintext to ciphertext (e.g., from hundreds or thousands of bytes to just a couple of bytes). As a result, adversaries dramatically reduce the amount of effort needed to decrypt the protected information without the key.

Adversaries may modify the key size used and other encryption parameters using specialized commands in a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) introduced to the system through [Modify System Image](https://attack.mitre.org/techniques/T1601) to change the configuration of the device. (Citation: Cisco Blog Legacy Device Attacks)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
