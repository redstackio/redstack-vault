---
id: uuid-5
tags:
  - dos
  - lockout
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:33:12.518Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Test-Login-Lockout-Effect

## Summary

This procedure tests how triggering verification emails via enumeration locks out victim accounts, demonstrating a secondary DoS impact alongside discovery.

## Description

After enumeration, valid accounts require email verification for login, preventing access and harassing users with unwanted emails. This affects even previously verified accounts on the target site.

## Requirements

1. Enumerated valid email
2. Access to login page

## Defense

Defensive measures and detection strategies:

- Limit verification email sends per account
- Allow bypass for verified sessions
- Notify users of suspicious resend attempts

## Objectives

1. Confirm lockout mechanism
2. Amplify attack with harassment/DoS
3. Validate enumeration accuracy

## Instructions

### Step 1: Attempt Victim Login

**Context**: Try logging in with enumerated email.

Navigate to https://en.instagram-brand.com/register/signin and enter the email/password (any).

> Site prompts for verification link from email, blocking login.

### Step 2: Observe Effects

**Context**: Check for lockout and email trigger.

Monitor if verification email was sent and login is denied.

> Lockout confirmed if access requires unclicked link.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- lockout
