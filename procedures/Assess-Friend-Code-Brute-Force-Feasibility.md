---
tags:
  - brute-force
  - rate-limiting
  - crashplan
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f819aef0-4664-44e2-ba8b-885064e877d2
created_at: '2025-12-14T17:26:30.457Z'
updated_at: '2025-12-14T17:26:30.457Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Assess-Friend-Code-Brute-Force-Feasibility

## Summary

This procedure evaluates the security of CrashPlan's friend code system by calculating the keyspace and testing for rate limiting on the validation endpoint, determining if brute-forcing is practical.

## Description

Friend codes in CrashPlan are 6-character alphanumeric strings (0-9, a-z), yielding 36^6 = 2,176,782,336 possibilities. The validation endpoint (likely a POST to /validate or similar on backup.uber.com:443) lacks rate limiting, allowing rapid guesses. This assessment involves manual calculation and light testing to avoid detection. Prerequisites include understanding HTTP request patterns. Outcome: Confirmation that the small keyspace and no throttling make brute-forcing feasible within hours to days.

## Requirements

1. Basic scripting knowledge for request simulation
2. Access to the validation endpoint
3. Calculator or script for keyspace computation

## Defense

Defensive measures and detection strategies:

- Introduce rate limiting (e.g., 10 req/min per IP) on code validation
- Use CAPTCHA or stronger auth for public endpoints
- Log and alert on high-volume requests to backup APIs

## Objectives

1. Compute total possible friend codes
2. Test endpoint for throttling
3. Estimate brute-force timeline

## Instructions

### Step 1: Calculate Keyspace

**Context**: Determine the number of possible codes to assess attack viability.

Manually compute or script: 36 options (10 digits + 26 letters) raised to power 6.

> Expected output: 2,176,782,336 combinations; at 1,000 requests/second, feasible in ~24 days.

### Step 2: Test Rate Limiting

**Context**: Send multiple validation requests to check for delays or blocks.

Use a loop in a script or browser console to submit 100+ invalid codes rapidly to the endpoint.

> Expected output: All requests process without errors, delays, or IP bans, confirming no rate limiting.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[brute-force]]
- [[rate-limiting]]
