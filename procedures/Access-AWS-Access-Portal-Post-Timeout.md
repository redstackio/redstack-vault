---
tags:
  - aws
  - portal
  - access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.701Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e1634d54-1cd2-4c77-8fd2-40cc641ee1b3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-AWS-Access-Portal-Post-Timeout

## Summary

This procedure navigates to the AWS Access Portal after console session expiration to exploit the lack of re-authentication enforcement.

## Description

The AWS Access Portal (https://*.awsapps.com/start) is intended for SSO-based access to accounts and apps. Due to inconsistent session handling, expired console sessions remain valid here, allowing bypass. This step tests portal accessibility in the same browser session.

## Requirements

1. Expired console session in browser
2. AWS Access Portal URL (organization-specific)
3. Same browser instance (cookies intact)

## Defense

Defensive measures and detection strategies:

- Synchronize session policies between console and portal
- Enable just-in-time access in IAM Identity Center
- Audit portal access logs for post-timeout entries

## Objectives

1. Reach the portal without SSO prompt
2. Confirm session persistence
3. Set up for resource access

## Instructions

### Step 1: Open Portal URL

**Context**: Direct browser to the portal endpoint.

Enter `https://yourorg.awsapps.com/start` in the address bar.

> The page should load the portal interface without redirecting to SSO.

### Step 2: Inspect Session State

**Context**: Verify no re-auth is triggered.

Attempt to view available accounts/apps.

> Success if list populates; failure if SSO login appears. Use dev tools to inspect for active tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[access-portal]]
- [[bypass]]
