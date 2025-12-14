---
tags:
  - auth-bypass
  - hackerone
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
updated_at: '2025-12-14T17:32:48.317Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 455e0e44-ac05-4891-bf72-10bec1ef8a6b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Contact-Support-for-Account-Ban

## Summary

This procedure involves intentionally contacting HackerOne support to request a ban on report submissions for the account, setting up the conditions for demonstrating an API bypass vulnerability.

## Description

In the context of testing HackerOne's ban enforcement, reach out to support via their designated channels (e.g., email or in-app support) to request that your researcher account be banned from submitting reports. This simulates a scenario where a user has been flagged for abuse. Once banned, UI-based submissions are restricted, but API access remains open, allowing the bypass. Prerequisites include a valid HackerOne account with researcher privileges.

## Requirements

1. Active HackerOne researcher account
2. Access to support contact methods (email or UI)
3. Internet connectivity

## Defense

Defensive measures and detection strategies:

- Monitor support ticket volumes for suspicious ban requests
- Implement rate limiting on support interactions
- Log all ban actions for audit

## Objectives

1. Trigger account ban to enforce UI restrictions
2. Establish baseline for bypass testing
3. Expected outcome: Ban confirmation from support

## Instructions

### Step 1: Initiate Support Contact

**Context**: Use HackerOne's support interface to request the ban, providing a reason like testing or simulation.

**Command** (No command; manual action):

Navigate to HackerOne support and submit a ticket requesting report submission ban.

> Support will process the request, resulting in a ban applied to the account. Expected output: Email or in-app confirmation of ban enforcement.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- hackerone
