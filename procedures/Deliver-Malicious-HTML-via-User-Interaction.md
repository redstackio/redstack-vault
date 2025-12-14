---
id: proc-uuid-2
tags:
  - csrf
  - social-engineering
  - phishing
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
updated_at: '2025-12-14T17:27:15.735Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-Malicious-HTML-via-User-Interaction

## Summary

This procedure involves tricking an authenticated Factlink user into loading the malicious CSRF HTML page, triggering the unauthorized sign-up request from their browser.

## Description

Delivery relies on social engineering, such as sending the HTML file via email attachment, a direct link to a hosted version, or embedding in a phishing site. The victim's active session cookie makes the request appear legitimate, exploiting the CSRF flaw to submit the form without additional interaction.

## Requirements

1. Method to contact the victim (email, chat, etc.)
2. The crafted HTML file from the previous procedure
3. Victim must be authenticated to Factlink during interaction

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links/files
- Enforce browser security features like popup blockers
- Log and alert on unexpected form submissions from user agents

## Objectives

1. Induce the victim to load the malicious page
2. Ensure the request originates from the victim's session
3. Maintain stealth to avoid detection

## Instructions

### Step 1: Prepare Delivery Mechanism

**Context**: Choose and set up a delivery method, such as hosting the HTML on a controlled server or attaching to an email.

For file delivery: Save the HTML as anyname.html and attach to an email with a lure like "Click to view update.html".

For link delivery: Upload to a web server and send a URL like http://evil.com/anyname.html.

> Ensure the page loads quickly and submits without visible prompts.

### Step 2: Send to Victim and Monitor

**Context**: Dispatch the lure and wait for interaction.

Send the email or message, phish the victim into clicking/opening while they are logged into Factlink.

> Expected output: Victim's browser executes the script, submitting the form invisibly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[Phishing]]
- [[drive-by-compromise]]
