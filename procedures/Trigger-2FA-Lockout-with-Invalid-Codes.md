---
tags:
  - dos
  - lockout
  - rate-limit
  - invalid-code
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-trigger-lockout]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:24:48.353Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: 1b3f706a-ce06-42d4-99d9-8d2780365700
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Trigger-2FA-Lockout-with-Invalid-Codes

## Summary

This procedure submits modified 2FA requests with incorrect codes multiple times to exhaust rate limits, locking the victim's account for 5 minutes and causing DoS.

## Description

Exploiting the IDOR in cookie validation, repeated invalid submissions apply lockouts to the impersonated SteamID. This affects login and other 2FA actions, with potential for chaining to delete 2FA if escalated.

## Requirements

1. Modified request with victim's steamid
2. At least 4 invalid 2FA codes (random 6-digit strings)
3. Ability to repeat requests rapidly

## Defense

Defensive measures and detection strategies:

- Tie rate limits to IP + SteamID pairs
- Add CAPTCHA after failed attempts
- Alert on rapid failures from single sources

## Objectives

1. Exhaust 2FA submission quota
2. Induce 5-minute lockout
3. Disrupt victim's access to account

## Instructions

### Step 1: Prepare Invalid Code Requests

**Context**: Set up the modified request with wrong code.

Use [[commands/curl-trigger-lockout]] as base:

```bash
curl -X POST https://target.com/login/confirm -H "Cookie: steamid=victim_steamid" -d '{"token":"session_token","code":"000000"}'
```

> Response: Invalid code error.

### Step 2: Repeat Submission 4 Times

**Context**: Forward the request 4 times with different invalid codes (e.g., 000000, 111111, etc.).

Automate in Burp Intruder or script loops.

> After 4th: Lockout response (e.g., "Too many attempts, try again in 5 minutes").

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-lockout]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[dos]]
- [[lockout]]
- [[rate-limit]]
- [[invalid-code]]
