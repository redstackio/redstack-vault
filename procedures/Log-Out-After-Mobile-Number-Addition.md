---
tags:
  - session-management
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
updated_at: '2025-12-14T17:30:58.801Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: eb37ed1a-d6d2-47a3-8e31-9b27f4c7d3b2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-Out-After-Mobile-Number-Addition

## Summary

This simple procedure terminates the current session after adding an unverified mobile number, simulating a scenario where the attacker must rely on the reset flow for re-access.

## Description

Following the mobile number addition, logging out ensures the account is in a state requiring re-authentication via password reset. This step is crucial to test the unverified number's usability in the forgot password flow without an active session. The target is the Twitter web platform, with no special prerequisites beyond the prior step's completion. Expected outcome is a clean logout, redirecting to the login page.

## Requirements

1. Active session from previous mobile number addition step
2. Web browser access to Twitter

## Defense

Defensive measures and detection strategies:

- Monitor session logs for patterns of quick add-logout cycles
- Require secondary verification on sensitive actions like number addition before logout

## Objectives

1. End the current authenticated session
2. Force reliance on password reset for re-entry
3. Validate the setup for the next exploitation step

## Instructions

### Step 1: Initiate Logout

**Context**: From the account dashboard or settings, trigger the logout action.

Click on the profile icon or menu, select "Log out", and confirm if prompted.

> The page redirects to the Twitter homepage or login screen, confirming session termination.

### Step 2: Verify Session End

**Context**: Ensure no residual access remains.

Attempt to access a protected feature (e.g., tweets); redirection to login indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-management]]
