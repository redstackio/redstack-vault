---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567896
tags:
  - brute-force
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:31:42.731Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Execute Brute-Force Attack to Update Password

## Summary

Run the Intruder attack to brute-force the old password, identify the correct one, and update to attacker-controlled value for takeover.

## Description

Start the attack; due to no rate limiting, send 1000+ requests quickly. Success is indicated by a different response (e.g., 200 with update confirmation vs. 400 error). Once found, the password is reset, granting full control.

## Requirements

1. Payloads loaded in Intruder
2. Session still valid
3. Monitor for response differences

## Defense

Defensive measures and detection strategies:

- Add server-side rate limiting (e.g., 10 req/min per session)
- Use progressive delays or bans on failures
- Alert on high-volume auth attempts

## Objectives

1. Guess correct old password
2. Successfully update password
3. Achieve account takeover

## Instructions

### Step 1: Start Attack

**Context**: Launch the brute-force.

In Intruder, click Start attack.

> Expected output: Requests sent; progress bar advances.

### Step 2: Monitor and Identify Success

**Context**: Watch responses for the correct password.

Sort by length/status; success shows password update (e.g., redirect or success message).

> Expected output: ~4 minutes for 1000+ tries; confirmed takeover by new login.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Password Guessing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-takeover
