---
tags:
  - authentication
  - oauth
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: a6343b7c-00ad-451d-af0c-2bc0a93eba40
created_at: '2025-12-14T17:31:19.573Z'
updated_at: '2025-12-14T17:31:19.573Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-OWOX-Portal-using-Gmail-OAuth

## Summary

This procedure outlines the initial authentication to the OWOX support portal using Gmail OAuth, setting up the session that will later be exploited for bypass.

## Description

The OWOX support portal at https://support.owox.com/hc/ relies on Gmail OAuth for user login. This step involves navigating to the portal, initiating the sign-in process, and completing the OAuth flow with a valid Gmail account. It establishes a session token or cookie that persists incorrectly after logout, enabling the vulnerability. Prerequisites include a Gmail account with no prior OWOX authorizations to simulate a fresh login.

## Requirements

1. Web browser with cookies enabled
2. Valid Gmail account credentials
3. Internet access to https://support.owox.com/hc/

## Defense

Defensive measures and detection strategies:

- Implement proper OAuth token revocation on logout
- Monitor for anomalous session persistence post-logout
- Use short-lived session tokens with strict invalidation

## Objectives

1. Gain authenticated access to the portal
2. Establish a baseline session for exploitation
3. Verify OAuth integration works as expected

## Instructions

### Step 1: Navigate to Portal

**Context**: Access the login page to begin the process.

Navigate to https://support.owox.com/hc/ in your web browser.

> The homepage should display a Sign In option.

### Step 2: Initiate Gmail OAuth

**Context**: Start the authentication flow using Gmail.

Click the Sign In button and select the Gmail option to redirect to Google's OAuth consent screen.

> Enter Gmail credentials and authorize OWOX access when prompted.

### Step 3: Complete Login

**Context**: Return to the portal with authenticated session.

After authorization, the browser redirects back to the OWOX dashboard.

> Confirm access by checking for user-specific content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[oauth]]
