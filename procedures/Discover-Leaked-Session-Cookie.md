---
tags:
  - discovery
  - cookie-leak
type: procedure
tools:
  - '[[tools/cURL]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: d64fea71-1f5d-4277-be5a-bd31eea33c9b
created_at: '2025-12-10T05:55:44.998Z'
updated_at: '2025-12-10T05:55:44.998Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---
# Discover Leaked Session Cookie

## Summary

This procedure involves monitoring bug bounty reports to identify accidentally leaked sensitive data like session cookies in comments.

## Description

Attackers interact with reports on platforms like HackerOne, scanning comments for pasted commands that include credentials. This discovery phase enables further exploitation without technical tools beyond a browser.

## Requirements

1. Access to the bug bounty platform.
2. Ability to view report comments.
3. Tool: [[tools/Browser]].

## Defense

Defensive measures and detection strategies:

- Restrict comment visibility and implement data loss prevention scans.
- Monitor for unusual report viewing patterns.

## Objectives

1. Locate a leaked session cookie.
2. Extract the cookie value for reuse.
3. Assess potential impact.

## Instructions

### Step 1: Monitor Report Comments

**Context**: Browse active reports and review comments for sensitive data.

No command; use the browser interface to read comments.

> Look for strings like 'Cookie: session=...' in pasted cURL commands.

### Step 2: Extract Cookie Value

**Context**: Copy the identified cookie for later use.

No command; manually note the value.

> Ensure the cookie appears valid and not expired.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser]]

## Tags

- [[Discovery]]
- #cookie-leak
