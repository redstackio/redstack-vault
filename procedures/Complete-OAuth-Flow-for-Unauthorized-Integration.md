---
tags:
  - oauth-flow
  - calendar-sync
  - unauthorized-integration
  - 8x8
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
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:30:18.088Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Application Access Token]]'
id: 0ac233d7-c53f-4e6f-8e95-c0749148ce1f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
# Complete-OAuth-Flow-for-Unauthorized-Integration

## Summary

This procedure completes the Cronofy OAuth flow initiated by a member user, authorizing an external email (e.g., Gmail) and linking it to the 8x8 admin rooms section without permission checks, enabling unauthorized calendar access.

## Description

Following the auth init, the OAuth URL leads to Cronofy authorization. Without validation, the member's email is integrated into the admin's room management, potentially allowing read-only calendar data sync or further manipulation in Jitsi-integrated meetings.

## Requirements

1. OAuth URL from previous init step
2. Member's external email account (e.g., Gmail)
3. Browser for OAuth consent

## Defense

Defensive measures and detection strategies:

- Validate user roles during OAuth callback processing
- Restrict delegated scopes for non-admin users
- Audit calendar integrations for unauthorized sources

## Objectives

1. Authorize OAuth with member email
2. Complete integration to admin area
3. Verify unauthorized linking

## Instructions

### Step 1: Access OAuth URL

**Context**: Open the provided Cronofy URL in a browser to start the flow.

Navigate to the URL, e.g., https://app.cronofy.com/oauth/authorize?response_type=code&client_id=M0wBDPDXk6EQLaGCqp-pTN_VGt7_AtM9&redirect_uri=https://api-vo.jitsi.net/rosy/sso/cronofy/callback&scope=read_only&delegated_scope=read_only&state=...&avoid_linking=true.

> The page prompts for email signup or authorization; no admin check occurs.

### Step 2: Authorize and Complete

**Context**: Consent to calendar access with member's email and follow redirects.

Enter Gmail credentials, grant read_only scope, and complete the flow.

> Success: Redirect to callback, then to successRedirectUrl (admin rooms add), with email now integrated.

### Step 3: Verify Integration

**Context**: Check admin rooms for the new calendar link.

Log in as admin and navigate to https://admin.8x8.vc/#/rooms/add; member's email should appear as synced.

> Expected: Unauthorized calendar visible in privileged section.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques

- [[Application Access Token]] Application Access Token (OAuth tokens)

## Commands Used

-

## Tools Used

-

## Tags

- [[oauth-flow]]
- [[calendar-sync]]
