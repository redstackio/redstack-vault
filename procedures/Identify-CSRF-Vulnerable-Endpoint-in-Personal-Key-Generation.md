---
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:16.045Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f6144a45-c1bf-4194-a2c3-50ba726e4a9e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CSRF-Vulnerable-Endpoint-in-Personal-Key-Generation

## Summary

This procedure involves reconnaissance to identify the personal key generation endpoint on staging.login.gov that lacks CSRF protection, enabling subsequent exploitation to force unauthorized key regeneration.

## Description

In a web application like staging.login.gov, the personal key management feature at https://staging.login.gov/manage/personal_key uses a form submission with the 'resend=true' parameter to generate a new key. By inspecting the endpoint, an attacker discovers no CSRF token validation, allowing cross-origin form submissions. This step is crucial for confirming the vulnerability before crafting an exploit, targeting authenticated users to invalidate their current personal key, which is critical for account recovery.

## Requirements

1. Access to a browser developer tools for inspecting forms
2. Knowledge of the target application (staging.login.gov)
3. Ability to test form submissions from external sites (e.g., local HTML file)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing forms
- Use Content Security Policy (CSP) to restrict cross-origin submissions
- Monitor for anomalous form submissions from unexpected referers

## Objectives

1. Confirm the endpoint's lack of CSRF protection
2. Document the exact parameters needed for exploitation ('resend=true')
3. Assess potential impact on user account access

## Instructions

### Step 1: Inspect the Target Form

**Context**: Navigate to the personal key management page while authenticated and examine the HTML form structure.

Open https://staging.login.gov/manage/personal_key in a browser, right-click the form, and select 'Inspect Element'. Look for input fields and the form's action attribute.

**Expected Output**: Form action points to https://staging.login.gov/manage/personal_key with method POST and hidden input for 'resend' value 'true'.

### Step 2: Test for CSRF Protection

**Context**: Create a simple test HTML page to submit the form cross-origin and verify if it processes without a token.

Craft a basic HTML file with a form mimicking the target:

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://staging.login.gov/manage/personal_key" method="POST">
  <input type="hidden" name="resend" value="true">
  <input type="submit" value="Submit">
</form>
<script>document.forms[0].submit();</script>
</body>
</html>
```

Load this file in a browser while authenticated to the target site.

**Expected Output**: The server processes the request, generating a new key and redirecting to the success page.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
