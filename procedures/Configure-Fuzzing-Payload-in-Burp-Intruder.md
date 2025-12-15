---
tags:
  - payload
  - fuzzing
  - enumeration
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:24:56.424Z'
sub_techniques: []
id: 99b46668-28ed-434a-8897-00791c2a347e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Configure-Fuzzing-Payload-in-Burp-Intruder

## Summary

This procedure sets up payload positions and types in Burp Intruder to fuzz the category ID parameter with sequential numbers, targeting enumeration of unprotected API categories.

## Description

In the information disclosure attack on Discourse APIs, marking the ID (e.g., 38) for replacement and using numeric payloads from 1 to 1000 allows systematic probing. This reveals categories returning user data. Burp's Numbers payload type generates integers efficiently. Expected outcome is configured positions ready for attack launch.

## Requirements

1. Request loaded in Burp Intruder
2. Knowledge of the enumerable parameter (category ID in URL)
3. Estimated range for payloads (e.g., 1-1000 based on forum size)

## Defense

Defensive measures and detection strategies:

- Parameter validation and sanitization on API routes
- CAPTCHA or throttling on sequential ID requests to prevent enumeration

## Objectives

1. Define injection point for fuzzing
2. Generate appropriate payloads for ID enumeration
3. Optimize for efficiency in discovery

## Instructions

### Step 1: Mark Payload Position

**Context**: Identify and highlight the parameter to fuzz.

In Intruder > Positions tab, click on the category ID in the URL (e.g., highlight "38" and use Ctrl+I or button to mark as §38§). Clear any other auto-marked positions.

> Positions tab updates to show one § position for the ID.

### Step 2: Set Payload Type

**Context**: Configure payloads as sequential numbers.

Switch to Payloads tab, set Payload type to "Numbers". Configure: From 1, To 1000, Step 1, Include leading 0s: No, Infinite: No.

> Payloads preview shows 1,2,3,... up to 1000, ready for injection like /c/beta-builds/1.json.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[payload]]
- [[enumeration]]
