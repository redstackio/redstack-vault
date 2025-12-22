---
tags:
  - csrf-poc
  - exploitation
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
updated_at: '2025-12-14T17:27:15.756Z'
sub_techniques: []
id: 2c12f1d4-5b8a-4aaf-952f-d9e6d96de91d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Deliver-Login-CSRF-PoC

## Summary

This procedure creates and deploys a proof-of-concept HTML page that exploits a CSRF-vulnerable login form by auto-submitting attacker credentials, demonstrating session hijacking via login CSRF.

## Description

Login CSRF tricks users into authenticating to attacker accounts, often linking sessions or aiding phishing. This targets unprotected forms on web apps like IRCCloud. Use a text editor to build the PoC and host it simply (e.g., local server). Prerequisites: Control over a domain or file hosting. Outcomes: Automatic form submission from victim's browser, compromising authentication.

## Requirements

1. Text editor (e.g., VS Code)
2. Web server for hosting PoC (e.g., Python's http.server)
3. Attacker credentials for the target service

## Defense

Defensive measures and detection strategies:

- Add unique CSRF tokens to forms and validate on server
- Double-submit cookies for token verification
- Educate users on phishing and unexpected logins

## Objectives

1. Mimic the vulnerable form in HTML
2. Auto-submit to force login without user input
3. Verify impact on victim session

## Instructions

### Step 1: Create Malicious HTML File

**Context**: Build a form identical to the target's but pre-filled.

Open a text editor and write the HTML with POST to https://www.irccloud.com/, inputs for email/password/org_invite, and JavaScript auto-submit.

### Step 2: Add Auto-Submission Script

**Context**: Ensure immediate execution upon page load.

Include <script>document.getElementById('csrf-form').submit();</script> after the form.

**Command** (Save as poc.html):

No bash command; save file manually.

> File ready for hosting.

### Step 3: Host and Deliver PoC

**Context**: Serve the page and lure victim.

Host locally with `python -m http.server 8000`, access via http://localhost:8000/poc.html. Send link via email/social engineering, timing it when victim is on target site.

**Expected Output**: Browser navigates and submits form silently, logging victim into attacker's account.

> Success if login completes without alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-poc]]
- [[exploitation]]
