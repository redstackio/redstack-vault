---
id: uuid-for-proc1
tags:
  - xss
  - stored-xss
  - slack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.270Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Malicious-User-Name-in-Slack

## Summary

This procedure injects a stored XSS payload into a Slack teammate's display name, leveraging insufficient sanitization to store malicious HTML/JavaScript for later execution during post sharing.

## Description

In Slack workspaces, user names are editable by admins or authorized users and stored without proper escaping. By setting a name to an XSS payload like `<img src=x onerror=alert(1)>`, the attacker prepares for payload delivery. This targets the share post menu where names are rendered in HTML without encoding, executing in the victim's browser context. Prerequisites include authenticated access and permission to edit user profiles. Expected outcome is payload storage without immediate execution, setting up for chain exploitation.

## Requirements

1. Authenticated Slack session with user profile editing permissions
2. Access to the workspace user directory
3. Web browser for manual interface navigation

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and HTML escaping for all user profile fields
- Implement Content Security Policy (CSP) to restrict inline scripts and unsafe HTML
- Monitor for unusual user name changes via audit logs and alert on suspicious patterns like script tags

## Objectives

1. Store XSS payload in user profile for persistence
2. Avoid detection during setup phase
3. Prepare for payload triggering in subsequent sharing actions

## Instructions

### Step 1: Access User Directory

**Context**: Navigate to the Slack workspace's user management to locate the target teammate.

Log in to Slack at https://app.slack.com and use the search or directory to find the user.

### Step 2: Edit User Name

**Context**: Modify the display name to include the XSS payload, ensuring it bypasses any client-side checks.

In the user profile view, select edit and set the name to `'><img src=x onerror=alert(1)>`. Save the changes.

> This stores the payload in Slack's backend, visible in profiles but not executed until rendered in a vulnerable context like the share menu.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored without triggering execution.

View the updated profile; the name should display the injected HTML literally.

**Expected Output**: Updated name visible in user list or profile without alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- slack
- user-profile
