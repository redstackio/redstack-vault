---
tags:
  - authentication
  - valid-accounts
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:01.565Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
id: 3bd301b4-babd-48c4-9686-11ef79d1bbc9
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Unauthorized-User-in-Rocket-Chat

## Summary

This procedure logs in to a Rocket.Chat instance using credentials of an account without access to the target private room, establishing a session for exploitation.

## Description

Using a low-privilege account (e.g., Trudy), authenticate to the Rocket.Chat web application to obtain a session token. This simulates an insider or compromised user who can access public rooms but not private ones. The session enables API calls to the vulnerable endpoint while respecting ACL for direct access.

## Requirements

1. Valid credentials for an unauthorized user account
2. Network access to the Rocket.Chat login endpoint
3. Browser or API client for session management

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all users
- Monitor login patterns for anomalous sessions

## Objectives

1. Obtain an authenticated session as an unauthorized user
2. Confirm access to public rooms only
3. Prepare for API-based exploitation

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the Rocket.Chat login interface.

**Instructions**: Open the Rocket.Chat URL in a browser and click login.

### Step 2: Enter Credentials and Authenticate

**Context**: Submit credentials for the unauthorized account to establish the session.

**Instructions**: Input username/email and password for Trudy, then submit. Upon success, note the auth token from localStorage or cookies (e.g., via dev tools: localStorage.getItem('Meteor.loginToken')).

**Expected Output**: Redirect to dashboard with access to public channels like GENERAL.

### Step 3: Verify Access Restrictions

**Context**: Test that private rooms are inaccessible.

**Instructions**: Attempt to join or view the target private room; expect denial.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used


## Tags

- authentication
- valid-accounts
