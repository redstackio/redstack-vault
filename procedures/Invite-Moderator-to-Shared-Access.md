---
id: proc-streamlabs-invite-mod-001
tags:
  - shared-access
  - moderator-invite
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
updated_at: '2025-12-14T17:32:20.840Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-Moderator-to-Shared-Access

## Summary

This procedure sets up shared access by inviting a secondary user as a moderator to the parent Streamlabs account, enabling subsequent exploitation of access control flaws.

## Description

In the Streamlabs dashboard, the shared access feature allows account owners to invite users with roles like Moderator, which should limit permissions but fails to enforce checks on certain API endpoints. This step creates the invitation link, targeting the web-based settings page. Prerequisites include a valid parent account login. Expected outcome: A moderator gains entry point to the account context.

## Requirements

1. Valid credentials for the parent Streamlabs account (User A)
2. Access to a web browser
3. Internet connectivity to https://streamlabs.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) with strict API permission validation
- Monitor invitation link generations and acceptances for anomalous patterns
- Audit shared access logs for unauthorized role assignments

## Objectives

1. Generate a moderator invitation link for shared access
2. Establish initial shared context between accounts
3. Prepare for context switching and API exploitation

## Instructions

### Step 1: Log In and Navigate to Settings

**Context**: Access the parent account dashboard and locate shared access configuration.

Log in to User A's Streamlabs account and go to the dashboard settings.

Navigate to: https://streamlabs.com/dashboard#/settings/shared-access

**Expected Output**: Shared access settings page loads, showing options to create invitations.

### Step 2: Create Invitation Link

**Context**: Select Moderator role and generate the link to invite User B.

In the shared access section, choose "Moderator" role and click to generate the invitation link. Copy the link.

**Expected Output**: Unique invitation URL is provided for sharing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shared-access]]
- [[moderator-invite]]
