---
tags:
  - business-logic-flaw
  - api-key
  - steam
  - authenticator
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.939Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 25d5da40-9fb2-4868-aa50-37b015c67b51
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Registration-via-Mobile-Authenticator

## Summary

This procedure confirms the Steam API key registration using the mobile authenticator, completing the issuance of the initial API key after receiving the `request_id`.

## Description

Following initiation, this step involves using the Steam mobile app to approve the pending `request_id`, which authenticates and finalizes the first key. The flaw exploited later relies on this confirmation not invalidating the `request_id`. The target is the Steam ecosystem, requiring app access, and results in a functional API key. Expected outcomes include key visibility in the dashboard.

## Requirements

1. Steam mobile app installed and linked to the account
2. Generated `request_id` from initiation step
3. Physical access to the mobile device

## Defense

Defensive measures and detection strategies:

- Invalidate `request_id` immediately after confirmation
- Require unique `request_id` per registration attempt
- Audit mobile confirmations for suspicious timing or volume

## Objectives

1. Authenticate and issue the initial API key
2. Complete the standard registration flow
3. Enable reuse of `request_id` due to the logic flaw

## Instructions

### Step 1: Open Mobile App

**Context**: Launch the Steam app to check for pending confirmations.

Open the Steam mobile app and navigate to the authenticator section or notifications.

> A prompt for the specific `request_id` should appear if the initiation was recent.

### Step 2: Approve Confirmation

**Context**: Review and confirm the request to issue the key.

Select the confirmation request matching the `request_id` and approve it using your authenticator code or biometrics.

> Upon approval, the first API key is generated; check the web dashboard to verify.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- business-logic-flaw
- api-key
- steam
- authenticator
