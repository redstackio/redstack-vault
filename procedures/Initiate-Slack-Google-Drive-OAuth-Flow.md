---
tags:
  - oauth
  - initiation
  - slack
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.320Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ba486f06-08b9-4265-9325-ff08b6b621c5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Slack-Google-Drive-OAuth-Flow

## Summary

This procedure initiates the Google OAuth 2.0 authorization flow for Slack's Google Drive integration, generating the authorization URL that can be inspected for security flaws.

## Description

In the context of testing Slack's third-party integrations, this procedure simulates a legitimate user connecting Google Drive to Slack. By starting the OAuth flow, it exposes the authorization endpoint URL from Google, which in this case lacks the state parameter, opening the door to CSRF attacks. The target environment is a web-based Slack workspace with integration capabilities. Prerequisites include a valid Slack account and browser access. Expected outcome is the redirection to Google's OAuth page without proper CSRF protection.

## Requirements

1. Active Slack workspace account with admin or integration permissions.
2. Web browser with developer tools enabled.
3. Internet access to slack.com and accounts.google.com.

## Defense

Defensive measures and detection strategies:

- Implement strict OAuth state parameter validation on all authorization requests.
- Monitor for anomalous OAuth flows in application logs, such as missing state tokens.
- Use web application firewalls (WAF) to detect and block requests lacking CSRF tokens.

## Objectives

1. Trigger the OAuth authorization to obtain the redirect URL.
2. Verify integration setup without completing authentication.
3. Identify initial exposure points in the flow.

## Instructions

### Step 1: Access Slack Integration Settings

**Context**: Navigate to the Google Drive integration within Slack to begin the connection process.

Log into your Slack workspace, go to Apps > Google Drive, and select 'Add to Slack' or 'Connect Account'.

> This action initiates the OAuth handshake, redirecting to Google's authorization page.

### Step 2: Observe Redirect

**Context**: Allow the browser to follow the redirect and capture the generated URL.

Do not approve the authorization yet; instead, pause to inspect the URL in the address bar.

> Expected: URL without state parameter, confirming vulnerability potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[slack]]
- [[web]]
