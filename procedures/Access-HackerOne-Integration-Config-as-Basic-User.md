---
id: proc-uuid-002
tags:
  - access-control-bypass
  - config-access
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.167Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-HackerOne-Integration-Config-as-Basic-User

## Summary

This procedure demonstrates how a basic Jira user can directly access the HackerOne integration configuration page, which lacks permission checks, exposing a JWT token for admin actions.

## Description

The plugin's endpoint /plugins/servlet/ac/com.hackerone/get-started-with-hackerone-on-jira treats all authenticated users equally, allowing basic users to view the setup interface intended for admins. This leads to generation of a JWT that grants over-privileged access when claimed.

## Requirements

1. Logged-in basic user session in Jira
2. Installed HackerOne app
3. Browser access to Jira instance

## Defense

Defensive measures and detection strategies:

- Implement server-side permission verification before rendering config pages
- Log and alert on non-admin access to app endpoints
- Use Atlassian Connect descriptors to enforce scopes

## Objectives

1. Bypass UI-level access controls
2. Expose sensitive setup interface
3. Obtain JWT without admin privileges

## Instructions

### Step 1: Log In as Basic User

**Context**: Authenticate with limited privileges.

Use Jira login page to sign in as basic user.

> Expected: Dashboard loads with restricted views.

### Step 2: Navigate to Config Endpoint

**Context**: Directly access the unprotected page.

Enter URL: {BaseUrl}/plugins/servlet/ac/com.hackerone/get-started-with-hackerone-on-jira in browser.

> Expected: Page displays "Get started with HackerOne on Jira" prompt with clickable link containing JWT.

### Step 3: Inspect for JWT

**Context**: Use dev tools to confirm exposure.

**Command** (Manual with [[tools/Browser-Developer-Tools]]):
Open Network tab, reload page, inspect response or link href for JWT.

> Expected: Link like https://hackerone.com/apps/atlassian/claim-app?jwt=eyJ... visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- access-control-bypass
- config-access
