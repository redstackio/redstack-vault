---
id: proc-nextcloud-token-access-001
tags:
  - unauthorized-access
  - token-abuse
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:46:20.008Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
---
# Access-Shared-Resources-Using-Extracted-Tokens

## Summary

This procedure uses leaked share tokens from the SQL injection to forge access URLs and retrieve shared files from Nextcloud without authentication.

## Description

After extracting tokens like rkNCkcYcbGEBDQN from ocshares, construct share links in the format https://<server>/index.php/s/<token> to directly access files. This bypasses authorization checks, allowing download of sensitive shared content such as /Nextcloud.mp4.

## Requirements

1. Extracted token and server URL from prior query
2. Network access to the Nextcloud server
3. Browser or curl for URL access

## Defense

Defensive measures and detection strategies:

- Rotate share tokens periodically and monitor usage logs
- Implement token validation with IP/source checks
- Rate-limit share link accesses and require CAPTCHA for suspicious activity

## Objectives

1. Forge valid share URLs using leaked tokens
2. Download or view shared files unauthorized
3. Demonstrate impact of data disclosure

## Instructions

### Step 1: Construct Share URL

**Context**: Build the URL using the token from extraction.

No command; example: https://cloud.local.yourosoft.com/index.php/s/rkNCkcYcbGEBDQN.

> Replace <server> and <token> with actual values.

### Step 2: Access the Resource

**Context**: Open the URL in a browser or use curl to fetch content.

```bash
curl -O https://cloud.local.yourosoft.com/index.php/s/rkNCkcYcbGEBDQN/download
```

> Downloads the shared file without login.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Valid Accounts]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unauthorized-access]]
- [[token-abuse]]
- [[nextcloud]]
