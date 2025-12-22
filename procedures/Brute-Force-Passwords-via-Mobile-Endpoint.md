---
id: proc-bruteforce-passwords-mobile
tags:
  - brute-force
  - credential-access
type: procedure
tools:
  - '[[tools/BurpSuite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:24:41.832Z'
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute Force Passwords via Mobile Endpoint

## Summary

This procedure exploits the lack of rate limiting on the Instacart iOS app's login endpoint to attempt multiple passwords rapidly, gaining unauthorized access and bypassing web-based account locks after ~15 failures.

## Description

The mobile endpoint (POST https://www.instacart.com/oauth/token) does not enforce locks or delays, unlike the web version. Using Burp Repeater, attackers replay the intercepted request with a password list, checking for 200 OK responses with access tokens. To demonstrate bypass, lock the account via web first, then succeed via app. Expected outcomes include account compromise if weak passwords are used.

## Requirements

1. Intercepted login request template from prior steps
2. Wordlist of passwords (e.g., rockyou.txt or top 100 common)
3. Target username/email
4. BurpSuite Repeater or Intruder for automation

## Defense

Defensive measures and detection strategies:

- Implement rate limiting and progressive delays on all login endpoints, including mobile
- Apply account locking consistently across web and app (e.g., shared backend flags)
- Monitor for high-volume failed logins from single IPs or user agents indicating mobile clients

## Objectives

1. Enumerate valid passwords through exhaustive trials
2. Achieve account access without triggering defenses
3. Validate bypass of web-specific protections

## Instructions

### Step 1: Prepare Request in Repeater

**Context**: Load the intercepted request for modification.

In BurpSuite, send the captured login to Repeater. Identify the password parameter in the body (e.g., "password": "value") and prepare to edit it.

### Step 2: Lock Account via Web (Optional Bypass Test)

**Context**: Simulate web defenses to test mobile bypass.

Using a browser, attempt ~15 invalid logins on the Instacart website with the target account until locked (error message indicates lockout).

### Step 3: Execute Brute Force Attempts

**Context**: Replay with password variations to find valid credentials.

In Repeater, change the password to entries from a wordlist (manual for small lists, or use Intruder for automation: set payload position on password, load wordlist, attack type Sniper). Send requests; invalid yield 401, valid yield 200 with {"access_token": "...", "token_type": "Bearer"}. Continue until success or list exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used

- [[tools/BurpSuite]]

## Tags

- [[brute-force]]
- [[credential-access]]
