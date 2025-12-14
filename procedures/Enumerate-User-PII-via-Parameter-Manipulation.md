---
tags:
  - idor
  - enumeration
  - pii-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:32:58.345Z'
sub_techniques: []
id: 5fee90f4-26ae-444d-99d2-90cde643b3dd
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Credentials In Files]]'
---
# Enumerate User PII via Parameter Manipulation

## Summary

This procedure exploits an Insecure Direct Object Reference (IDOR) by manipulating a numeric parameter in the disclosure endpoint to enumerate PII for multiple users on the MASS platform, enabling mass data collection without authentication.

## Description

The endpoint uses sequential numeric IDs for users without access controls, allowing attackers to decrement or increment the parameter to access arbitrary user records. This IDOR flaw, combined with the lack of rate limiting, permits efficient enumeration of names, emails, mobile numbers, and pins, which can lead to widespread account compromises.

## Requirements

1. Initial successful access from the disclosure procedure
2. Web browser for manual manipulation
3. Optional scripting knowledge for automation (e.g., via browser console)

## Defense

Defensive measures and detection strategies:

- Enforce indirect object references using GUIDs instead of sequential IDs
- Implement rate limiting and IP-based access controls on sensitive endpoints
- Log and alert on sequential parameter requests indicating enumeration attempts

## Objectives

1. Collect PII for multiple users
2. Identify high-value targets (e.g., admin accounts)
3. Prepare data for credential access procedures

## Instructions

### Step 1: Modify the Numeric Parameter

**Context**: Start from a known valid ID and decrement to access prior users.

In the browser, change the URL parameter, e.g., from `https://www.████████/███████?id=123` to `https://www.████████/███████?id=122`.

> Each change loads new PII. Repeat for several IDs to confirm enumeration works. Expected output: Unique user data per ID.

### Step 2: Document and Scale Enumeration

**Context**: Record leaked data for use in reset flows.

Manually note emails and pins, or use browser extensions to export responses.

> Successful scaling reveals patterns in user IDs, allowing prediction of total user count.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Credentials In Files]] Credentials In Files (adapted for web params)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[enumeration]]
- [[pii-leak]]
