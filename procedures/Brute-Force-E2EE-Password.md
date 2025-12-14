---
id: proc-brute-force-e2ee
tags:
  - brute-force
  - password-cracking
  - insufficient-entropy
  - e2ee
type: procedure
tools:
  - '[[tools/Hashcat]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/hashcat-brute]]'
verified: false
platforms:
  - Linux
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:24:42.731Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-E2EE-Password

## Summary

This procedure exploits the bias in Rocket.Chat Mobile app's initial E2EE password generation (prior to v4.5.1) to perform an optimized brute-force attack, recovering the password in a practical timescale and decrypting communications.

## Description

The vulnerability stems from biased random value generation in the password creation process, reducing effective entropy (e.g., from expected 128+ bits to much lower due to predictable patterns or non-uniform distribution). Attackers, having extracted encrypted data, can craft a reduced search space (e.g., custom masks or wordlists accounting for bias) and use GPU-accelerated tools to crack the password. Success compromises all E2EE chats tied to that initial password, exposing sensitive messages.

## Requirements

1. Extracted encrypted data and known password format (e.g., length, charset from app reverse engineering)
2. GPU-enabled system for efficient cracking
3. Understanding of the bias (e.g., via app decompilation to identify RNG flaws)

## Defense

Defensive measures and detection strategies:

- Upgrade to Rocket.Chat v4.5.1+ with fixed entropy generation
- Implement password strength checks and user-prompted strong passwords
- Monitor for offline cracking attempts via anomaly detection in compute usage

## Objectives

1. Identify and exploit generation bias to minimize brute-force complexity
2. Recover the initial E2EE password
3. Decrypt and access protected communications

## Instructions

### Step 1: Analyze Password Bias

**Context**: Reverse engineer the app to understand the bias, reducing the attack surface.

Decompile the APK using apktool:

```bash
apktool d rocket-chat.apk
# Inspect java/smali for password gen logic, e.g., Random.nextInt() bias
```

> Expected output: Source revealing biased RNG (e.g., seeded predictably), informing custom mask like ?l?l?l?l?d?d for 6 chars with letter bias.

### Step 2: Prepare Cracking Environment

**Context**: Set up tools with extracted hash (password-derived key).

Assume password is hashed (e.g., PBKDF2); extract hash from data and prepare rules.

Install Hashcat and create a mask based on bias analysis.

### Step 3: Execute Brute Force

**Context**: Run optimized brute force against the encryption key.

**Command** ([[commands/hashcat-brute]]):

```bash
hashcat -m 1000 -a 3 extracted_hash.txt ?l?l?l?l?d?d --increment --increment-min=4 --increment-max=8
```

> This uses mask attack (?l=lowercase, ?d=digit) tailored to bias; expected output: Cracked password displayed, e.g., "pass1234", verifiable by decrypting a sample message.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques

- [[Password Guessing]]

## Commands Used

- [[commands/hashcat-brute]]

## Tools Used

- [[tools/Hashcat]]

## Tags

- [[brute-force]]
- [[password-cracking]]
- [[insufficient-entropy]]
- [[e2ee]]
