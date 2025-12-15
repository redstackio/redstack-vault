---
tags:
  - account-manipulation
  - email-addition
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:58.991Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 031c5db1-18f3-4127-9af8-30b29074d7f2
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Initiate Email Addition in Account Settings

## Summary

This procedure accesses Phabricator's account settings to start adding a new email address, exploiting the lack of re-authentication prompts for session-based users.

## Description

Phabricator's email management feature, found in user settings, allows adding addresses without password or 2FA verification if a valid session exists. This design choice avoids MFA fatigue but enables session compromise attacks. The procedure assumes an active session and leads to email submission without barriers.

## Requirements

1. Valid Phabricator session
2. Browser access to the web interface
3. Target account with email settings enabled

## Defense

Defensive measures and detection strategies:

- Require re-authentication for sensitive changes like email addition
- Log and alert on email modifications from active sessions
- Enable 2FA for all account changes

## Objectives

1. Load email management interface
2. Prepare for unauthorized email addition
3. Bypass authentication checks

## Instructions

### Step 1: Navigate to Settings

**Context**: Reach the account configuration area.

**Instructions**: From the Phabricator dashboard, click on user profile > Settings > Emails (URL approx. /settings/panel/emails/).

> Interface loads with current emails listed.

### Step 2: Locate Add Email Form

**Context**: Identify the addition mechanism.

**Instructions**: Find and click 'Add Email Address' button or link.

> Form for email input appears without auth prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[phabricator]]
