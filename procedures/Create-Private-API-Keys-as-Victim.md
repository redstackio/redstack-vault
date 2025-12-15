---
tags:
  - api-key-creation
  - credential-setup
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-create-api-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:25:23.052Z'
sub_techniques: []
id: 78963026-001a-40cc-b624-3bb7c98f919f
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Create-Private-API-Keys-as-Victim

## Summary

Generate private API keys in the organization as the victim to provide targets for IDOR exploitation.

## Description

Log in as victim and use the API keys interface to create keys, saving the request details for later replay with attacker cookies. This simulates legitimate key management before demonstrating bypass.

## Requirements

1. Victim session active
2. ORG-UUID available
3. Browser dev tools for request capture

## Defense

Defensive measures and detection strategies:

- Enforce key rotation policies
- Log all key creations with user attribution
- Restrict key scopes to least privilege

## Objectives

1. Create multiple private keys
2. Capture creation request
3. Note API-UUIDs for targeting

## Instructions

### Step 1: Navigate to API Keys

**Context**: Access management interface.

Log in as victim, go to https://target-platform.com/organization/ORG-UUID/apiKeys.

> Expected: Empty or existing keys list.

### Step 2: Add Keys

**Context**: Submit creation forms.

Fill in key details (name, scopes), submit, and use dev tools to save the POST request as 'Create_Req'.

Execute equivalent with [[commands/curl-create-api-key]] for testing:

```bash
curl -X POST https://target-platform.com/organization/ORG-UUID/apiKeys -H "Cookie: victim_session" -d '{"name":"Test Key","scopes":["read"] }'
```

> Expected: Keys listed with UUIDs.

### Step 3: Verify Creation

**Context**: Confirm visibility.

Refresh the page to see new keys.

> Expected: Private keys marked as organization-owned.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/curl-create-api-key]]

## Tools Used


## Tags

- api-key-creation
- credential-setup
