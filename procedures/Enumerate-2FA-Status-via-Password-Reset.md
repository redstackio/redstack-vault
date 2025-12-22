---
tags:
  - user-enumeration
  - 2fa-enumeration
  - business-logic
  - password-reset
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.390Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6c37e2e5-690c-40ea-9998-c6966ff012b8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate-2FA-Status-via-Password-Reset

## Summary

This procedure exploits a business logic vulnerability in the password reset flow to enumerate whether specific users have two-factor authentication (2FA) enabled, by observing differences in the reset prompts without uniform error handling.

## Description

In vulnerable web applications, the password reset process checks for 2FA enablement early in the flow. If 2FA is active, it prompts for a second factor after initial verification; otherwise, it skips to password update. This leaks sensitive security configuration information, allowing attackers to identify users with weaker protection (no 2FA) for targeted attacks like phishing or brute-force. The technique relies on manual or automated submission of reset requests for known or guessed email addresses, observing response branches. While rate-limiting may slow enumeration, it does not prevent inference from small-scale tests. This was demonstrated in Legal Robot's implementation during testing of new 2FA options.

## Requirements

1. Access to the public password reset endpoint (e.g., via browser or HTTP client)
2. List of target email addresses (from prior reconnaissance or public sources)
3. Basic understanding of web request flows (no advanced tools required)

## Defense

Defensive measures and detection strategies:

- Implement uniform responses in password reset flows (e.g., always show generic 'check your email' without 2FA hints)
- Enforce strict rate-limiting on reset requests per IP/email
- Log and monitor anomalous reset attempts for patterns indicating enumeration

## Objectives

1. Infer 2FA enablement status for target users
2. Identify users without 2FA for potential follow-on exploitation
3. Assess the application's security configuration exposure

## Instructions

### Step 1: Prepare Target Emails

**Context**: Compile a list of emails to test, ensuring they are valid formats for the target domain.

No specific command; manually create a file like `emails.txt` with one email per line, e.g.,
```
target1@example.com
target2@example.com
```

### Step 2: Initiate Reset Requests

**Context**: Submit password reset for each email to trigger the flow.

Use a browser to visit the forgot-password page and enter emails one by one, or automate with curl:

**Command** ([[commands/curl-password-reset]]):
```bash
for email in $(cat emails.txt); do
  curl -X POST https://target.com/forgot-password \
    -H "Content-Type: application/json" \
    -d "{\"email\": \"$email\"}" \
    -c cookies.txt -b cookies.txt
  echo "Reset for $email completed"
done
```

> This loops through emails, sending POST requests to initiate reset. Capture cookies for session continuity. Expected output: HTTP 200/302 with reset initiation message.

### Step 3: Analyze Flow Responses

**Context**: Follow or inspect the post-reset prompts to detect 2FA branching.

After submission, in browser: If 2FA enabled, expect a prompt like 'Enter your 2FA code'; if not, direct to 'Set new password'. For API inspection:

**Command** ([[commands/curl-reset-verify]]):
```bash
curl -X POST https://target.com/reset-verify \
  -H "Content-Type: application/json" \
  -d "{\"token\": \"reset_token\", \"code\": \"123456\"}" \
  -b cookies.txt
```

> Check response body for 2FA challenge (e.g., JSON field 'requires_2fa: true') or direct password set endpoint. Log differences to infer status.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[user-enumeration]]
- [[2fa-enumeration]]
- [[business-logic]]
- [[password-reset]]
