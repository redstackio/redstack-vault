---
tags:
  - html-injection
  - external-login
  - oauth-bypass
type: procedure
tools:
  - '[[tools/Browser-Developer-Console]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:45.003Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: abe6f2a9-21db-4c54-ae51-0872776f8b9a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-HTML-for-External-Login-Linking

## Summary

This procedure uses browser developer tools to inject custom HTML into the Shopify account profile, creating a link to connect an external login provider like Google without proper verification checks.

## Description

Shopify's external login section at accounts.shopify.com lacks client-side protections against HTML injection via console, allowing attackers to forge a POST request to the /external-login endpoint. This bypasses UI restrictions for unverified accounts under 24 hours old. The attack scenario targets the profile page, leading to OAuth redirection. Prerequisites include an unverified account ID.

## Requirements

1. Access to the unverified account profile
2. Browser with developer console (e.g., Chrome DevTools)
3. Account ID from creation step

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for external login requests, rejecting unverified accounts
- Disable or restrict console access to sensitive endpoints via CSP headers
- Log and monitor anomalous POST requests to external-login paths

## Objectives

1. Forge external login connection without email verification
2. Initiate OAuth flow to Google
3. Link external credentials to the backdoor account

## Instructions

### Step 1: Access Profile Page

**Context**: Navigate to the account profile to prepare for injection.

No command; go to https://accounts.shopify.com/accounts/{account_id}, replacing {account_id} with the actual ID.

> Expected: Profile loads with external login section visible but restricted for unverified accounts.

### Step 2: Inject HTML Link

**Context**: Use developer console to add a clickable link for Google connection.

Open console (F12) and execute:

```javascript
document.body.innerHTML += '<a href="/accounts/{victim_account_id}/external-login/1" data-method="post">Connect to Google</a>';
```

Replace {victim_account_id} with the actual ID.

> This appends the link; clicking simulates the POST without UI.

### Step 3: Trigger the Link

**Context**: Initiate the external login flow.

Click the injected "Connect to Google" link.

> Expected: POST to /accounts/{victim_account_id}/external-login/1, redirect to Google OAuth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Console]]

## Tags

- [[html-injection]]
- [[external-login]]
- [[oauth-bypass]]
