---
tags:
  - shopify
  - authorization-bypass
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
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.268Z'
sub_techniques: []
id: 5bf8c069-0068-4c6d-88f6-19385b886100
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Trigger Automatic Account Conversion with Second Partner Account

## Summary

This procedure uses the second partner account to exploit the shared email, forcing the system to automatically convert the pending collaborator request to active without approval.

## Description

The vulnerability lies in the conversion logic that assumes an 'existing user account' for the same email and activates pending requests without verifying account type (partner vs. normal user). Logging into the second account triggers this flaw.

## Requirements

1. Pending request from first account
2. Second partner account with same email
3. No merchant intervention

## Defense

Defensive measures and detection strategies:

- Validate account types during conversion
- Require explicit merchant approval for all activations
- Log and audit shared email conversions

## Objectives

1. Activate pending request illicitly
2. Gain collaborator status
3. Bypass authorization checks

## Instructions

### Step 1: Log In to Second Account

**Context**: Switch to the second account to invoke detection.

Log out of the first account and log in to the second at partners.shopify.com.

> Expected output: Dashboard loads; system detects shared email and pending request.

### Step 2: Observe Conversion

**Context**: The system auto-applies conversion logic.

Navigate to the stores section; the pending request should auto-activate due to the flaw.

> Expected output: Status changes to 'Active Collaborator' without prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[authorization-bypass]]
