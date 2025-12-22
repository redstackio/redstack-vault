---
id: 123e4567-e89b-12d3-a456-426614174003
name: Revoke-Application-Access
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.911Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - oauth2
  - revocation
commands:
  - '[[commands/verify-access-token]]'
platforms:
  - Web
tools:
  - '[[tools/me-sh]]'
skill_level: basic
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Revoke-Application-Access

## Summary

This procedure revokes access for a connected OAuth2 app in Vimeo's user settings, invalidating existing access tokens but leaving authorization codes usable due to the vulnerability.

## Description

Users navigate to account settings to disconnect apps, which triggers token revocation. However, in Vimeo's flawed implementation, this does not invalidate prior codes, enabling bypass. This step confirms token invalidation via API failure.

## Requirements

1. Logged-in Vimeo account with connected app (e.g., 'Dor1s Test1')
2. Access to browser for settings navigation

## Defense

Defensive measures and detection strategies:

- Ensure revocation cascades to invalidate all related codes and tokens
- Audit logs for revocation events and subsequent access attempts
- User notifications on revocation to monitor for unauthorized re-access

## Objectives

1. Disconnect the app to simulate user intent to revoke permissions
2. Verify that existing tokens are invalidated
3. Highlight the gap where codes remain valid

## Instructions

### Step 1: Navigate to Settings

**Context**: Access the apps management page in Vimeo settings.

No command; use browser:

```bash
# Direct URL for reference
https://vimeo.com/settings/apps
```

> Log in if needed and locate the connected apps section.

### Step 2: Disconnect App and Verify

**Context**: Revoke the specific app and test the prior token.

**Command** ([[commands/verify-access-token]]):

```bash
./me.sh d3ac3bb53d1c4ebc3de7d28e4ed801c0
```

> After disconnection, this returns 401 Unauthorized with 'invalid_token' error.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/verify-access-token]]

## Tools Used

- [[tools/me-sh]]

## Tags

- [[oauth2]]
- [[revocation]]
