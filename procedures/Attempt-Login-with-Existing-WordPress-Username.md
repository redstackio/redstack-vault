---
tags:
  - user-enumeration
  - wordpress
  - login
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4ce79d6f-fc32-4e6a-9d56-b19668d10633
created_at: '2025-12-14T17:28:36.664Z'
updated_at: '2025-12-14T17:28:36.664Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Attempt-Login-with-Existing-WordPress-Username

## Summary

This procedure simulates a failed login attempt using a valid WordPress username and incorrect password to elicit a specific error message that confirms the username's existence on the system.

## Description

In WordPress, the wp-admin login page differentiates between valid and invalid usernames through error messages. By submitting a login with a known or suspected valid username and wrong password, attackers can confirm active accounts. This is part of a broader user enumeration attack, though WordPress considers usernames public information, making this low-impact. The procedure targets the authentication endpoint and relies on observing HTTP responses or page content.

## Requirements

1. Access to a web browser
2. URL of the WordPress wp-admin login page (e.g., https://target.com/wp-admin)
3. A suspected valid username (common defaults like 'admin')

## Defense

Defensive measures and detection strategies:

- Implement consistent error messages (e.g., always show "Invalid username or password")
- Enable rate limiting on login attempts to prevent enumeration
- Monitor login logs for patterns of username probing

## Objectives

1. Confirm the existence of a specific username
2. Collect evidence of valid accounts for further reconnaissance
3. Differentiate from invalid username responses

## Instructions

### Step 1: Access the Login Page

**Context**: Navigate to the WordPress administration login interface to prepare for the authentication attempt.

Open a web browser and go to the target site's wp-admin URL, such as `https://target.com/wp-admin`.

> This loads the login form where username and password can be entered.

### Step 2: Submit Invalid Login

**Context**: Enter a valid username with an incorrect password to trigger the targeted error.

Fill in the username field with a suspected valid username (e.g., 'admin') and any incorrect password (e.g., 'wrongpass'). Click the login button or submit the form.

> The server responds with an error page. For valid usernames, expect: "ERROR: The password you entered for the username admin is incorrect."

### Step 3: Capture and Analyze Response

**Context**: Inspect the error message to validate the username.

View the resulting page or use browser developer tools (F12) to check the response body for the specific error text.

> Successful output confirms the username is valid if the message references the username directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[user-enumeration]]
- [[wordpress]]
- [[authentication]]
