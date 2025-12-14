---
id: access-profile-modal
tags:
  - recon
  - profile-access
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
updated_at: '2025-12-14T17:33:12.069Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Profile-Name-Change-Modal

## Summary

This procedure navigates the authenticated session to the profile editing modal in Acronis File Sync & Share, which exposes the vulnerable name and email change functionality leading to API exploitation.

## Description

Once logged in, the attacker accesses the user profile settings to open a modal for editing display name and email. This modal triggers a PUT request to the /fc/api/v1/account endpoint upon save, which lacks proper verification. The procedure assumes an active session and targets the web interface. Outcomes include the modal being open and ready for interaction to initiate the vulnerable request.

## Requirements

1. Active authenticated session from prior login
2. Access to the dashboard at https://mc-beta-cloud.acronis.com/fc/access#/nodes
3. Web browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Log all profile access and modification attempts with user context
- Require secondary verification for profile changes, especially email updates
- Audit API calls to account endpoints for anomalies like rapid changes

## Objectives

1. Expose the email change interface
2. Prepare for request interception
3. Identify current account details for modification planning

## Instructions

### Step 1: Navigate to Dashboard

**Context**: Ensure the session is at the main interface post-login.

No specific command; confirm URL is https://mc-beta-cloud.acronis.com/fc/access#/nodes.

> The dashboard should display file nodes and navigation options.

### Step 2: Open Profile Modal

**Context**: Trigger the editing interface for name and email.

No specific command; click the profile button in the top right corner, then select the 'Name' option.

> The modal opens with fields for current name and email, plus a save button. Note the current email for reference in modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-ui
- profile-edit
