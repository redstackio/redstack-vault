---
tags:
  - pin-bypass
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.341Z'
sub_techniques: []
id: b6e0f87f-147a-46d9-bfca-39727c141a2a
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
---
# Verify Reset with Leaked Pin

## Summary

This procedure bypasses the verification step by entering the leaked security pin, exploiting the weak protection in the reset flow.

## Description

The pin, disclosed via the endpoint, is re-entered without additional checks, allowing unauthorized verification.

## Requirements

1. Leaked pin matching the email
2. Verification page loaded

## Defense

- Use time-limited or one-time pins sent via secure channels
- Implement secondary factors like SMS to mobile (from PII)

## Objectives

1. Pass verification
2. Reach password change

## Instructions

### Step 1: Enter Pin

**Context**: Input the pin on the verification form.

Re-enter email and pin (e.g., 1234), then submit.

> System validates and proceeds if matched.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[pin-bypass]]
- [[credential-access]]
