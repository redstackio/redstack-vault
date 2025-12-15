---
id: proc-omise-2fa-bruteforce-001
tags:
  - brute-force
  - 2fa-bypass
  - credential-access
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.515Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
---
# Brute-Force-Password-in-2FA-Disable-Process

## Summary

This procedure exploits the lack of rate limiting and CAPTCHA on password confirmation during the 2FA disable process in Omise's web dashboard, allowing an attacker with an active session to brute force the user's password, disable multi-factor authentication, and achieve full account takeover.

## Description

In the Omise dashboard, disabling 2FA requires password confirmation via a web form submitted to an endpoint without protections against repeated attempts. Attackers can leverage an existing session (e.g., from a shared or forgotten login) to repeatedly submit passwords. By capturing requests with a proxy like Burp Suite and fuzzing the 'password' parameter, differences in response content length (e.g., shorter error for invalid, detailed success for valid) serve as an oracle to identify the correct password. Once guessed, 2FA is disabled, removing MFA protection and granting persistent access. This targets web applications with weak authentication controls in sensitive operations.

## Requirements

1. Active session in the Omise dashboard (valid credentials or session hijack)
2. Proxy tool like Burp Suite for request interception and fuzzing
3. Wordlist of potential passwords (e.g., common passwords, leaked creds)
4. Network access to https://dashboard.omise.co

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 attempts per minute) on password submissions during 2FA changes
- Add CAPTCHA or secondary verification (e.g., email code) for disable requests
- Monitor for anomalous request patterns, like high-volume POSTs to auth endpoints from single sessions
- Use response normalization to eliminate side-channel leaks (e.g., uniform error messages and lengths)

## Objectives

1. Guess the user's password via brute force using session access
2. Disable 2FA to bypass multi-factor protection
3. Achieve full account control without further authentication barriers

## Instructions

### Step 1: Establish Active Session

**Context**: Gain access to the dashboard to reach the 2FA disable feature without triggering full login.

Navigate to https://dashboard.omise.co/signin and login with valid credentials to set session cookies.

> Successful login redirects to the dashboard, confirming session establishment.

### Step 2: Access 2FA Disable Prompt

**Context**: Trigger the vulnerable password confirmation form.

From the dashboard, click the username to open the profile menu, select Two-factor authentication, and choose Disable 2FA.

> The form appears with a password input field; no rate limits are enforced on submissions.

### Step 3: Intercept and Baseline Request

**Context**: Capture the initial submission to identify the password parameter and response patterns.

Configure [[tools/Burp-Suite]] as a proxy, enter a random password, and submit. Note the POST request to the disable endpoint (e.g., /api/2fa/disable) and response details like content length for invalid input.

> Baseline: Invalid responses are short (e.g., 100 bytes JSON error); valid would differ (e.g., 500+ bytes success).

### Step 4: Fuzz the Password Parameter

**Context**: Automate brute force attempts to guess the password using the side-channel oracle.

In Burp Intruder, set the password position as payload, load a wordlist, and attack. Iterate through candidates, comparing response lengths or timings.

> On correct guess, response indicates success (e.g., longer content or redirect); resubmit to confirm disable.

### Step 5: Verify 2FA Disable and Access

**Context**: Confirm exploitation and test for takeover.

After successful submission, check account settings for 2FA status. Attempt login on another device without MFA.

> 2FA is disabled; full access granted without multi-factor prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[2fa-bypass]]
- [[account-takeover]]
