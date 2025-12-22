---
id: proc-002
tags:
  - jwt
  - token-generation
type: procedure
tools:
  - '[[tools/token-dev]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.872Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate-Unsigned-JWT-Token

## Summary

This procedure crafts an unsigned JSON Web Token (JWT) with custom payload, such as a target email, to exploit endpoints that fail to verify signatures in the Newspack Extended Access plugin.

## Description

The plugin's /wp-json/newspack-extended-access/v1/google/register endpoint accepts JWTs without signature validation (as per class-rest-controller.php lines 81-87), allowing attackers to forge tokens for auth bypass or registration. Use an online tool to set payload fields like 'email' without signing.

## Requirements

1. Target email address (for hijack) or arbitrary details (for new account)
2. Access to [[tools/token-dev]]
3. Basic JSON knowledge for payload

## Defense

Defensive measures and detection strategies:

- Enforce JWT signature verification in all plugins
- Log and alert on unsigned token attempts

## Objectives

1. Create valid-looking but unsigned JWT
2. Embed attacker-controlled data
3. Enable submission for bypass

## Instructions

### Step 1: Access Token Generator

**Context**: Navigate to the tool and prepare payload.

**Command** (Tool Interaction):

Visit https://token.dev, select JWT generation, set algorithm to HS256 (but don't sign).

> Input payload: {"email": "target@example.org", "sub": "1234567890", "iat": 1713666649, "exp": 1713670249}. Expected output: Encoded token string without valid signature.

### Step 2: Copy Token

**Context**: Extract the full token for use in submission.

**Command** (Manual Copy):

Copy the generated token from the tool's output field.

> Expected output: String like "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZW1haWwiOiJ0YXJnZXRAZXhhbXBsZS5vcmciLCJpYXQiOjE3MTM2NjY2NDksImV4cCI6MTcxMzY3MDI0OX0.invalid".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/token-dev]]

## Tags

- jwt
- token-generation
