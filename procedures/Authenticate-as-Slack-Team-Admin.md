---
id: proc-uuid-1
name: Authenticate as Slack Team Admin
tags:
  - authentication
  - slack
  - initial-access
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
updated_at: '2025-12-14T17:28:44.784Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate as Slack Team Admin

## Summary

This procedure establishes an authenticated session in the Slack web application using team admin credentials, enabling subsequent API interactions for privilege escalation.

## Description

In the context of exploiting Slack's team settings API, authentication as a team admin provides the necessary session state (cookies and token) to attempt unauthorized modifications. This step assumes valid admin credentials and targets the Slack web login endpoint. Expected outcome is a valid session without triggering additional MFA if not enforced.

## Requirements

1. Valid Slack team admin username and password
2. Web browser or HTTP client (e.g., curl with cookie jar)
3. Network access to app.slack.com

## Defense

Defensive measures and detection strategies:

- Enforce MFA for all admin accounts
- Monitor login events for unusual IP locations
- Rate-limit authentication attempts

## Objectives

1. Obtain authenticated session with admin privileges
2. Capture session cookies and API token
3. Prepare for API-based privilege escalation

## Instructions

### Step 1: Access Slack Login Page

**Context**: Navigate to the Slack login to initiate authentication.

No command needed; use browser to visit https://app.slack.com/signin and enter admin credentials.

> Successful login redirects to the team dashboard.

### Step 2: Capture Authentication Artifacts

**Context**: Extract session details for API use.

Use browser developer tools (Network tab) to inspect requests and copy cookies (e.g., 'd' session cookie) and 'xoxs-' token from local storage.

> Expected output: Valid cookie string and token for subsequent requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- slack
- initial-access
