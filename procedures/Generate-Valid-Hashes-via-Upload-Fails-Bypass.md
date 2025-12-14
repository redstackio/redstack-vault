---
id: proc-vk-hash-gen-001
tags:
  - bypass
  - sanitization
  - hash-gen
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-13T23:52:34.002Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Generate-Valid-Hashes-via-Upload-Fails-Bypass

## Summary

This procedure bypasses input sanitization in VK.com's upload_fails.php to generate valid hashes for the proxy_img endpoint, enabling authenticated requests with role=share.

## Description

By adding dots to parameter names (e.g., hash.hash), evade sanitization filters in upload_fails.php, allowing hash generation for proxy_img act, which is integral to serving the malicious image response.

## Requirements

1. Authenticated VK session
2. Access to upload_fails.php
3. Parameter manipulation knowledge

## Defense

Defensive measures and detection strategies:

- Robust parameter sanitization without dot evasion
- Rate-limit hash generation requests

## Objectives

1. Bypass sanitization with dotted params
2. Obtain valid proxy hashes
3. Enable authenticated proxy use

## Instructions

### Step 1: Prepare Parameters

**Context**: Modify params to evade filters.

Set role=share&hash.hash=...&other.params with dots.

> Expected output: Parameters accepted without stripping.

### Step 2: Request Hashes

**Context**: Submit to upload_fails.php.

POST to upload_fails.php with bypassed params.

> Expected output: Response containing valid hash like 8dfd93e60c78ddb4a9cf914c27f7642c.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1078.004]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- bypass
- sanitization
- hash-gen
