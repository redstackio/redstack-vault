---
id: 20641b7b-da4e-4426-97cf-23cf83330d48
name: Weaken Encryption
type: technique
mitre_id: T1600
mitre_url: null
created_at: '2023-04-06T00:31:25.704696+00:00'
updated_at: '2023-04-06T00:31:27.798758+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Weaken Encryption

**MITRE ID**: T1600

## Description

Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would otherwise protect data communications. (Citation: Cisco Synful Knock Evolution)

Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer keys increase the cost of cryptanalysis, or decryption without the key.

Adversaries can compromise and manipulate devices that perform encryption of network traffic. For example, through behaviors such as [Modify System Image](https://attack.mitre.org/techniques/T1601), [Reduce Key Space](https://attack.mitre.org/techniques/T1600/001), and [Disable Crypto Hardware](https://attack.mitre.org/techniques/T1600/002), an adversary can negatively effect and/or eliminate a device’s ability to securely encrypt network traffic. This poses a greater risk of unauthorized disclosure and may help facilitate data manipulation, Credential Access, or Collection efforts. (Citation: Cisco Blog Legacy Device Attacks)

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
