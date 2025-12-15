---
tags:
  - auth-bypass
  - 2fa
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ubnt-login]]'
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1c2c6831-8d22-463e-b368-24e33e208d8a
created_at: '2025-12-14T17:31:19.775Z'
updated_at: '2025-12-14T17:31:19.775Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Submit-Valid-Credentials-to-Initiate-2FA

## Summary

This procedure submits valid username and password to the Ubiquiti login page, initiating the 2FA challenge and establishing a session cookie for subsequent brute-force attempts.

## Description

In the context of the Ubiquiti 2FA bypass vulnerability, this step authenticates the primary credentials on www.ubnt.com, which triggers the server to send a 6-digit 2FA code (typically via email or app) and returns a session token. The lack of rate limiting on the following 2FA verification allows brute-forcing. Prerequisites include knowing valid credentials for the target account. Expected outcome is a partial authentication state ready for code submission.

## Requirements

1. Valid username and password for a Ubiquiti account
2. Network access to www.ubnt.com
3. curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Implement account lockout after failed primary login attempts
- Monitor for unusual login patterns from known credentials
- Use device fingerprinting to detect automated submissions

## Objectives

1. Establish authenticated session with primary credentials
2. Trigger 2FA code generation on the server
3. Prepare for 2FA verification bypass

## Instructions

### Step 1: Prepare Login Request

**Context**: Set up the HTTP POST request to the login endpoint with credentials.

**Command** ([[commands/curl-ubnt-login]]):
```bash
curl -X POST https://www.ubnt.com/login -d "username=validuser&password=validpass" -c cookies.txt -v
```

> This command sends the credentials, saves session cookies to cookies.txt, and uses -v for verbose output to confirm the 2FA prompt in the response.

### Step 2: Verify 2FA Initiation

**Context**: Check the response to ensure 2FA is required and session is active.

**Command** ([[commands/curl-ubnt-login]]):
```bash
curl -X POST https://www.ubnt.com/login -d "username=validuser&password=validpass" -c cookies.txt | grep -i "2fa\|code"
```

> Expected output includes indicators like "Enter 2FA code" or a token in the response body, confirming the session is ready for brute-force.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ubnt-login]]

## Tools Used


## Tags

- [[auth-bypass]]
- [[2fa]]
