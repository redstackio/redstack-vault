---
tags:
  - csrf-attack
  - url-crafting
  - web-exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:27:29.848Z'
sub_techniques: []
id: 0bc68021-5daf-4604-8752-88d35c088c68
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Simulate CSRF Attack via Direct URL Access

## Summary

This procedure simulates a CSRF attack by opening the captured remove invitation URL in an authenticated browser tab, demonstrating unauthorized removal without user intent.

## Description

Using the URL extracted from Burp (e.g., https://infogram.com/api/team/cancel-invitation/c535cc62-9586-4f4b-8306-9381dcdbc815?teamId=16537204&_=1508852073697), direct access in an admin session executes the removal via session cookies alone. In a real attack, this URL would be embedded in a malicious site or email to trick the admin, disrupting team access.

## Requirements

1. Captured URL from Burp Repeater
2. Authenticated browser session
3. Target invitation still pending

## Defense

Defensive measures and detection strategies:

- Enforce POST for state-changing actions
- Implement SameSite cookies
- Educate users on phishing via URLs

## Objectives

1. Execute removal via crafted URL
2. Verify vulnerability impact
3. Highlight social engineering potential

## Instructions

### Step 1: Copy URL from Repeater

**Context**: Extract the full request URL.

In Burp Repeater, copy the raw URL including parameters.

> Ensure timestamp or ID is preserved for validity.

### Step 2: Open in Authenticated Tab

**Context**: Trigger the action using existing session.

Paste the URL into a new tab in the logged-in browser.

> The request executes, removing the invitation silently.

### Step 3: Verify Removal

**Context**: Check team list for changes.

Refresh the team management page.

> Confirm the invitation is no longer pending.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf-attack
- url-crafting
- web-exploitation
