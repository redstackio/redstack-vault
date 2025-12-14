---
id: proc-496326-step3
tags:
  - cookie-forgery
  - crypto
  - web
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:10.896Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Craft-Forged-Download-Cookie

## Summary

This procedure generates a forged 'pickup' cookie by encoding the file ID and password into a predictable format using base64 and SHA512 hashes, enabling auth bypass.

## Description

The cookie lacks server-side secrets, using: base64(file ID) + '-' + base64(SHA512(base64(file ID))) + '-' + base64(secret key) + '-' + base64(SHA512(base64(secret key))). This predictability allows forgery with just the ID and password. Use hashing tools like openssl; outcomes include a valid-looking cookie for download requests.

## Requirements

1. File ID (e.g., 15849581) and secret key/password
2. Access to base64 and SHA512 tools (e.g., openssl, Python)
3. Knowledge of cookie format from analysis

## Defense

Defensive measures and detection strategies:

- Incorporate server-side signing keys in cookies
- Validate cookie integrity with HMAC
- Monitor for anomalous cookie patterns

## Objectives

1. Create forgeable auth token
2. Mimic legitimate cookie structure
3. Prepare for unauthorized download

## Instructions

### Step 1: Compute Cookie Components

**Context**: Encode and hash elements to build the cookie string.

Example using openssl (adapt for actual secret):

```bash
echo -n "15849581" | base64 | tr -d '\n'  # MTU4NDk1ODE=
sha512sum <(echo -n "MTU4NDk1ODE=") | cut -d' ' -f1 | xxd -r -p | base64  # Hash part
# Repeat for secret key and its hash
# Assemble: pickup=Subject=&PackageID=MTU4NDk1ODE=-<hash1>-<b64secret>-<hash2>
```

> Output: Forged cookie like pickup=Subject=&PackageID=MTU4NDk1ODE=████

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cookie-forgery]]
- [[crypto]]
- [[web]]
