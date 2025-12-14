---
id: proc-404797-setup-accounts
tags:
  - authentication
  - access-setup
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
updated_at: '2025-12-14T17:25:34.459Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup Restaurant Manager Accounts

## Summary

This procedure establishes authenticated sessions for multiple Zomato restaurant manager accounts, providing the foundation for testing cross-restaurant access controls in photo management.

## Description

In the context of exploiting an IDOR vulnerability, authenticated access as a restaurant manager is required to interact with the photo deletion endpoint. This step involves logging into two separate accounts to simulate an attacker with access to multiple stores, allowing subsequent manipulation of requests across different res_id values. The target environment is Zomato's web application, where manager privileges enable access to /clients/manage_photos.php. Expected outcomes include active sessions with capturable cookies for request replay.

## Requirements

1. Valid login credentials for at least two Zomato restaurant accounts with manager privileges
2. Browser or proxy tool for session management and cookie capture
3. Network access to www.zomato.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for manager accounts to prevent credential compromise
- Monitor for unusual login patterns from multiple accounts in short succession
- Use session binding to IP or device to limit cookie reuse

## Objectives

1. Secure authenticated access to restaurant manager interfaces
2. Capture session artifacts (e.g., cookies) for request authentication
3. Enable switching between accounts without re-authentication

## Instructions

### Step 1: Login to First Restaurant Account

**Context**: Initiate authentication for the primary account to establish a baseline session.

Log in via https://www.zomato.com using the first restaurant's manager credentials. Navigate to /clients/manage_photos.php to confirm privileges.

**Expected Output**: Successful access to photo management page; session cookies like PHPSESSID visible in developer tools.

### Step 2: Login to Second Restaurant Account

**Context**: Create a separate session for the target account used in exploitation.

Repeat the login process with the second account's credentials, ensuring cookies are isolated (e.g., use incognito or clear cache). Verify access to manage_photos.php.

**Expected Output**: Independent session established; cookies captured for both accounts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- session-management
