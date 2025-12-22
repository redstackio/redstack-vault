---
tags:
  - session-takeover
  - token-swapping
type: procedure
tools:
  - '[[tools/Custom-HTTP-Smuggling-Tools]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/smuggle-request-basic]]'
  - '[[commands/smuggle-request-token-theft]]'
  - '[[commands/smuggle-request-triage]]'
  - '[[commands/get-userid]]'
  - '[[commands/get-userdetails]]'
  - '[[commands/post-auth]]'
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b76e9142-d911-4688-9b7d-3fc29cebdac5
created_at: '2025-12-11T06:10:24.465Z'
updated_at: '2025-12-11T06:10:24.465Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1550]]'
---
# Perform Session Takeover by Token Swapping

## Summary

This procedure intercepts an authentication response and swaps tokens to achieve session takeover of a victim's account.

## Description

By modifying the response of a POST /v2/auth request with the victim's Access-Token and UserID, the attacker gains authenticated access, applicable in APIs with token-based auth.

## Requirements

1. Stolen Access-Token and UserID
2. Burp Suite for interception
3. Active session to intercept

## Defense

Defensive measures and detection strategies:

- Use secure token generation and validation
- Detect session anomalies like IP changes

## Objectives

1. Swap tokens in auth response
2. Gain victim account access
3. Enable persistent compromise

## Instructions

### Step 1: Intercept and Modify Auth

**Context**: Use Burp to capture and edit response.

Execute [[commands/post-auth]]:

```bash
POST /v2/auth
```

> Replace Access-Token/UserID with victim's in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used

- [[commands/post-auth]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[session-takeover]]
- [[token-swapping]]
