---
id: uuid-6
tags:
  - brute-force
  - automation
  - account-takeover
type: procedure
tools:
  - '[[tools/InstagramBrandLoginBruteForce.rb]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/run-brute-force-ruby-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:33:12.515Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Automated-Brute-Force-Login-with-Ruby-Script

## Summary

This procedure uses a custom Ruby script to automate password brute-force attempts on the login endpoint using enumerated emails, exploiting absent rate limiting for potential account takeover.

## Description

The login endpoint (/wp-json/brc/v1/login/) accepts unlimited guesses without CAPTCHA or lockout, allowing ~100 attempts/min single-threaded. Success grants session access; script can be multi-threaded for speed.

## Requirements

1. Ruby installed
2. passlist.txt with password candidates
3. Enumerated target email set in script (line 7)

## Defense

Defensive measures and detection strategies:

- Add rate limiting and progressive delays
- Integrate CAPTCHA post-failed attempts
- Lock accounts after N failures

## Objectives

1. Guess valid credentials for takeover
2. Scale attacks across multiple targets
3. Achieve compromise at ~144,000 attempts/day

## Instructions

### Step 1: Configure Script

**Context**: Set target and prepare passwords.

Edit line 7 in InstagramBrandLoginBruteForce.rb with target email. Create passlist.txt.

### Step 2: Execute Brute-Force

**Context**: Run attempts against login endpoint.

**Command** ([[commands/run-brute-force-ruby-script]]):

```bash
ruby InstagramBrandLoginBruteForce.rb
```

> Logs attempts; success if login response indicates auth (e.g., token). 1020 attempts in 10 min demoed.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Password Guessing]] Brute Force: Password Guessing

### Sub-Techniques


## Commands Used

- [[commands/run-brute-force-ruby-script]]

## Tools Used

- [[tools/InstagramBrandLoginBruteForce.rb]]

## Tags

- brute-force
- automation
- account-takeover
