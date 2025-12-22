---
tags:
  - mobile-reverse-engineering
  - hardcoded-credentials
  - oauth
type: procedure
tools:
  - '[[tools/Jadx]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/jadx-decompile-apk]]'
verified: false
platforms:
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:32:10.236Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0c11ba7c-a019-4d03-9c0d-5d14f47d7d09
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Decompile-Mobile-App-to-Extract-Hardcoded-OAuth-Keys

## Summary

This procedure involves reverse engineering Instacart's Android or iOS mobile app binaries to extract hardcoded OAuth keys, including the private key, which are embedded directly in the decompilable code. It enables attackers to obtain sensitive credentials without any authentication, leading to potential API abuse.

## Description

The Instacart mobile apps contain hardcoded OAuth public and private keys in their binaries, lacking obfuscation or secure storage. By decompiling the app using tools like Jadx for Android, attackers can search the source code for these keys. This vulnerability allows anyone with the app binary to extract the keys and use them for unauthorized access. The process targets client-side applications where such secrets are insecurely stored, common in mobile reverse engineering scenarios. Expected outcomes include obtaining functional keys that bypass normal authentication flows.

## Requirements

1. Downloaded Instacart APK (Android) or IPA (iOS) file from app stores or official sources.
2. Installed reverse engineering tools like Jadx on a Linux/macOS environment.
3. Basic knowledge of searching decompiled Java/Swift code for strings like "oauth_private_key" or base64 patterns.
4. Text editor or grep for scanning output files.

## Defense

Defensive measures and detection strategies:

- Avoid hardcoding secrets in mobile apps; use secure storage like Android Keystore or iOS Keychain.
- Obfuscate code and use runtime key generation or server-side validation.
- Monitor API access logs for anomalous patterns from leaked keys.
- Implement certificate pinning and rate limiting on API endpoints.

## Objectives

1. Extract hardcoded OAuth private key from app binary.
2. Validate key usability for API authentication.
3. Demonstrate information disclosure risks in mobile applications.

## Instructions

### Step 1: Obtain and Prepare App Binary

**Context**: Download the Instacart app binary to set up for decompilation. This step ensures you have the target file ready for reverse engineering.

**Command** ([[commands/jadx-decompile-apk]]):
```bash
jadx -d instacart_decompiled instacart.apk
```

> This command decompiles the APK into readable Java source code in the 'instacart_decompiled' directory. For iOS, use equivalent tools like 'otool' or Hopper to disassemble the IPA.

### Step 2: Search for Hardcoded Keys

**Context**: Scan the decompiled code for embedded OAuth keys, focusing on configuration classes or constants.

**Command** (grep search):
```bash
grep -r "oauth\|private_key\|bearer" instacart_decompiled/
```

> Expected output includes lines with hardcoded strings, such as base64-encoded private keys. Copy the key for use in subsequent steps. Validate by checking if it's a functional RSA private key format.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Credentials In Files]] Credentials in Files

### Sub-Techniques

- N/A

## Commands Used

- [[commands/jadx-decompile-apk]]
- grep for string search

## Tools Used

- [[tools/Jadx]]

## Tags

- mobile-reverse-engineering
- hardcoded-credentials
- oauth
- information-disclosure
