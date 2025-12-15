---
tags:
  - password-reset
  - business-logic
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
  - '[[Password Spraying]]'
updated_at: '2025-12-14T17:32:58.342Z'
sub_techniques: []
id: 7b18d578-6994-46c6-a766-a790fae70cf3
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Password Spraying]]'
---
# Initiate Password Reset with Leaked Email

## Summary

This procedure starts the password reset by submitting a leaked email address, triggering the verification step that can be bypassed with disclosed pins.

## Description

Using PII from enumeration, the attacker inputs the email to initiate reset, exploiting the lack of safeguards in the flow.

## Requirements

1. Leaked email from prior enumeration
2. Access to reset form

## Defense

- Add email ownership verification beyond pins
- Rate limit reset initiations per IP/email

## Objectives

1. Trigger verification page
2. Advance to pin entry

## Instructions

### Step 1: Submit Email

**Context**: Enter the leaked email in the form.

Fill the email field with the obtained address and submit.

> Redirects to verification page asking for email and pin.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Password Spraying]] Password Spraying (adapted for reset abuse)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[business-logic]]
