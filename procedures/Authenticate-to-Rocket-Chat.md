---
id: proc-rocket-auth-001
name: Authenticate-to-Rocket-Chat
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.270Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
tags:
  - authentication
  - initial-access
  - rocket-chat
platforms:
  - Web
tools:
  - '[[tools/Browser-Web-Inspector]]'
commands: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Authenticate-to-Rocket-Chat

## Summary

This procedure establishes an authenticated session in Rocket.Chat, a prerequisite for accessing messaging features and exploiting vulnerabilities like CSS injection in custom avatars.

## Description

Rocket.Chat is a web-based team communication platform built on Meteor.js. Authentication involves standard username/password or OAuth login, granting access to rooms and direct messages. This step is essential for any authenticated attack, such as injecting malicious payloads via the sendMessage method. The target environment is a web browser accessing the Rocket.Chat instance over HTTPS. Expected outcomes include a valid session cookie enabling API calls like Meteor.call.

## Requirements

1. Valid username and password for a Rocket.Chat user account
2. Web browser with JavaScript enabled (e.g., Chrome, Firefox)
3. Network access to the Rocket.Chat server (typically port 443)

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) to limit impact of stolen credentials
- Monitor login attempts for anomalies using Rocket.Chat's audit logs
- Use web application firewalls (WAF) to detect unusual authentication patterns

## Objectives

1. Establish a persistent authenticated session
2. Gain access to chat rooms or direct messages
3. Enable execution of authenticated API methods like sendMessage

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the Rocket.Chat instance to begin authentication.

No specific command; use browser navigation to the Rocket.Chat URL (e.g., https://chat.example.com).

> Enter the login endpoint and provide credentials. Expected output: Login form loads.

### Step 2: Submit Credentials

**Context**: Authenticate using provided username and password.

No command; fill in the form fields and submit.

> Upon success, redirect to the main interface. Expected output: Dashboard with user menu visible.

### Step 3: Verify Session

**Context**: Confirm authentication by accessing a chat room.

Use the browser's Web Inspector to check for session tokens in cookies or local storage.

> Expected output: Active session indicators like user ID in console (e.g., Meteor.userId()).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Browser-Web-Inspector]]

## Tags

- [[authentication]]
- [[initial-access]]
- [[rocket-chat]]
