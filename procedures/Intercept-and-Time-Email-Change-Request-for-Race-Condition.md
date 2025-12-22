---
tags:
  - race-condition
  - interception
  - shopify
type: procedure
tools:
  - '[[tools/HTTP-Proxy-(e.g.,-Burp-Suite)]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 972ef38c-947e-4864-9a9c-b54d8641614b
created_at: '2025-12-11T03:47:56.678Z'
updated_at: '2025-12-11T03:47:56.678Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Intercept and Time Email Change Request for Race Condition

## Summary

This procedure uses an HTTP proxy to intercept and time an email change request to a victim's address, then visits a prior confirmation link to exploit the race condition.

## Description

The core exploit involves delaying the email change request (1,100-2,500 ms) and confirming the old link during the window where the database is in an inconsistent state, allowing arbitrary email confirmation.

## Requirements

1. HTTP proxy tool configured
2. Previously captured confirmation link
3. Victim's email address

## Defense

Defensive measures and detection strategies:

- Use database transactions or locking for email updates
- Detect timed requests or anomalies in confirmation timing

## Objectives

1. Bypass email verification
2. Confirm arbitrary email

## Instructions

### Step 1: Intercept Email Change

**Context**: Initiate email change to victim's address and intercept the request.

Use [[tools/HTTP-Proxy-(e.g.,-Burp-Suite)]] to intercept the HTTP request on the settings page.

### Step 2: Release and Confirm

**Context**: Release the request, wait milliseconds, then visit the old confirmation link.

Release the intercepted request, then immediately open the confirmation link in another tab.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/HTTP-Proxy-(e.g.,-Burp-Suite)]]

## Tags

- #race-condition
- #interception
- #shopify
