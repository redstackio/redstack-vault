---
tags:
  - account-setup
  - hackerone
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:48.110Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a984469f-cd48-4bd5-98fd-6e156cfd5ea5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-HackerOne-Accounts-and-Tags

## Summary

This procedure establishes the foundational environment for an IDOR attack on HackerOne by creating separate attacker and victim accounts, adding scope assets, and having the victim create a custom tag to target.

## Description

In the context of exploiting an IDOR in HackerOne's tag management, this setup simulates a multi-account scenario where the attacker prepares to probe the victim's data. It requires no special privileges, only the ability to register accounts on the public-facing platform. The outcome is a controlled environment where the victim's custom tag exists for later unauthorized access via bruteforcing.

## Requirements

1. Access to a web browser for account registration
2. Email addresses for two separate accounts (attacker and victim simulation)
3. No VPN or special network needed; direct internet access suffices

## Defense

Defensive measures and detection strategies:

- Implement account creation rate limiting to prevent bulk registrations
- Monitor for suspicious multi-account activity tied to the same IP
- Require email verification and CAPTCHA on sign-ups

## Objectives

1. Create isolated attacker and victim profiles on HackerOne
2. Add scope assets to enable tag assignments
3. Introduce a target custom tag in the victim account

## Instructions

### Step 1: Register Accounts

**Context**: Create two distinct user accounts to separate attacker and victim contexts, ensuring no cross-contamination.

Navigate to https://hackerone.com and register the first account as the attacker using one email. Repeat for the victim account with a different email.

**Expected Output**: Confirmation emails sent; accounts accessible via login.

### Step 2: Add Scope Assets

**Context**: Scope assets (e.g., programs or domains) are required for tag assignments in later steps.

Log in to each account, go to the dashboard, and add a sample scope asset like a dummy domain or program.

**Expected Output**: Assets listed in the dashboard for both accounts.

### Step 3: Create Victim Custom Tag

**Context**: The victim must create a custom tag to serve as the disclosure target.

In the victim account, navigate to tag management (under assets or programs) and create a new custom tag, e.g., "sensitive-victim-tag".

**Expected Output**: New tag appears in the victim's tag list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-setup
- hackerone
