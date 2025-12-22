---
id: proc-uuid-123
name: Intercept-and-Brute-Force-Password-Change-Request
tags:
  - brute-force
  - web-exploit
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:33:06.417Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Intercept-and-Brute-Force-Password-Change-Request

## Summary

This procedure exploits the lack of rate limiting on the current password verification endpoint during password changes on Reddit, allowing an attacker to intercept the change password request and use automated brute-force to guess the current password, resulting in account takeover.

## Description

The attack targets the POST /change_password endpoint on reddit.com and vip.reddit.com, where the current_password parameter is verified without restrictions on attempt frequency. By intercepting the request with a proxy tool like Burp Suite and configuring an Intruder attack with a password wordlist, an attacker can rapidly test multiple guesses. In a real-world scenario, this could be combined with session hijacking or CSRF to target a victim's account. The procedure assumes initial session access for demonstration but enables takeover by changing the password upon successful guess. Expected outcome: Password reset to attacker-controlled value in under 100 attempts for weak passwords.

## Requirements

1. Burp Suite installed and configured as a proxy for browser traffic.
2. Active session on the target account (via login for testing; in attack, obtain via phishing or other means).
3. Wordlist file with potential passwords (e.g., rockyou.txt subset of 100 entries).
4. Network access to reddit.com over HTTPS.

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 attempts per minute per IP/session) on password verification endpoints.
- Add CAPTCHA or multi-factor authentication (MFA) after failed attempts.
- Monitor for anomalous request volumes to /change_password from single sources.
- Use session binding and CSRF tokens to prevent unauthorized form submissions.

## Objectives

1. Intercept and analyze the password change request to identify the vulnerable parameter.
2. Automate brute-force testing of the current_password field.
3. Achieve account takeover by successfully verifying and changing the password.

## Instructions

### Step 1: Prepare and Intercept the Request

**Context**: Fill the password change form with an incorrect current password and matching new passwords, then submit via proxied browser to capture the request.

**Instructions**: Navigate to https://www.reddit.com/change_password, enter incorrect value in current_password (e.g., "wrong"), matching new passwords (e.g., "new1"), and click save with Burp proxy active.

> The intercepted POST request will include parameters like current_password=wrong&new_password=new1&confirm_password=new1. Forward it to observe the "Incorrect password" response, confirming no rate limit.

### Step 2: Send to Intruder and Configure Payload

**Context**: Transfer the request to Burp Intruder and mark the current_password for substitution to enable brute-force.

**Instructions**: Right-click the request in Burp Proxy, select "Send to Intruder". In Intruder, clear positions, then select the current_password value and add payload markers (§).

> Configuration ensures only current_password varies; set payload type to "Simple list" and load wordlist (e.g., passwords.txt with 100 lines).

### Step 3: Launch the Brute-Force Attack

**Context**: Execute the attack to test passwords rapidly and identify the correct one based on response differences.

**Instructions**: In Intruder, click "Start attack". Review responses: Look for absence of "Incorrect password" error or a success indicator (e.g., 200 OK without error).

> Successful guess (e.g., in 101st attempt) allows password change, granting takeover. Stop attack upon success and resubmit with correct guess to complete.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques

- [[Password Guessing]]

## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[account-takeover]]
- [[rate-limiting-bypass]]
