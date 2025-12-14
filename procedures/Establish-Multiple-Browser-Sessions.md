---
tags:
  - authentication
  - session-setup
  - web
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
updated_at: '2025-12-14T17:31:42.815Z'
sub_techniques: []
id: c6e11b0b-a3ab-4aa4-b0ad-06e910ae27bd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Establish Multiple Browser Sessions

## Summary

This procedure sets up independent authentication sessions for the same account across multiple browsers, enabling testing of session management flaws in web applications.

## Description

In scenarios involving broken session invalidation, creating multiple sessions simulates concurrent user access. This is typically done using distinct browser instances to ensure session isolation via separate cookie jars and storage. The target is any web app with multi-session support, and success confirms active logins without interference.

## Requirements

1. Valid account credentials (username and password)
2. Access to at least two web browsers (e.g., Chrome and Firefox) or incognito modes
3. Direct network access to the web application's login endpoint

## Defense

Defensive measures and detection strategies:

- Implement session binding to user agents or IP addresses to limit multi-session risks
- Monitor for unusual multi-browser logins from the same account via logging

## Objectives

1. Achieve authenticated access in multiple isolated sessions
2. Prepare for testing session invalidation behaviors
3. Validate initial access without triggering anomalies

## Instructions

### Step 1: Prepare Browsers

**Context**: Select and open browsers to ensure session separation.

Open two different browsers, such as Google Chrome and Mozilla Firefox. Alternatively, use incognito/private mode in one browser alongside a regular session in another to isolate cookies and local storage.

### Step 2: Perform Logins

**Context**: Authenticate the account in each browser to establish active sessions.

Navigate to the web application's login page in both browsers. Enter the same username and password credentials. Submit the login form in each, confirming redirection to the authenticated dashboard or profile area.

**Expected Output**: Both sessions display logged-in content, such as user profile or account settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- session-setup
