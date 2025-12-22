---
id: proc-uuid-001
tags:
  - initial-access
  - account-creation
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:25:23.145Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Account-Creation-for-Initial-Access

## Summary

This procedure involves creating a standard user account on the target DoD-affiliated website to establish an authenticated session, enabling access to member features necessary for subsequent IDOR exploitation.

## Description

In the context of exploiting an IDOR vulnerability, initial access is gained by registering a new account on the website. This provides the necessary authentication tokens and session cookies to interact with endpoints that handle user connections and profiles. The target environment is a web-based member portal where user IDs are sequential and predictable, allowing escalation to unauthorized data access. Prerequisites include a valid email address for verification and basic web navigation skills. Expected outcomes include a functional account with permissions to view and request connections from other members.

## Requirements

1. Internet access to the target website (https://█████████)
2. Valid email for account verification
3. Web browser or proxy tool like Burp Suite for session management

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification on signup to prevent automated account creation
- Monitor for unusual signup patterns from single IPs
- Rate-limit new account interactions with sensitive endpoints

## Objectives

1. Establish authenticated access to member features
2. Obtain session cookies and authorization codes
3. Prepare for user enumeration and request sending

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Access the registration form to input user details.

No specific command; use a web browser to visit the signup endpoint and fill in fields like email, username, and password.

> Upon submission, expect an email verification link. Click it to activate the account.

### Step 2: Login and Verify Session

**Context**: Authenticate to confirm access and capture session details.

Use Burp Suite to intercept the login POST request and note the Authorization-Code and Rest-Authorization-Code headers (e.g., b6315c0b-3f28-4b63-93de-b6a5a1c3db82).

> Successful login redirects to the dashboard with cookies like UserName=█████ █████.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[initial-access]]
- [[web]]
