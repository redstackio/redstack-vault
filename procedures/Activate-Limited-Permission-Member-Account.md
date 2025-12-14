---
tags:
  - activation
  - session
  - shopify
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
updated_at: '2025-12-14T17:29:44.873Z'
sub_techniques: []
id: dbdc25b8-aff7-41b8-bb81-3acfd28d1136
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Activate-Limited-Permission-Member-Account

## Summary

This procedure activates and logs in the invited member with limited 'Manage apps' permissions in a separate session for exploitation.

## Description

To isolate the low-privilege context, activation occurs in an incognito or new browser tab, ensuring no admin session interference. This sets up the unauthorized access vector.

## Requirements

1. Invitation email received
2. Separate browser session
3. Valid credentials

## Defense

Defensive measures and detection strategies:

- Session isolation and multi-factor auth
- Monitor cross-session access

## Objectives

1. Establish limited user session
2. Verify permission restrictions
3. Prepare for IDOR testing

## Instructions

### Step 1: Accept Invitation

**Context**: Start the member onboarding.

Open the invitation email and click the activation link.

> Redirect to login/activation page.

### Step 2: Log In

**Context**: Access dashboard as limited user.

Enter credentials and log in in incognito mode.

> Restricted dashboard loads without full features.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[activation]]
- [[session]]
- [[shopify]]
