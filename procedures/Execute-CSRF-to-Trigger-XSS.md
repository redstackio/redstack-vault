---
id: proc-uuid-5
tags:
  - csrf-execution
  - xss-trigger
  - session-hijack
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.613Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Execute-CSRF-to-Trigger-XSS

## Summary

This procedure deploys the CSRF PoC to force a victim to authenticate as the attacker, leading to execution of the stored XSS payload in their browser.

## Description

By tricking the victim into loading the malicious HTML (e.g., via phishing), the form submits, logs them in as the attacker, and upon viewing the profile (now with attacker's username), the XSS executes, stealing session data.

## Requirements

1. Generated CSRF PoC HTML file
2. Victim browser access (e.g., via link)
3. Stored XSS payload in attacker's profile

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Implement SameSite cookies to mitigate CSRF
- Scan for and block XSS payloads in user inputs

## Objectives

1. Force victim login as attacker
2. Trigger stored XSS execution
3. Steal victim cookies or perform actions

## Instructions

### Step 1: Save PoC HTML

**Context**: Prepare the file for delivery.

Paste the generated HTML into a text editor, save as `csrf-poc.html`.

> Expected: Valid HTML file ready for hosting or direct opening.

### Step 2: Load in Victim Browser

**Context**: Simulate victim interaction.

Open the file in a browser (or host and link to it) to trigger the form submission.

> Expected: Automatic login as attacker, session established.

### Step 3: View Profile to Execute XSS

**Context**: Trigger the payload.

Navigate to the profile page in the now-authenticated session.

> Expected: Alert dialog with `document.cookie` contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[xss]]
