---
id: proc-17512-brute-force-token
tags:
  - brute-force
  - token-guessing
  - response-oracle
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:33:06.443Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute Force Reset Token

## Summary

This procedure uses Burp Suite to send multiple token variations, identifying valid ones via distinguishable server responses (200/4378 chars vs 302/1525 chars).

## Description

The vulnerability stems from no rate limiting and an oracle in responses: valid tokens load the edit page (200, long response), invalid redirect (302, short). Brute force guesses the token, often starting from a partial known value, leading to account access potential.

## Requirements

1. Configured Burp Intruder from prior step
2. Payload list (e.g., base64-like characters for tokens)
3. Target endpoint /users/password/edit

## Defense

Defensive measures and detection strategies:

- Enforce rate limiting on token checks
- Use uniform responses (e.g., always 302 for invalid)
- Shorten token lifespan and increase entropy

## Objectives

1. Send 1000+ token guesses efficiently
2. Detect valid token via response metrics
3. Extract full valid token

## Instructions

### Step 1: Launch Intruder Attack

**Context**: Execute brute force with payloads.

In Burp Intruder, click Start attack. Use options to grep for status/length.

> Monitor results table; filter for 200 status and ~4378 length.

### Step 2: Identify and Validate

**Context**: Confirm valid token.

Select high-length responses, replay to verify.

> Success: Valid token found, ready for reset.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[token-guessing]]
- [[response-oracle]]
