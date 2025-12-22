---
id: proc-uuid-2
tags:
  - account-closure
  - token-extraction
  - csrf
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T05:32:13.714Z'
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
# Close-Account-and-Extract-Tokens

## Summary

This procedure closes a newly created account and extracts CSRF tokens and session cookies from a failed login attempt, enabling request replay with seemingly valid but unauthorized credentials.

## Description

Targeting applications with flawed post-closure authentication, this step simulates de-authentication while preserving session artifacts. It applies to Rails apps where account status isn't checked in upload endpoints. Outcomes include tokens for bypassing CSRF and session validation in subsequent requests.

## Requirements

1. Active account from previous creation step
2. Burp Suite intercepting login traffic
3. Knowledge of account credentials

## Defense

Defensive measures and detection strategies:

- Invalidate all sessions immediately upon account closure
- Log and alert on login attempts to closed accounts
- Enforce account status checks in all API endpoints

## Objectives

1. Transition account to closed state without session cleanup
2. Harvest CSRF token and cookie from denied login
3. Prepare for authentication bypass in upload flows

## Instructions

### Step 1: Close the Account

**Context**: Deactivate the account via settings.

Navigate to account settings and close the newly created account.

### Step 2: Attempt Login and Intercept

**Context**: Force token generation despite denial.

Login with closed credentials at https://app.hey.com/, intercept response for X-CSRF-Token and Cookie.

**Expected Output**: Access denied page with meta tag containing CSRF token and Set-Cookie header.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-closure
- token-extraction
- csrf
