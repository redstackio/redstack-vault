---
tags:
  - xss
  - cookie-theft
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9888e0f2-a007-4bfd-a176-d4cac126974a
created_at: '2025-12-13T23:52:49.646Z'
updated_at: '2025-12-13T23:52:49.646Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Exfiltrate-Cookies-via-Advanced-XSS-Payload

## Summary

This procedure extends the basic XSS to steal session cookies by modifying the payload to alert(document.cookie), demonstrating data exfiltration in the admin context.

## Description

Building on the initial payload, this crafts a chained URL that embeds the cookie-accessing JS, allowing attackers to capture admin session tokens for hijacking. It highlights the vulnerability's potential for unauthorized access.

## Requirements

1. Basic XSS confirmed from prior procedures
2. Attacker-controlled endpoint for exfiltration (optional for alert demo)
3. Active admin session for cookie access

## Defense

Defensive measures and detection strategies:

- Set HttpOnly flags on sensitive cookies to block JS access
- Implement referrer checks and CORS policies
- Detect anomalous cookie access patterns in logs

## Objectives

1. Extract session cookies via JS
2. Enable session hijacking
3. Demonstrate full impact of the vuln

## Instructions

### Step 1: Modify Payload

**Context**: Update the return_url to include cookie access.

Craft new URL:

```url
https://<Any>.myshopify.com/admin/authenticate/?return_url=https://<Any>.myshopify.com/admin/authenticate/?return_url=javascript:alert(document.cookie)
```

> This chains the URL to embed the advanced payload.

### Step 2: Navigate and Reload

**Context**: Repeat trigger process with new URL.

Navigate to the URL and reload the page.

> Payload executes, alerting cookie string.

### Step 3: Capture Output

**Context**: Record the exfiltrated data.

Copy the alert contents showing cookies like _shopify_sa, admin session IDs.

> Cookies reveal session details for further exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[cookie-theft]]
- [[exfil]]
