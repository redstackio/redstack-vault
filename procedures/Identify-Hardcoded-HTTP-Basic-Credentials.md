---
id: proc-uuid-002
tags:
  - hardcoded-credentials
  - basic-auth
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:44.662Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Identify-Hardcoded-HTTP-Basic-Credentials

## Summary

This procedure focuses on locating embedded authentication credentials within decompiled Android app code, specifically HTTP basic auth strings that can be decoded and tested for validity.

## Description

Hardcoded credentials in mobile apps represent a common misconfiguration where development secrets are not removed or obfuscated before release. In this scenario, credentials for a Zomato development subdomain were found in plaintext or base64 form during code inspection, associated with a domain initially showing 503 errors. The approach involves string searching and decoding, enabling subsequent exploitation if the creds grant access to sensitive interfaces.

## Requirements

1. Decompiled app source code directory
2. Text editor or IDE for code review (e.g., VS Code)
3. Base64 decoder (built-in to most tools)
4. Knowledge of HTTP basic auth format

## Defense

Defensive measures and detection strategies:

- Implement code scanning in CI/CD to detect hardcoded secrets (e.g., using TruffleHog)
- Use environment-specific builds to exclude dev creds from production APKs
- Encrypt or externalize credentials via backend services

## Objectives

1. Extract potential credential strings from app code
2. Decode and validate their format
3. Prepare for testing on target domains

## Instructions

### Step 1: Search Decompiled Code

**Context**: Locate strings indicative of authentication.

Scan the decompiled directory for HTTP-related terms.

**Command** (grep-search-creds):
```bash
grep -r "Basic\s*auth\|Authorization:\s*Basic" output_dir/
```

> This reveals base64-encoded strings like 'dXNlcm5hbWU6cGFzc3dvcmQ=' which decode to 'username:password'.

### Step 2: Decode Credentials

**Context**: Convert base64 to plaintext for usability. Use online tools or CLI.

**Command** (base64-decode):
```bash
echo 'dXNlcm5hbWU6cGFzc3dvcmQ=' | base64 -d
```

> Expected output: 'username:password'. Note the domain context (e.g., zomato.com subdomain).

### Step 3: Verify Credential Context

**Context**: Confirm association with target domain.

Review surrounding code for URL usage, ensuring creds tie to a 503-responding endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None

## Tags

- [[hardcoded-credentials]]
- [[basic-auth]]
