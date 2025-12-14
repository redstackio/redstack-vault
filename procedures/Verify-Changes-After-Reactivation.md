---
tags:
  - verification
  - reactivation
  - impact-assessment
type: procedure
tools: []
tactics:
  - '[[Command and Control]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:53.393Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: 8f8e9cb4-364d-4b54-968a-851efcf84562
validated: true
mitre_tactics:
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Changes-After-Reactivation

## Summary

Reactivate the account and confirm that unauthorized modifications persist, proving the bypass's impact.

## Description

After mutations, enabling the account (which sends a notification) shows changes in the UI, indicating backend persistence without prior alerts.

## Requirements

1. Access to 'Enable' button on disabled page
2. Owner email for notification (to simulate)
3. Post-reactivation login

## Defense

Defensive measures and detection strategies:

- Roll back changes on reactivation
- Audit logs for pre-reactivation mutations
- Require approval for sensitive updates

## Objectives

1. Trigger reactivation
2. Validate data alterations
3. Assess notification gaps

## Instructions

### Step 1: Enable Account

**Context**: Initiate reactivation.

No command; Click 'Enable' on https://hackerone.com/settings/disabled/edit.

> Email sent to owner; account status changes.

### Step 2: Log In and Check Settings

**Context**: Verify persistence.

No command; Log in normally, navigate to https://hackerone.com/settings/payment_preferences.

> Expected: New PayPal method listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- post-exploit-verification
- persistence-check
