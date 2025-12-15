---
tags:
  - deauthorization
  - auth-removal
  - weblate
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
updated_at: '2025-12-14T17:31:10.914Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 6dcff343-8c49-4de6-be75-6256cf67ad06
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Remove-Third-Party-Authentication-Linkage

## Summary

This procedure disconnects a third-party authentication provider from a Weblate account, exploiting the lack of session invalidation to maintain unauthorized access on other devices.

## Description

In Weblate's profile management at /accounts/profile/#auth, removing OAuth linkages should ideally trigger session cycling for security. However, due to the vulnerability, this does not occur, allowing persistent sessions. This step requires an active session on the primary device and targets the auth management UI. Outcome: Provider unlinked without revoking existing sessions.

## Requirements

1. Active session on the primary device with linked provider
2. Access to profile authentication settings
3. No additional MFA blocking the removal action
4. Stable connection to the Weblate instance

## Defense

Defensive measures and detection strategies:

- Automatically invalidate all sessions upon auth method changes
- Require secondary verification for deauthorizing providers
- Audit logs for linkage removals and correlate with active sessions

## Objectives

1. Revoke third-party access to the account
2. Trigger (or exploit failure of) session invalidation
3. Enable persistence testing on secondary sessions

## Instructions

### Step 1: Navigate to Auth Management

**Context**: Access the profile to locate and target the linked provider.

Log in on the first device if needed, then go to https://hosted.weblate.org/accounts/profile/#auth.

> Identify the Google entry in the list of connected providers.

### Step 2: Execute Disconnection

**Context**: Perform the removal action and confirm changes.

Click the disconnect button next to Google and follow any confirmation prompts to complete the unlinking.

> Refresh the profile page to verify Google is no longer listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[deauthorization]]
- [[auth-removal]]
