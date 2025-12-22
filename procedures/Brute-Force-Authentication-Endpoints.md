---
tags:
  - brute-force
  - missing-rate-limit
  - credential-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - ASP.NET Core
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:25:29.295Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Password Guessing]]'
id: 790c96dc-2450-47ef-874d-a6ad05443116
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-Authentication-Endpoints

## Summary

This procedure exploits the absence of rate limiting on signup and password reset endpoints to perform unlimited brute-force attempts, potentially discovering credentials or gaining admin access.

## Description

The application's authentication flows (signup and forgot password) allow unrestricted requests without CAPTCHA or throttling, enabling automated guessing of usernames, emails, or passwords. This can be combined with leaked PII from IDOR to target specific accounts, increasing success rates for account takeover.

## Requirements

1. List of potential credentials or emails from PII leak
2. Burp Suite Intruder or similar for automation
3. Network access to auth endpoints

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 attempts per IP per minute)
- Add CAPTCHA after failed logins
- Monitor logs for high-volume requests to auth paths
- Use account lockouts after multiple failures

## Objectives

1. Guess valid credentials via unlimited attempts
2. Access admin or privileged accounts
3. Amplify impact from leaked PII

## Instructions

### Step 1: Identify Endpoints

**Context**: Locate signup and reset pages.

Navigate to /signup and /forgot-password; confirm no limits by sending multiple requests.

### Step 2: Automate Brute-Force

**Context**: Use Burp Intruder to test payloads.

Capture a login request, send to Intruder, and load a wordlist for username/password positions. Start attack with unlimited iterations.

**Expected Output**: Successful login response (302 redirect) for valid combos.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[credential-access]]
