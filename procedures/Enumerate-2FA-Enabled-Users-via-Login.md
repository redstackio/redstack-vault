---
tags:
  - 2fa-enumeration
  - business-logic-error
  - user-enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-attempt-invalid-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:47.421Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1a4367e7-f01f-4af1-a936-0e5ee2a9eaf6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-2FA-Enabled-Users-via-Login

## Summary

This procedure exploits a business logic error in the login process where invalid passwords still trigger a 2FA prompt for enabled accounts, allowing enumeration of 2FA status without valid credentials. It is useful for reconnaissance in web applications to identify protected accounts for targeted attacks.

## Description

In vulnerable applications like Legal Robot's, the login flow checks for 2FA enablement before fully validating the password. For users with 2FA, an incorrect password leads to a second-factor prompt; for others, it rejects immediately. This timing or response difference enables enumeration. The attack requires public access to the login endpoint and a list of usernames. Rate-limiting may slow but not prevent it, as responses still leak information. Expected outcomes include a mapping of usernames to 2FA status, aiding phishing or social engineering against secure accounts. No account takeover is possible directly, but it exposes security configurations.

## Requirements

1. Access to the target's login endpoint (e.g., HTTPS POST to /login)
2. List of known or guessed usernames (e.g., from email enumeration)
3. Tool for HTTP requests (curl or browser)
4. Awareness of rate-limits to avoid IP blocking

## Defense

Defensive measures and detection strategies:

- Validate password before any 2FA checks and return generic errors
- Implement consistent response timings or messages for all login failures
- Monitor for repeated failed logins from single IPs and enforce strict rate-limits
- Log and alert on enumeration patterns (e.g., high volume of invalid attempts)

## Objectives

1. Determine 2FA enablement for specific usernames
2. Compile a list of high-security (2FA-protected) accounts
3. Expose application logic flaws for reporting or exploitation

## Instructions

### Step 1: Prepare Test Data

**Context**: Gather usernames and a deliberately wrong password to avoid accidental success.

No command needed; manually prepare a list like usernames.txt with one username per line.

### Step 2: Execute Invalid Login Attempt

**Context**: Send a POST request to the login endpoint with the username and wrong password to observe the response.

**Command** ([[commands/curl-attempt-invalid-login]]):
```bash
curl -X POST -d "username=targetuser@example.com&password=wrongpass123" https://target.com/login -c cookies.txt -v
```

> This command performs the login attempt, saving cookies for session tracking and using -v for verbose output to inspect headers/responses. Look for 2FA indicators like a 200 OK with 2FA form HTML, redirect to /verify-2fa, or JSON {"stage": "2fa"}. A 401/403 with "invalid credentials" indicates no 2FA.

### Step 3: Log and Repeat

**Context**: Record the 2FA status and repeat for other usernames, respecting rate-limits (e.g., wait 60 seconds between attempts).

Use a script or manual notes to track: if 2FA prompt detected, mark as "enabled"; else "disabled".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-attempt-invalid-login]]

## Tools Used


## Tags

- 2fa-enumeration
- business-logic-error
- user-enumeration
