---
id: proc-csrf-login-redirect
tags:
  - csrf
  - authentication
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-csrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.893Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Handle-Login-Redirect-for-Unauthenticated-Users

## Summary

This procedure handles the login redirect in the CSRF attack, ensuring that even unauthenticated users complete the application submission automatically after logging in, without additional validation.

## Description

When an unauthenticated user accesses the malicious ?apply=true URL, HackerOne redirects to the login page while preserving the parameter. Upon successful login, the application submits seamlessly, especially for users with tax confirmation or prior bounties. This extends the attack surface to non-logged-in victims.

## Requirements

1. Victim account on HackerOne capable of login
2. Malicious URL from prior procedure
3. No attacker credentials needed

## Defense

Defensive measures and detection strategies:

- Clear sensitive parameters on redirects to login
- Require re-validation or tokens post-login for state changes
- Log and alert on parameter persistence across auth flows
- Educate users on phishing risks

## Objectives

1. Bypass authentication barriers in CSRF attacks
2. Automate submission post-login without confirmation
3. Increase attack reach to unauthenticated sessions

## Instructions

### Step 1: Simulate Unauthenticated Access

**Context**: Test the redirect behavior for non-logged-in users.

**Command** ([[commands/curl-trigger-csrf]]):
```bash
curl -X GET "https://hackerone.com/hackthedts?apply=true" -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:60.0) Gecko/20100101 Firefox/60.0" -v
```

> Follows redirects (-L); expect 302 to login, then post-auth success. In attack, victim logs in manually.

### Step 2: Verify Post-Login Submission

**Context**: Confirm automatic trigger after authentication.

Monitor victim's session; no command needed, but re-run Step 1 in authenticated context to validate.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-csrf]]

## Tools Used


## Tags

- [[csrf]]
- [[authentication]]
