---
id: proc-cloudflare-logout-dashboard-001
tags:
  - session-management
  - cloudflare
  - logout
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.501Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Logout-from-Cloudflare-Dashboard

## Summary

This procedure performs a logout from the Cloudflare Dashboard, which due to an outdated implementation, does not propagate to the Zero Trust Dashboard, leaving the latter session active.

## Description

The vulnerability stems from independent session handling in the dashboards despite shared login. Logging out from the main Dashboard sends a session invalidation request that fails to synchronize across interfaces. This requires no special tools, just browser interaction. Expected outcome: Dashboard session ends, but Zero Trust remains accessible, highlighting the flaw.

## Requirements

1. Active session in Cloudflare Dashboard
2. Web browser with the session open
3. No additional privileges needed

## Defense

Defensive measures and detection strategies:

- Synchronize session invalidation across all linked services
- Implement global logout tokens that expire all related sessions
- Log and alert on session activities post-logout attempts

## Objectives

1. Terminate the Dashboard session
2. Exploit lack of propagation to maintain Zero Trust access
3. Validate the session mismatch

## Instructions

### Step 1: Initiate Logout

**Context**: Trigger the logout mechanism in the Dashboard.

Click on your profile icon in the top-right of the Dashboard, then select 'Log out' from the dropdown menu. Confirm if prompted.

> The page should redirect to the login screen, indicating successful Dashboard logout.

### Step 2: Verify Dashboard Invalidation

**Context**: Confirm the session is no longer valid in the Dashboard.

Attempt to navigate to a protected Dashboard page, such as account settings.

> Expected output: Redirect to login page with no access to prior content.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-management]]
- [[logout]]
