---
tags:
  - account-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: 0742d9ed-c18a-4243-9479-d401dda2fa2b
created_at: '2025-12-14T17:28:51.743Z'
updated_at: '2025-12-14T17:28:51.743Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Navigate-to-Coinbase-Settings-Page

## Summary

This procedure navigates to the Coinbase settings page from the dashboard, accessing administrative controls without re-verification due to the initial bypass.

## Description

The settings page at https://www.coinbase.com/settings contains options for account management. The bypassed session allows unrestricted navigation, stemming from inadequate authorization checks in the routing logic for mobile sessions.

## Requirements

1. Active dashboard session from previous access
2. Windows Phone browser maintaining the session
3. No intervening logout or verification

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls with per-page verification
- Track navigation patterns and flag direct settings access post-mobile login
- Session timeouts for sensitive areas

## Objectives

1. Reach account configuration options
2. Prepare for settings enumeration
3. Enable potential destructive actions

## Instructions

### Step 1: Locate Settings Link

**Context**: From the dashboard, find the path to settings.

Click on the user profile or menu icon leading to settings.

> The page loads directly via internal navigation.

### Step 2: Direct URL Access

**Context**: Use the explicit URL for confirmation.

Enter or navigate to https://www.coinbase.com/settings in the browser.

> Page renders fully without auth prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-discovery]]
