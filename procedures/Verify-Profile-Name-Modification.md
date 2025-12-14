---
id: proc-uuid-4
tags:
  - verification
  - profile-check
  - post-exploit
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:27:15.243Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Profile-Name-Modification

## Summary

This post-exploitation procedure logs into the victim's Liberapay account to confirm the successful CSRF-induced change to the optional 'Name' field, validating the attack's impact.

## Description

After the victim visits the malicious page, access the account using known credentials (in a test scenario) and inspect the profile edit page. This step confirms the public_name field update, such as to 'YOU HAVE BEEN HACKED', highlighting the defacement potential. It's essential for reporting or chaining further attacks.

## Requirements

1. Victim's login credentials (for verification purposes)
2. Access to the updated account session
3. Web browser to navigate Liberapay

## Defense

Defensive measures and detection strategies:

- Enable email notifications for profile changes
- Audit logs for unauthorized edits tied to IP or user-agent anomalies
- User training to review profile after suspicious link clicks

## Objectives

1. Inspect the profile for evidence of modification
2. Document the injected value for impact assessment
3. Ensure no automatic reversions or detections

## Instructions

### Step 1: Log into Victim Account

**Context**: Authenticate to access profile settings.

Navigate to https://liberapay.com/sign-in and enter the victim's credentials (e.g., username talaohu28 and password).

> Expected output: Successful login redirect to dashboard.

### Step 2: Access Edit Page

**Context**: Navigate to the username edit endpoint to view fields.

Go to https://liberapay.com/talaohu28/edit/username.

> Look for the 'Name (optional)' field; it should now show the attacker-injected value like 'CSRF TOKEN EXPLOIT FOR EDIT NAME'.

### Step 3: Screenshot and Log

**Context**: Capture proof of change for validation.

Take a screenshot of the updated field and note any public display of the name on the profile page.

> Success: Field matches the payload from the malicious form; change persists.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[post-exploit]]
