---
tags:
  - xss
  - injection
  - web
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:10.210Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 11825f3a-e1f1-424a-9105-423cc2ba609f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Admin-Email-Field

## Summary

This procedure demonstrates injecting a JavaScript payload into the email field of Revive Adserver's admin preferences, exploiting lack of input sanitization to store the script persistently for later execution by other admins.

## Description

In Revive Adserver, the admin preferences email field accepts user input without proper HTML/JS escaping, allowing stored XSS. An attacker with one admin account can inject a payload like `<script>alert('xss');</script>`, which is saved to the database and displayed unsanitized on the Inventory > Admin Access page. When another admin views this page, the script executes in their browser context, potentially stealing sessions, logging keystrokes, or hooking into frameworks like BeEF. This targets web-based ad server environments and requires admin privileges but no advanced tools.

## Requirements

1. Valid admin credentials for the target Revive Adserver instance
2. Access to the web interface via a browser like Firefox
3. No additional network privileges beyond HTTP access

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., htmlspecialchars) when displaying user input in HTML contexts
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor admin logs for unusual email field modifications and JavaScript patterns

## Objectives

1. Store malicious JavaScript in the admin email field
2. Ensure persistence across sessions and users
3. Set up for cross-admin exploitation

## Instructions

### Step 1: Login as Primary Admin

**Context**: Authenticate to gain access to the preferences section.

Use Firefox to navigate to the Revive Adserver login page and enter admin1 credentials.

**Expected Output**: Redirect to the admin dashboard.

### Step 2: Navigate to Preferences and Inject Payload

**Context**: Access the email change form and insert the XSS payload.

Navigate to Configuration > Preferences > Change E-mail. Enter the current password, then set the Email address to `admin1@example.com<script>alert('xss');</script>`. Click Save changes.

> This injects the script without triggering immediate execution due to stored nature.

**Expected Output**: Success message confirming email update.

### Step 3: Logout to Confirm Storage

**Context**: End the session to verify the payload persists.

Log out from the admin account.

**Expected Output**: Logout confirmation, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- stored-xss
- injection
