---
tags:
  - account-takeover
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/hmac-generation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:44.164Z'
sub_techniques: []
id: aa79de41-cd07-475a-b2e2-77bc795150e9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Account-Takeover-with-Stolen-Token

## Summary

Use the stolen API token to generate HMAC-signed requests, impersonating the victim for full shop access and actions.

## Description

The token serves as the HMAC key; no further checks allow authenticated API calls, enabling data access, modifications, and chat impersonation.

## Requirements

1. Stolen API private token
2. Victim's shop domain
3. API endpoints knowledge

## Defense

- Implement multi-factor for token usage
- Audit API logs for anomalous HMAC uses
- Limit token scopes

## Objectives

1. Authenticate as victim
2. Access private resources
3. Perform destructive actions

## Instructions

### Step 1: Generate Victim HMAC

**Context**: Use token for new domain.

**Command** ([[commands/hmac-generation]]):
```php
$hmac = hash_hmac('sha256', "no_iframe=1&platform=woocommerce&shop_domain=victim-domain.com", $stolen_token, false);
```

> Creates access URL for victim shop.

### Step 2: Execute Actions

**Context**: Call APIs with HMAC.

> Expected: Full admin access without password.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/hmac-generation]]

## Tools Used


## Tags

- [[account-takeover]]
- [[auth-bypass]]
