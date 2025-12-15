---
id: proc-uuid-1
tags:
  - csrf
  - web
  - token-extraction
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.697Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Establish Slack Session and Extract CSRF Token

## Summary

This procedure logs into a Slack account, navigates to the account settings page, and extracts the anti-CSRF crumb token using browser tools, setting up for token reuse exploitation.

## Description

In the context of exploiting Slack's CSRF flaw, this step establishes a legitimate session and captures the crumb token, which is a hidden form field value used for CSRF protection. The token is tied to session cookies but fails to expire on logout, enabling later bypass. This is performed manually in a browser on the web platform, targeting URLs like https://sehacure.slack.com/account/settings. Expected outcome: Token captured for reuse, no server-side detection as it's legitimate access.

## Requirements

1. Valid Slack account credentials
2. Modern web browser with developer tools (e.g., Chrome, Firefox)
3. Internet access to Slack workspace

## Defense

Defensive measures and detection strategies:

- Implement token expiration on logout and session invalidation
- Monitor for unusual form submissions from known sessions
- Use Content Security Policy (CSP) to limit dev tools interference

## Objectives

1. Gain initial access to account settings
2. Capture reusable CSRF token
3. Prepare for session manipulation

## Instructions

### Step 1: Login to Slack

**Context**: Authenticate to create a session.

Open browser, navigate to https://app.slack.com, enter username and password, and complete login.

> Successful login redirects to workspace dashboard.

### Step 2: Navigate to Account Settings

**Context**: Access the vulnerable page.

Click user menu > Account Settings or directly visit https://sehacure.slack.com/account/settings.

> Page loads with form elements including crumb token.

### Step 3: Extract Crumb Token

**Context**: Inspect and copy the token for reuse.

Right-click form > Inspect Element, find <input name="crumb" value="...">, copy the value attribute.

> Token string copied, e.g., a long alphanumeric value.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[csrf]]
- [[web]]
- [[token-extraction]]
