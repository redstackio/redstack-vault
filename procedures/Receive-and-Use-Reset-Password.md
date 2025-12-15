---
tags:
  - email-interception
  - credential-retrieval
type: procedure
tools:
  - '[[tools/tempmail]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.140Z'
sub_techniques: []
id: 664594ee-1ffd-4bff-972a-28a72ce06119
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Receive-and-Use-Reset-Password

## Summary

This procedure involves checking the temporary email for the password reset notification and extracting the new password.

## Description

The reset email arrives at the attacker-controlled temporary address with the generated password. Use tempmail to view inbox. Target: Email service. Outcome: Attacker obtains credentials for login.

## Requirements

1. Temporary email from earlier step
2. Access to tempmail interface
3. Recent reset trigger

## Defense

Defensive measures and detection strategies:

- Avoid emailing passwords; use secure links
- Monitor for use of disposable emails in accounts
- Log reset events

## Objectives

1. Retrieve new password
2. Prepare for account access
3. Complete takeover chain

## Instructions

### Step 1: Check Temporary Inbox

**Context**: Access tempmail to view emails.

Navigate to tempmail service and enter the generated email address.

> Inbox shows reset email from target app.

### Step 2: Extract Password

**Context**: Open and read the email content.

Locate the new password in the email body.

> Password copied, e.g., a random string like 'NewPass123'.

### Step 3: Secure the Credential

**Context**: Note for immediate use.

Store temporarily for login step.

> Credential ready.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/tempmail]]

## Tags

- [[credential-access]]
- [[tools/tempmail]]
