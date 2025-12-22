---
id: proc-uuid-001
tags:
  - recon
  - request-capture
  - slack
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Firefox-DevTools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:35.464Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Capture-Slack-Workspace-Creation-Request

## Summary

This procedure captures the HTTP POST request payload used to create a workspace on slack.com, enabling later modification for exploitation in related environments like GovSlack.

## Description

In the context of authentication bypass attacks on Slack variants, this step involves using a web browser to simulate workspace creation on the standard slack.com platform. By leveraging browser developer tools, the exact request structure—including headers, multipart/form-data body, and parameters—is extracted as a JavaScript fetch snippet. This payload can then be replayed against restricted endpoints. Prerequisites include internet access and no existing Slack account restrictions. Expected outcome is a reusable request template that bypasses domain-specific validations when modified.

## Requirements

1. Firefox browser installed
2. Access to slack.com without account blocks
3. Developer Tools enabled in browser

## Defense

Defensive measures and detection strategies:

- Monitor for unusual request captures in browser sessions on staging sites
- Implement rate limiting on signup endpoints to detect scripted replays
- Use client-side fingerprinting to block automated DevTools usage

## Objectives

1. Extract authentic workspace creation payload from slack.com
2. Prepare for request modification in bypass scenarios
3. Validate payload integrity for replay

## Instructions

### Step 1: Log In and Navigate to Workspace Creation

**Context**: Create a new user session on slack.com to access the signup flow.

Open Firefox and navigate to slack.com. Sign up as a new user if needed, then proceed to the "Create a workspace" option under get-started.

**Expected Output**: Workspace creation form loaded.

### Step 2: Capture Request with DevTools

**Context**: Intercept the POST request during submission to obtain the fetch code.

Open Firefox DevTools (F12), go to the Network tab, submit the workspace creation form, locate the /api/signup.createTeam request, right-click, and select "Copy as Fetch".

**Expected Output**: JavaScript code snippet for the POST request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Firefox-DevTools]]

## Tags

- recon
- request-capture
