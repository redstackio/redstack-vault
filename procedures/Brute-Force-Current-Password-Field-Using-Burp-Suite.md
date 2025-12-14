---
tags:
  - brute-force
  - account-takeover
  - web-auth
  - rate-limit-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3956617a-5b74-404d-b75c-c6ef599aace0
created_at: '2025-12-14T17:33:24.333Z'
updated_at: '2025-12-14T17:33:24.333Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-Current-Password-Field-Using-Burp-Suite

## Summary

This procedure exploits the absence of rate limiting on the current password field in the Acronis web application's password change process. Using Burp Suite's Intruder, an attacker automates brute force attempts to guess the user's current password, enabling unauthorized password changes and account takeover. It requires an active logged-in session and is effective against weak or common passwords.

## Description

The Acronis password change endpoint (accessed via Profile > Password) validates the current password without enforcing rate limits, allowing unlimited guesses. The attack involves intercepting the HTTP POST request, marking the current_password parameter for payload injection, loading a wordlist of potential passwords, and analyzing responses for success. Upon identifying the correct password, the attacker can submit a modified request to set a new password, gaining persistent control. This targets web-based authentication systems vulnerable to brute force, with high impact in multi-user or public access scenarios.

## Requirements

1. Active logged-in session to the target Acronis account
2. Burp Suite installed and configured as a proxy for the browser
3. Wordlist file with candidate passwords (e.g., 100+ common passwords like 'password123', 'admin')
4. Network access to the Acronis web application over HTTPS

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 attempts per minute) on password validation endpoints
- Enforce strong password policies and multi-factor authentication (MFA) to mitigate brute force risks
- Monitor for anomalous request patterns, such as high-volume POSTs to password change endpoints from the same IP/session
- Use CAPTCHA or device fingerprinting after failed attempts

## Objectives

1. Guess the correct current password through unlimited brute force attempts
2. Change the account password to attacker-controlled value
3. Achieve full account takeover for data access or further exploitation

## Instructions

### Step 1: Access Password Change Page and Trigger Initial Request

**Context**: Log in and navigate to the password change form to generate a baseline request for interception.

No specific command; perform manually in the browser:

- Go to Acronis dashboard > Profile > Password.
- Enter an incorrect current password (e.g., 'wrong') and a placeholder new password.
- Submit the form.

> This triggers an HTTP POST request to the password change endpoint, which will be intercepted in the next step. Expected response: 400/422 error with 'invalid current password' message.

### Step 2: Intercept Request with Burp Suite

**Context**: Capture the outgoing request to inspect and prepare it for automation.

No specific command; use Burp Suite GUI:

- Enable Intercept in Burp Proxy (Proxy > Options > Intercept Client Requests: On).
- Resubmit the password change form.
- In the Proxy > Intercept tab, forward the captured request after review.
- Right-click the request > Send to Intruder.

> The request body will include parameters like current_password=wrong&new_password=placeholder. Expected: Full HTTP request details visible.

### Step 3: Configure Payload Marker in Intruder

**Context**: Mark the current_password field for replacement with brute force payloads.

No specific command; configure in Burp Intruder:

- In Intruder > Positions, clear all positions (Attack type: Sniper).
- Add § markers around the current_password value (e.g., current_password=§wrong§).
- Ensure new_password remains static.
- Go to Payloads > Payload Sets > Add > Simple list (leave empty for now).

> This sets up the request template. Expected: Single payload position highlighted.

### Step 4: Load Payloads and Start Attack

**Context**: Inject wordlist passwords and execute to find the match.

No specific command; launch in Burp:

- In Payloads, load wordlist (Payload Options > Load > select file with 100+ passwords).
- Options: Grep - Extract to identify success (e.g., look for 'password changed' or absence of error).
- Click Start Attack.
- Analyze results: Sort by response length/status; the correct password yields a unique response (e.g., 200 OK).

> Once found, copy the request, replace current_password with the guessed value and new_password with attacker choice, then resubmit manually or via Repeater to change password. Expected: Confirmation of password update.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[account-takeover]]
- [[web-auth]]
- [[rate-limit-bypass]]
