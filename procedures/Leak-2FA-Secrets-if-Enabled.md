---
tags:
  - 2fa-bypass
  - secret-leak
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:20.443Z'
sub_techniques: []
id: ab378788-fb98-4363-9406-28e8bb95ca1a
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
---
# Leak-2FA-Secrets-if-Enabled

## Summary

This procedure checks for and leaks 2FA configuration data, such as TOTP secrets or email token hashes, using blind injection to bypass multi-factor authentication during takeover.

## Description

If 2FA is enabled on the admin account, fields like services.totp.secret are targeted with $where oracles. Similar blind techniques extract base32 secrets or hashes, allowing code generation for TOTP or hash cracking.

## Requirements

1. Admin user with 2FA active
2. Knowledge of 2FA field names in schema
3. Tools for TOTP simulation if secret leaked

## Defense

- Encrypt 2FA secrets in DB
- Rotate secrets on suspicious activity
- Detect injection targeting auth fields

## Objectives

1. Identify 2FA presence
2. Extract secrets for bypass
3. Complete credential access

## Instructions

### Step 1: Probe for 2FA Fields

**Context**: Test if services.totp exists.

**Instructions**: $where: this.roles.includes('admin') && this.services.totp != null

> Expected: Confirmation if 2FA enabled.

### Step 2: Leak Secret

**Context**: Enumerate secret characters.

**Instructions**: Similar to token: /^A/.test(this.services.totp.secret)

> Expected: Base32 secret leaked, usable for TOTP codes.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/post-auth-nosqli-py]]

## Tags

- 2fa-leak
