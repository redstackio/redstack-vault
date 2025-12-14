---
tags:
  - email-injection
  - account-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:24.453Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ad128437-a45c-41e7-b9ec-b80de61cfb42
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Set Email on Target Account

## Summary

This procedure leverages the manipulated fanclub subscription to inject the attacker's email onto a target account that lacks one, exploiting the billing update logic without proper validation.

## Description

Upon completing the subscription purchase with tampered parameters, the system updates the target account's profile with the provided email if none exists. This occurs because the subscription handler assumes the email belongs to the target and applies it during profile synchronization. The attack requires a real purchase, making it costly but effective for accounts without emails. Outcomes include the attacker receiving all future communications for the target.

## Requirements

1. Successful parameter manipulation from prior step
2. Valid payment method for subscription fee
3. Attacker's email address ready for injection
4. Proxy for request handling

## Defense

Defensive measures and detection strategies:

- Require email verification before allowing subscription updates
- Prevent email changes via billing flows without explicit user consent
- Audit logs for email updates tied to subscriptions and flag cross-user changes
- Enforce two-factor authentication on account modifications

## Objectives

1. Associate attacker's email with target account
2. Enable password reset access without prior email
3. Maintain stealth by using legitimate billing process

## Instructions

### Step 1: Include Email in Subscription Payload

**Context**: Ensure the tampered request includes the email parameter, which the server will apply to the target.

Edit the request in Burp Suite to add or modify the email field:

```http
{"username": "target_username", "email": "attacker@example.com", "payment_method": "card"}
```

> The server processes this during purchase confirmation. Expected: Update succeeds silently if no email exists.

### Step 2: Complete Purchase and Confirm

**Context**: Finalize the transaction to trigger the email update.

Submit payment details and forward the request. Check account status post-purchase.

> Success: No update errors; test by attempting password reset with the email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used

- [[Burp Suite]]

## Tags

- [[email-injection]]
- [[account-modification]]
