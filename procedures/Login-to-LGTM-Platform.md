---
id: proc-uuid-2
tags:
  - authentication
  - session-establishment
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
updated_at: '2025-12-14T17:27:29.635Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-LGTM-Platform

## Summary

This procedure establishes an authenticated session on the LGTM platform, creating the necessary cookies for subsequent CSRF exploitation in the same browser.

## Description

The LGTM platform requires user authentication to access Account Settings and the vulnerable savePublicInformation endpoint. By logging in with valid credentials, an active session is created, allowing CSRF PoCs to leverage these cookies for authenticated requests without additional prompts. This step is crucial as the vulnerability is authenticated-only, targeting logged-in users.

## Requirements

1. Valid LGTM credentials (username/email and password)
2. Modern web browser with proxy support if using Burp
3. Direct access to https://lgtm-com.pentesting.semmle.net/

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) to prevent credential compromise
- Implement session timeouts and IP binding to limit session reuse
- Log all login events and monitor for suspicious activity from new IPs

## Objectives

1. Create active session cookies for LGTM
2. Verify access to protected areas like Account Settings
3. Prepare browser for loading CSRF PoC

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the LGTM homepage to initiate authentication.

Open browser and go to https://lgtm-com.pentesting.semmle.net/.

**Expected Output**: Login form displayed.

### Step 2: Enter Credentials and Submit

**Context**: Provide valid credentials to authenticate and establish session.

Enter username/email and password, then click login.

**Expected Output**: Redirect to dashboard with session established; check developer tools (F12 > Application > Cookies) for session tokens.

### Step 3: Verify Session

**Context**: Confirm access to Account Settings.

Navigate to Account Settings page and attempt a minor profile change to ensure full access.

**Expected Output**: Profile editable without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[web-session]]
