---
tags:
  - business-logic-flaw
  - api-key-abuse
  - steam
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.938Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 42a4f135-b3a5-4de8-9747-b4dc6462bffb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Reuse-Request-ID-for-Additional-Key-Registration

## Summary

This procedure exploits the Steam API registration flaw by resubmitting the same confirmed `request_id` to generate additional API keys, bypassing the intended one-key-per-account restriction.

## Description

After confirmation, the `request_id` remains valid due to improper invalidation, allowing repeated submissions to the registration endpoint. This targets the Steam Web API, requires the prior `request_id`, and results in multiple keys, potentially enabling API limit abuse or unauthorized access. The attack scenario involves manual or scripted resubmissions.

## Requirements

1. Confirmed `request_id` from previous steps
2. Access to the registration endpoint
3. Steam account session active

## Defense

Defensive measures and detection strategies:

- Invalidate `request_id` post-confirmation and generate new ones per attempt
- Enforce strict one-key-per-account policy with database checks
- Monitor API key issuance logs for duplicates from single accounts

## Objectives

1. Register additional API keys using the reused `request_id`
2. Demonstrate the business logic vulnerability
3. Gain multiple keys for potential abuse

## Instructions

### Step 1: Prepare Resubmission

**Context**: Use the existing `request_id` without generating a new one.

Return to the API key registration page or endpoint, ensuring the session is active.

> No new initiation; directly prepare to submit the known `request_id`.

### Step 2: Submit Reused request_id

**Context**: Resend the registration request with the same `request_id`.

Fill the form or API payload with the confirmed `request_id` and submit again. Repeat for multiple keys.

> Each successful submission issues a new key; verify in the dashboard for multiples.

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
- api-key-abuse
- steam
