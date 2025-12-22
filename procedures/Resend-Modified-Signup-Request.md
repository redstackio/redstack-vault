---
id: proc-slack-resend-001
tags:
  - request-forgery
  - slack
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:30:47.022Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Resend-Modified-Signup-Request

## Summary

This procedure forwards the tampered HTTP request to Slack's signup endpoint, completing the unauthorized join to the target workspace if no admin approval is required.

## Description

After modification, resending the request to `api/signup.createUser` exploits the improper authentication, creating a user account in the arbitrary workspace. The request includes the forged team ID, bypassing checks. This works only for open-invitation workspaces. Prerequisites: Modified request in proxy. Outcome: Successful workspace access, but Slack fixed this vulnerability promptly with no reported impacts.

## Requirements

1. Modified request ready in proxy
2. Valid user details (email, password) in request
3. Target workspace without admin invite approval

## Defense

Defensive measures and detection strategies:

- Require admin approval for all invites
- Rate-limit signup requests per IP/email
- Audit logs for anomalous team ID usages

## Objectives

1. Submit the altered request to server
2. Achieve unauthorized account creation
3. Gain access to target workspace

## Instructions

### Step 1: Forward Request

**Context**: Release the intercepted request.

In the proxy, click 'Forward' to send the modified POST to Slack.

**Expected Output**: Server response, e.g., 200 OK with user creation confirmation.

### Step 2: Verify Access

**Context**: Confirm successful join.

Check email for confirmation or log into Slack with new credentials to see the workspace.

**Expected Output**: Workspace appears in account, access granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-forgery]]
- [[slack]]
