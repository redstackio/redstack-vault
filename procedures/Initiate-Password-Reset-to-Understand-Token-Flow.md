---
tags:
  - recon
  - password-reset
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-password-page]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:06.582Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 49ba5728-e34e-4680-9059-bdda5b95e344
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Initiate Password Reset to Understand Token Flow

## Summary

This procedure triggers the password reset mechanism in the Instacart shopper app to analyze the token format and response flow, setting the stage for brute forcing without rate limits.

## Description

In the Instacart shopper application, the password reset endpoint lacks protections against excessive requests. By initiating a reset, attackers can inspect the 20-character reset_password_token sent via email and confirm the validation behavior, where invalid tokens return a specific error without throttling. This is a reconnaissance step to map the attack surface for subsequent brute force attempts leading to account takeover.

## Requirements

1. Access to a target email or ability to trigger reset for any account
2. HTTP client like curl or browser
3. Network connectivity to https://shoppers.instacart.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on reset endpoints (e.g., 5 attempts per IP per hour)
- Use short-lived tokens with expiration (e.g., 15 minutes)
- Monitor for anomalous request volumes to /password endpoint
- Log and alert on repeated invalid token submissions

## Objectives

1. Understand token format and length (20 characters)
2. Confirm error response for invalid tokens
3. Prepare for brute force without initial blocks

## Instructions

### Step 1: Access Reset Page

**Context**: Navigate to the password reset page to initiate the flow and observe the initial request.

**Command** ([[commands/curl-get-password-page]]):
```bash
curl -X GET https://shoppers.instacart.com/password -c cookies.txt
```

> This fetches the reset form, extracts authenticity_token from the HTML response, and sets cookies for subsequent requests. Expected output includes the form HTML with token.

### Step 2: Submit Reset Request

**Context**: POST to the reset initiation endpoint with a target email to receive the token via email.

**Command** ([[commands/curl-post-reset-initiate]]):
```bash
curl -X POST https://shoppers.instacart.com/password \
  -d "utf8=%E2%9C%93" \
  -d "authenticity_token=extracted_token" \
  -d "driver[email]=target@example.com" \
  -d "commit=Reset+password" \
  -b cookies.txt
```

> Submits the email for reset. Expected output: Confirmation message or redirect. Check email for the 20-character token in the reset link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-get-password-page]]
- [[commands/curl-post-reset-initiate]]

## Tools Used


## Tags

- [[recon]]
- [[password-reset]]
