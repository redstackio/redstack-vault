---
id: proc-uuid-7936-brute-force
tags:
  - brute-force
  - credential-access
  - web
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-brute-force]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:27:23.471Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Perform-Brute-Force-on-Login-Endpoint

## Summary

This procedure leverages the lack of rate limiting on Secret.ly's login endpoint to perform repeated credential guessing attempts, potentially cracking user passwords.

## Description

The POST /_/login endpoint processes JSON login requests without mentioned throttling, allowing unlimited attempts. Attackers can script loops of requests with a wordlist to guess credentials for a target username. In the Secret.ly scenario, this amplifies the CSRF risk by enabling mass unauthorized logins. Prerequisites include a list of potential passwords and basic scripting. Successful execution leads to credential compromise and account takeover.

## Requirements

1. Target username (e.g., from reconnaissance)
2. Password wordlist
3. Scriptable environment for looping requests

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 attempts per IP per minute)
- Use CAPTCHA after failed logins
- Monitor for high-volume login failures and block IPs

## Objectives

1. Submit multiple credential guesses
2. Identify valid combinations
3. Achieve unauthorized authentication

## Instructions

### Step 1: Prepare Wordlist

**Context**: Create or obtain a list of common passwords.

No command; use a file like passwords.txt.

### Step 2: Execute Brute Force Loop

**Context**: Send repeated POST requests varying the password.

**Command** ([[commands/curl-brute-force]]):
```bash
for pass in $(cat passwords.txt); do curl -X POST https://www.secret.ly/_/login -H "Content-Type: application/json" -d '{"Login":"target@example.com","Password":"$pass"}'; done
```

> Expected output: Responses for each attempt; success shown by auth token or no error.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques


## Commands Used

- [[commands/curl-brute-force]]

## Tools Used


## Tags

- [[brute-force]]
- [[credential-access]]
