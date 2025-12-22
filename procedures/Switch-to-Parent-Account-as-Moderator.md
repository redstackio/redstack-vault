---
id: proc-streamlabs-switch-context-001
tags:
  - context-switch
  - shared-access
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:20.835Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Switch-to-Parent-Account-as-Moderator

## Summary

This procedure switches the moderator's dashboard context to the parent account, allowing actions as if authenticated as the parent while retaining moderator limitations that are bypassed later.

## Description

From the moderator's dashboard, select the shared account to switch context, loading the parent interface. This exploits the lack of re-validation on switch. Expected outcome: Full parent dashboard access without owner privileges enforced.

## Requirements

1. Active moderator role in the parent account
2. Logged in as User B
3. Access to https://streamlabs.com/dashboard

## Defense

Defensive measures and detection strategies:

- Re-validate permissions on every context switch
- Session tokens should carry role info and expire on switches
- Log context changes and monitor for moderator actions on sensitive endpoints

## Objectives

1. Load parent account interface as moderator
2. Confirm acting-as status
3. Prepare for API endpoint testing

## Instructions

### Step 1: Navigate to Shared Access in Moderator Dashboard

**Context**: Locate the parent account in shared access settings.

In User B's dashboard, go to https://streamlabs.com/dashboard#/settings/shared-access.

**Expected Output**: List of shared accounts, including User A.

### Step 2: Switch Context

**Context**: Select to act as the parent account.

Click on User A's entry to switch. The UI should update to indicate "You are currently acting as [User A], click here to return to your account".

**Expected Output**: Parent dashboard loads in moderator context.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[context-switch]]
- [[shared-access]]
