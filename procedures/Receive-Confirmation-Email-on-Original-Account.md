---
id: proc-uuid-4
tags:
  - email-intercept
  - confirmation-bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Email
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:58.664Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Receive-Confirmation-Email-on-Original-Account

## Summary

This procedure waits for and retrieves the confirmation email sent erroneously to the original signup email.

## Description

Due to the root cause logic error, Shopify sends the new email's confirmation to the stored original address. This allows the attacker to intercept it.

## Requirements

1. Access to original attacker email inbox
2. Recent email change performed

## Defense

Defensive measures and detection strategies:

- Audit email sending logs for mismatches
- Implement double-confirmation for email changes
- Alert on confirmation sends to non-target addresses

## Objectives

1. Receive the misdirected email
2. Extract confirmation link

## Instructions

### Step 1: Monitor Inbox

**Context**: Wait for automated email delivery.

Refresh the attacker email inbox (e.g., Gmail).

> Email from mailer@shopify.com arrives shortly.

### Step 2: Identify Confirmation Link

**Context**: Locate the verification URL.

Open the email titled something like 'Confirm your email address'.

> Copy the link: https://myshop.myshopify.com/account/confirm?token=...

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-intercept]]
- [[confirmation-bypass]]
- [[shopify]]
