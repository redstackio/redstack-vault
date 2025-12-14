---
id: uuid-1
tags:
  - reverse-engineering
  - credential-leak
  - mobile-app
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:33:34.362Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Twitter-Credentials-from-Periscope-App

## Summary

This procedure involves reverse engineering the Periscope mobile app to extract embedded Twitter OAuth consumer key and secret, enabling unauthorized use of the app's API credentials for malicious OAuth flows.

## Description

The Periscope app hardcodes Twitter's consumer key and secret for its 'Login with Twitter' feature, obfuscated in the binary. By decompiling the app, attackers can recover these to impersonate the app in OAuth requests. This targets Android/iOS apps and requires static analysis tools. Prerequisites include obtaining the app APK/IPA file. Expected outcome: Usable credentials for Twitter API calls, bypassing normal app registration.

## Requirements

1. Periscope app binary (APK for Android or IPA for iOS).
2. Reverse engineering environment (e.g., Linux/Mac with Java).
3. Knowledge of app deobfuscation techniques.

## Defense

Defensive measures and detection strategies:

- Avoid hardcoding secrets in mobile apps; use secure storage or runtime fetching.
- Obfuscate credentials more robustly and monitor for leaked keys via API rate limits.
- App integrity checks to detect tampering.

## Objectives

1. Recover Twitter consumer key and secret.
2. Validate credentials via test API call.
3. Enable subsequent OAuth token generation.

## Instructions

### Step 1: Obtain and Unpack App Binary

**Context**: Acquire the Periscope app and unpack it for analysis to access obfuscated strings.

Download the Periscope APK from a trusted source or device. Use APKTool to unpack:

(Descriptive: Run `apktool d periscope.apk` to decode resources and manifest.)

> This extracts smali code and assets; search for Twitter-related strings like 'api.twitter.com'.

### Step 2: Decompile and Search for Credentials

**Context**: Decompile the app to Java/Kotlin source and locate OAuth parameters.

Use Jadx GUI or CLI to decompile the DEX files: `jadx periscope.apk`. Search for classes handling Twitter login, looking for base64-encoded or hex strings matching consumer key/secret formats.

> Expected: Key like 'xvz1evFS4wEEPTGEFPHBog' and secret; deobfuscate if needed by reversing simple XOR or string concatenation.

### Step 3: Validate Extracted Credentials

**Context**: Test the credentials against Twitter API to confirm usability.

Construct a basic OAuth signature for `/oauth/request_token` and send via curl or Postman.

> Success: 200 OK with temporary credentials; failure indicates incorrect extraction.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[reverse-engineering]]
- [[credential-leak]]
