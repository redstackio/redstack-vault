---
id: proc-uuid-4
name: Logout-from-Web-Application
tags:
  - logout
  - session-management
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T00:11:09.574Z'
sub_techniques: []
validated: true
---
# Logout-from-Web-Application

## Summary

This procedure terminates the authenticated session after payload injection to isolate the attack and prepare for CSRF exploitation.

## Description

Standard logout clears session cookies, ensuring the attacker isn't logged in when the CSRF forces victim authentication. Targets apps with simple logout endpoints.

## Requirements

1. Active session
2. Access to logout button or URL

## Defense

Defensive measures and detection strategies:

- Secure logout with token invalidation
- Log session terminations
- Prevent concurrent sessions

## Objectives

1. End current session
2. Reset for CSRF testing
3. Avoid interference

## Instructions

### Step 1: Initiate Logout

**Context**: Clear authentication state.

Click 'Logout' or visit /logout endpoint.

> Session cookie removed; redirect to login.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- logout
- session-management
