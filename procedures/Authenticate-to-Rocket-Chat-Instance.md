---
id: proc-auth-rocket-chat
tags:
  - authentication
  - api-access
  - rocket-chat
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
updated_at: '2025-12-14T17:32:01.576Z'
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
# Authenticate-to-Rocket-Chat-Instance

## Summary

This procedure establishes authenticated access to a Rocket.Chat instance, enabling subsequent API interactions by retrieving necessary authentication tokens from browser storage.

## Description

Rocket.Chat requires authentication for API endpoints like users.list. This step involves creating a user account via the web interface and extracting the X-Auth-Token and X-User-Id, which are stored client-side. These tokens grant view-d-room permissions, sufficient for exploiting the vulnerable endpoint. The process targets public instances like open.rocket.chat and assumes no additional permissions are needed beyond basic user signup.

## Requirements

1. Web browser access to the Rocket.Chat instance
2. Ability to create a new user account (no invite required for public instances)
3. Developer tools enabled in the browser for inspecting local storage

## Defense

Defensive measures and detection strategies:

- Enforce strong account creation policies, such as CAPTCHA or email verification
- Monitor for unusual token usage or rapid account creations
- Log all authentication events and review for anomalies

## Objectives

1. Obtain valid authentication tokens for API access
2. Ensure the account has minimal permissions like view-d-room
3. Prepare for exploitation without triggering alerts

## Instructions

### Step 1: Create Account and Login

**Context**: Sign up to gain initial access and trigger token generation.

Navigate to the Rocket.Chat instance (e.g., https://open.rocket.chat) and complete the registration form with email and password. Log in to the dashboard.

> Successful login redirects to the chat interface, confirming access.

### Step 2: Extract Authentication Tokens

**Context**: Retrieve tokens from browser storage for API use.

Open browser Developer Tools (F12), go to Application > Storage > Local Storage > select the Rocket.Chat domain. Copy the values for 'authToken' (as X-Auth-Token) and 'userId' (as X-User-Id).

> Tokens appear as long strings; store securely for the next step.

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
- token-extraction
- web-access
