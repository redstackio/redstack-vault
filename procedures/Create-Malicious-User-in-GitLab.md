---
id: 123e4567-e89b-12d3-a456-426614174001
name: Create-Malicious-User-in-GitLab
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.513Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - gitlab
  - user-creation
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Create-Malicious-User-in-GitLab

## Summary

This procedure creates a GitLab user account with a username containing a persistent XSS payload, which is stored without sanitization and later rendered in UI components like protected branches dropdowns.

## Description

In GitLab, usernames are not properly escaped when displayed in certain JavaScript-rendered dropdowns. By creating a user with a payload like `<img src=x onerror=alert(document.domain)> foo / bar`, the attacker injects HTML and JavaScript that persists across sessions. This targets the protected branches feature, where the username appears in role selection lists, leading to execution when viewed by project members. Prerequisites include admin access or invitation rights; the attack assumes the instance lacks username validation for scripts.

## Requirements

1. GitLab account with admin or maintainer privileges to create users
2. Access to the GitLab web interface
3. No additional tools needed beyond a standard browser

## Defense

Defensive measures and detection strategies:

- Implement strict username validation to block HTML/JS characters
- Use output encoding (e.g., _.escape() from Underscore.js) in all UI renders
- Monitor for anomalous user creations with suspicious strings

## Objectives

1. Inject persistent XSS payload into user data
2. Ensure payload survives storage and retrieval
3. Set up for later execution in project settings

## Instructions

### Step 1: Log In and Navigate to User Creation

**Context**: Access the admin area to create a new user account.

Log in to GitLab and go to Admin Area > Users > New User.

### Step 2: Set Malicious Username

**Context**: Enter the XSS payload as the username to inject the script.

In the username field, input: `<img src=x onerror=alert(document.domain)> foo / bar`. Complete other fields (e.g., name, email) with benign values and submit.

> The payload uses an img tag with onerror to execute JS if the src fails, alerting the domain to prove execution.

### Step 3: Verify User Creation

**Context**: Confirm the user is created and the username is stored as-is.

Check the user list or profile to ensure the username displays with the injected HTML intact.

**Expected Output**: New user appears in the list with the full malicious string visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[gitlab]]
- [[user-creation]]
