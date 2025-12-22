---
tags:
  - persist-payload
  - form-submit
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
updated_at: '2025-12-14T03:16:31.089Z'
sub_techniques: []
id: 944056ec-3df8-4812-8e26-33710383cecc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Statement

## Summary

This procedure submits the form to store the malicious Markdown payload in the database, making it available on the public profile for rendering and exploitation.

## Description

Submitting the edited statement persists the unsanitized input server-side. Due to the vulnerability in Markdown processing, the payload survives storage and rendering. This step bridges injection to execution, with the profile becoming a vector for any visitor.

## Requirements

1. Payload entered in edit form
2. Active session
3. No server-side validation blocking save

## Defense

Defensive measures and detection strategies:

- Server-side sanitization before storage
- Content moderation queues for profile updates
- Audit logs for statement changes

## Objectives

1. Persist XSS payload
2. Make it publicly accessible
3. Enable victim interaction

## Instructions

### Step 1: Review Input

**Context**: Double-check payload before submission.

Ensure the statement field contains the malicious Markdown without alterations.

### Step 2: Submit Form

**Context**: Trigger the save action.

Click the 'Save' or 'Update' button to POST the data to the server.

### Step 3: Confirm Save

**Context**: Validate persistence.

Look for success message; refresh the profile to see if the statement updates (without clicking).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[persist-payload]]
- [[web]]
