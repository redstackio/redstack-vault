---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - account-takeover
  - login-completion
  - 2fa-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.200Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Identify Correct OTP and Complete Login

## Summary

This procedure analyzes Intruder results to pinpoint the successful OTP based on HTTP 302 responses, then completes the login to gain full account access.

## Description

After brute-forcing, the correct mfaToken triggers a 302 redirect (unlike 200/303 for failures). Refreshing the browser 2FA page allows manual submission of the identified code, bypassing the need for real-time TOTP generation and achieving unauthorized entry to sensitive SingleStore resources.

## Requirements

1. Completed Intruder attack results
2. Active browser session
3. Identified OTP value (e.g., from request #142)

## Defense

Defensive measures and detection strategies:

- Log successful 2FA after multiple failures
- Alert on logins from unusual contexts (e.g., after held sessions)

## Objectives

1. Confirm the valid OTP via response indicators
2. Finalize authentication for dashboard access
3. Access sensitive data and perform actions

## Instructions

### Step 1: Analyze Responses

**Context**: Review Intruder output for success signals.

Sort by status code in the results table; look for 302 on the first correct hit (subsequent may also 302).

> Example: Request 142 or payload 166236 indicates the OTP.

### Step 2: Refresh and Submit

**Context**: Use the found OTP to log in.

Return to browser, refresh 2FA page, enter the correct code, and submit.

> Expected: 302 redirect to /dashboard or similar, granting full access.

### Step 3: Verify Access

**Context**: Confirm takeover.

Navigate portal features to view sensitive data.

> Success: Unrestricted account control.

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

- [[account-takeover]]
- [[2fa-bypass]]
