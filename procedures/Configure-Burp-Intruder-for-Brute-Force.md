---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - brute-force
  - intruder
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
updated_at: '2025-12-14T17:31:42.739Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Configure Burp Intruder for Brute-Force

## Summary

Set up Burp Intruder's payload positions on the old_password field to automate brute-forcing.

## Description

From the intercepted request, send to Intruder and mark the old_password value for replacement with payloads. This exploits the no-rate-limit flaw to try multiple guesses rapidly.

## Requirements

1. Intercepted POST request in Burp
2. Basic familiarity with Burp UI

## Defense

Defensive measures and detection strategies:

- Enforce rate limits on auth endpoints (e.g., 5 attempts/min)
- Log rapid successive requests from sessions
- Use anomaly detection for brute-force patterns

## Objectives

1. Automate password guessing
2. Target vulnerable field
3. Prepare for wordlist loading

## Instructions

### Step 1: Send to Intruder

**Context**: Transfer the request for attack configuration.

Right-click intercepted request > Send to Intruder.

> Expected output: Intruder tab opens with request loaded.

### Step 2: Set Payload Position

**Context**: Mark the field to brute-force.

In Positions tab, clear defaults, then highlight old_password value and click Add §.

> Expected output: §old_password§ in request body.

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

- brute-force
