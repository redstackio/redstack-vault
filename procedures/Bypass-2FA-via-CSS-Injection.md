---
id: proc-css-injection-2fa-bypass
tags:
  - css-injection
  - 2fa-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/css-injection-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:58.093Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-2FA-via-CSS-Injection

## Summary

Inject CSS to manipulate the 2FA interface, hiding inputs or auto-submitting to bypass verification in the BountyPay system.

## Description

Unsanitized style inputs allow CSS injection, altering DOM to skip 2FA. In the CTF, this finalizes takeover after prior steps.

## Requirements

1. Vulnerable input field for styles
2. Browser dev tools or proxy
3. Prior access to injection point

## Defense

Defensive measures and detection strategies:

- Sanitize CSS inputs
- Use CSP to block inline styles
- Validate UI interactions server-side

## Objectives

1. Inject CSS payload
2. Bypass 2FA UI
3. Achieve full access

## Instructions

### Step 1: Identify Injection Point

**Context**: Find unsanitized style param.

**Command** ([[commands/css-injection-test]]):
```bash
curl 'https://bountypay.h1ctf.com/2fa?style=<style>body{display:none}</style>'
```

> Page renders hidden if vulnerable.

### Step 2: Craft Bypass Payload

**Context**: Hide 2FA and submit.

**Command** ([[commands/css-injection-test]]):
```javascript
// In console: document.querySelector('#2fa-form').style.display = 'none'; document.querySelector('form').submit();
```

> Bypasses to success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript (UI manipulation via CSS)

### Sub-Techniques

- None

## Commands Used

- [[commands/css-injection-test]]

## Tools Used

- None specific

## Tags

- [[css-injection]]
- [[2fa-bypass]]
