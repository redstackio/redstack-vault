---
id: proc-ato-access
tags:
  - account-takeover
  - unauthorized-access
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.555Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Achieve-Account-Takeover-and-Access-Features

## Summary

Following OTP bypass, this procedure grants the attacker full control over the victim's account on shop.mtn.ng, allowing viewing and modification of personal information, settings, and execution of unauthorized transactions.

## Description

With the MSISDN linked via manipulated response, the platform treats the attacker as authenticated for that number. This enables ATO, exposing PII (names, emails, phones) and allowing actions like purchases or settings changes, escalating to connected services.

## Requirements

1. Successful OTP bypass from prior step
2. Active session on shop.mtn.ng
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Implement multi-factor checks beyond OTP for sensitive actions
- Audit logs for MSISDN linking events and flag anomalies
- Session binding to verified devices/IPs

## Objectives

1. Gain persistent access to victim account
2. Modify settings and view PII
3. Perform unauthorized transactions

## Instructions

### Step 1: Verify Linkage

**Context**: Confirm MSISDN is active in profile.

Navigate to 'Manage Account'; check mobile number field.

> Expected: Victim's MSISDN displayed as verified.

### Step 2: Access Personal Data

**Context**: View and edit victim info.

In 'Edit Profile', review names, email; make changes if desired.

> Expected: Full PII access without prompts.

### Step 3: Initiate Transactions

**Context**: Test ATO with actions.

Proceed to purchase or balance check using account features.

> Expected: Transactions execute as victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-takeover
- unauthorized-access
