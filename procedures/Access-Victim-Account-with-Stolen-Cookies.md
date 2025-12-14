---
tags:
  - account-takeover
  - session-hijacking
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-access-victim-document]]'
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ae4e2af7-c1bd-496b-85d2-580c37c6e511
created_at: '2025-12-14T00:11:16.492Z'
updated_at: '2025-12-14T00:11:16.492Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Access Victim Account with Stolen Cookies

## Summary

This procedure uses stolen grauth and csrf-token cookies to access the victim's Grammarly account and documents from any IP, demonstrating full takeover.

## Description

With the stolen cookies, requests to app.grammarly.com endpoints authenticate as the victim, allowing document access without IP restrictions.

## Requirements

1. Valid stolen grauth and csrf-token values
2. curl or similar HTTP client
3. Knowledge of victim document IDs

## Defense

Defensive measures and detection strategies:

- Enforce IP-based session restrictions
- Monitor for logins from unusual IPs
- Use short-lived session tokens

## Objectives

1. Authenticate with stolen cookies
2. Access private documents
3. Verify takeover impact

## Instructions

### Step 1: Send Authenticated Request

**Context**: Use curl to access a document endpoint with cookies.

Execute [[commands/curl-access-victim-document]]:

```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_GRAUTH_VALUE" --cookie "csrf-token=STOLEN_CSRF_VALUE" -I
```

> Expect HTTP 200 for valid access, 301 for invalid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used

- [[commands/curl-access-victim-document]]

## Tools Used

- [[tools/curl]]

## Tags

- [[account-takeover]]
- [[session-hijacking]]
