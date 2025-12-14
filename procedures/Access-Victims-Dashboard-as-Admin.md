---
tags:
  - impersonation
  - dashboard-access
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
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6b7a32da-0102-4e24-abc1-ec2a29a1451d
created_at: '2025-12-13T23:52:55.365Z'
updated_at: '2025-12-13T23:52:55.365Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Victims-Dashboard-as-Admin

## Summary

Impersonate the victim by accessing their Streamlabs dashboard through the shared admin link.

## Description

After accepting the invitation, use the shared access interface to switch to the victim's context. This allows navigation to sensitive pages like goal settings without the victim's knowledge. The endpoint uses an 'act-as' parameter for impersonation.

## Requirements

1. Active shared admin access
2. Browser with cookies intact
3. Knowledge of victim's userId (inferred from link)

## Defense

Defensive measures and detection strategies:

- Log all act-as sessions
- Require victim approval for switches
- Session timeouts for shared access

## Objectives

1. Gain full dashboard control
2. Reach goal setting pages
3. Enable payload injection

## Instructions

### Step 1: Navigate to Shared Access Page

**Context**: Locate the victim's entry.

**Instructions**: Go to https://streamlabs.com/dashboard#/settings/shared-access in attacker's account.

**Expected Output**: List of shared accounts.

### Step 2: Click to Impersonate

**Context**: Switch to victim's dashboard.

**Instructions**: Click the hyperlink on victim's username to reach https://streamlabs.com/dashboard/act-as/{userId}.

**Expected Output**: Victim's dashboard loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[act-as]]
- [[session-hijack]]
