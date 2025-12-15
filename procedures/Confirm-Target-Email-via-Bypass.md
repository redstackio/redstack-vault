---
id: proc-uuid-5
tags:
  - email-confirmation
  - bypass
  - account-hijack
  - shopify
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.661Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Confirm-Target-Email-via-Bypass

## Summary

This procedure uses the intercepted link to verify the target email on the attacker's account without target involvement.

## Description

Clicking the link completes the bypass, associating the target email with the attacker's store and enabling SSO linkage.

## Requirements

1. Confirmation link from previous email
2. Active browser session

## Defense

Defensive measures and detection strategies:

- Token validation to prevent reuse across emails
- IP checks on confirmation clicks
- Expire tokens quickly

## Objectives

1. Bind target email to account
2. Enable SSO discovery

## Instructions

### Step 1: Click Confirmation Link

**Context**: Activate the verification.

Paste or click the link from the email into the browser.

> Redirects to Shopify confirmation page.

### Step 2: Verify Update

**Context**: Check profile for changes.

Return to profile; email now shows as confirmed target address.

> Success message or updated field confirms.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-confirmation]]
- [[bypass]]
- [[account-hijack]]
- [[shopify]]
