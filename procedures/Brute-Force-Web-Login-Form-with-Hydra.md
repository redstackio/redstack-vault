---
id: 58514fe3-dd53-4fba-949a-4126d85002be
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T18:54:56.457834+00:00'
updated_at: '2023-05-26T15:57:57.129350+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques:
  - '[[techniques/T1110.001 - Password Guessing]]'
platforms:
  - Web
tags:
  - Brute Force
  - Web Applications
commands:
  - '[[commands/hydra-brute-force-http-post-login-form]]'
tools:
  - '[[tools/Hydra]]'
  - '[[tools/Burp-Suite]]'
validated: true
---

# Brute-Force-Web-Login-Form-with-Hydra

## Summary

Brute-force WordPress login credentials by capturing the HTTP POST form details with Burp Suite and using Hydra to test username/password combinations against the failure string.

## Description

Web logins often use POST requests with cookies and parameters like username/password. This procedure intercepts a sample login to extract the exact format, then automates brute-forcing with Hydra, succeeding only when the failure message (e.g., 'incorrect') is absent.

## Requirements

- Valid usernames from prior enumeration
- Password wordlist
- Burp Suite for proxy interception
- Target login path (e.g., /wp-login.php)

## Defense

- Enforce account lockouts after failed attempts
- Use multi-factor authentication (MFA)
- Deploy WAF to block brute-force patterns

## Objectives

1. Extract login form parameters and failure indicator
2. Automate credential testing
3. Gain authenticated access to wp-admin

## Instructions

### Step 1: Capture Login Request

**Context**: Attempt a login to intercept the POST, noting parameters like log=^USER^&pwd=^PASS^ and the negative result string 'incorrect'.

No command; use Burp Proxy: POST /wp-login.php with body: log=admin&pwd=test&wp-submit=Log+In.

> Identify the failure page text for Hydra's denial string.

### Step 2: Run Hydra Brute-Force

**Context**: Feed usernames and passwords into Hydra, specifying the form path, POST data, and failure condition.

**Command** ([[commands/hydra-brute-force-http-post-login-form]]):
```bash
hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARGET_IP http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:incorrect'
```

> Hydra tests combinations; success shows valid creds without 'incorrect'.
