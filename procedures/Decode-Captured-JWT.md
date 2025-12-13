---
tags:
  - jwt-decoding
type: procedure
tools:
  - '[[tools/jwt-io]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Credentials In Files]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 80dacb1a-cf67-4ab8-be26-22a2789a591a
created_at: '2025-12-13T09:01:26.688Z'
updated_at: '2025-12-13T09:01:26.688Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Decode Captured JWT

## Summary

This procedure decodes the intercepted JWT to view its payload and header.

## Description

Using an online tool, the attacker pastes the JWT to decode it without verifying the signature initially. This reveals claims like email and timestamps, essential for tampering. Targets web auth systems with JWTs.

## Requirements

1. Captured JWT token
2. Access to jwt.io

## Defense

Defensive measures and detection strategies:

- Use asymmetric signing to prevent easy tampering
- Avoid exposing token structures

## Objectives

1. Analyze JWT claims
2. Identify modifiable fields
3. Extract signing algorithm

## Instructions

### Step 1: Use Decoding Tool

**Context**: Decode the token.

Paste the JWT into jwt.io to decode and view payload.

> Observe the header, payload, and signature sections.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/jwt-io]]

## Tags

- [[jwt-decoding]]
