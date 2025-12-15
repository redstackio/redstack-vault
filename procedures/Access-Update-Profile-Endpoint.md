---
tags:
  - profile-access
  - web
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
id: 745aecfb-5bbc-44f8-ad6c-6f0effd1dfa5
created_at: '2025-12-14T17:25:34.286Z'
updated_at: '2025-12-14T17:25:34.286Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Update-Profile-Endpoint

## Summary

This procedure details logging into the DoD platform and navigating to the Update Profile section to expose the vulnerable URL parameter for IDOR exploitation.

## Description

After account creation, authenticated users can access profile management features. The Update Profile endpoint uses a URL structure with a numeric user-id parameter that lacks proper server-side validation. This step identifies the endpoint and confirms access with the attacker's own ID before manipulation. The scenario targets web sessions over HTTPS, with outcomes including visibility of the exploitable parameter.

## Requirements

1. Valid authenticated session from prior account creation
2. Web browser with cookies enabled
3. Knowledge of the dashboard navigation

## Defense

Defensive measures and detection strategies:

- Enforce session timeouts and monitor for unusual profile access patterns
- Log all endpoint requests with user ID comparisons
- Use referer checks to prevent direct URL access

## Objectives

1. Confirm authenticated access to profile features
2. Identify the user-id parameter in the URL
3. Prepare for parameter manipulation in the next step

## Instructions

### Step 1: Log In and Navigate to Profile

**Context**: Use credentials to access the main dashboard and locate the profile update link.

Log in at the DoD login page, then click on "Update Profile" or similar in the user menu.

> The page loads at https://www.███████/JOINOnline/UpdateProfile/<user-id>, displaying your own profile details.

### Step 2: Inspect URL and Page

**Context**: Examine the endpoint to note the numeric user-id for later manipulation.

Use browser developer tools (F12) to inspect the network requests or simply copy the URL from the address bar.

> Expected output: URL with your assigned ID (e.g., 12345), and profile form showing editable fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[profile-access]]
- [[authentication]]
