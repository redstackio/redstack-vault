---
id: b37aeb8d-5044-4646-b06f-771a1df2a6a0
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T23:27:07.457615+00:00'
updated_at: '2023-05-26T18:36:07.091192+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
platforms:
  - Web
tags:
  - Web Applications
  - Brute Force
commands:
  - '[[commands/wfuzz-brute-force-http-post-form]]'
tools:
  - '[[tools/Wfuzz]]'
  - '[[tools/Burp-Suite]]'
validated: true
---

# Brute-Force-Valid-Users-via-Forgotten-Password-Form

## Summary

Exploit WordPress forgotten password forms that reveal valid usernames through differing error messages or HTTP responses, using fuzzing to enumerate accounts without full brute-force.

## Description

Many web apps, including WordPress, respond differently to valid vs. invalid usernames in password reset flows (e.g., 'Invalid username' vs. 'Email sent'). Intercept the POST request to capture parameters, then fuzz the 'user_login' field with a username list, filtering responses to spot valid ones.

## Requirements

- Access to /wp-login.php?action=lostpassword
- Username wordlist (e.g., common admin names)
- Burp Suite for request interception

## Defense

- Standardize error messages to avoid information disclosure
- Implement CAPTCHA or rate-limiting on reset forms
- Log and alert on repeated reset attempts

## Objectives

1. Capture the exact POST structure for the reset form
2. Fuzz usernames to identify valid accounts
3. Compile a list for subsequent password brute-forcing

## Instructions

### Step 1: Intercept and Analyze Reset Request

**Context**: Submit an invalid username to observe the response difference, then capture the POST with Burp to get parameters like user_login.

No command; use browser or Burp to POST to /wp-login.php?action=lostpassword with data: user_login=test&wp-submit=Get+New+Password.

> Invalid returns 200 with error; valid may return 500 or redirect. Note the POST data format.

### Step 2: Fuzz Usernames with Wfuzz

**Context**: Replace user_login with FUZZ and hide 200 (invalid) responses to highlight valid ones.

**Command** ([[commands/wfuzz-brute-force-http-post-form]]):
```bash
wfuzz --hc 200 -w $_USERS_TXT -u 'http://$_TARGET_IP/wp-login.php?action=lostpassword' -d 'user_login=FUZZ&redirect_to=&wp-submit=Get+New+Password'
```

> Valid users show 500 or other codes, e.g., 'elliot' with 500 response, confirming existence.
