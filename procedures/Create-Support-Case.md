---
tags:
  - support
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
techniques: []
updated_at: '2025-12-14T00:11:09.537Z'
sub_techniques: []
id: 6b501d4e-0f31-4d67-bc64-5035fd8dae67
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Create-Support-Case

## Summary

This procedure creates a new support request in the Acronis portal, enabling access to the attachment upload feature vulnerable to self-XSS.

## Description

After authentication, users can navigate to the support section to submit cases. This involves filling a web form with case details. The target is the support requests interface on account.acronis.com. Expected outcome is a new case with an ID, setting up the upload step. No special tools needed beyond a browser.

## Requirements

1. Active session from login
2. Basic case details (e.g., subject, description)
3. Web browser

## Defense

Defensive measures and detection strategies:

- Rate-limit support case submissions to prevent abuse
- Log and review case creation patterns for suspicious activity

## Objectives

1. Generate a support case ID
2. Unlock attachment functionality
3. Position for payload injection

## Instructions

### Step 1: Navigate to Support Section

**Context**: Locate the support requests area in the dashboard.

No command required; from the account dashboard, click on 'Support' or 'Requests'.

> The support page should display options to create a new case.

### Step 2: Submit Case Form

**Context**: Provide minimal details to create the case.

No command required; enter a subject like 'Test Issue' and a description, then submit.

> A confirmation with case ID appears, and the case details page loads with attachment options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- support
- web
