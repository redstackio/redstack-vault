---
id: proc-slack-access-001
tags:
  - authentication
  - slack
  - web
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
updated_at: '2025-12-14T17:26:12.502Z'
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
# Access-Slack-Account-and-Photo-Page

## Summary

This procedure outlines signing into a Slack workspace and navigating to the account photo change page, establishing access to the avatar upload functionality for further manipulation.

## Description

In the context of exploring Slack's photo upload feature, this procedure authenticates a user and reaches the /account/photo endpoint. It requires valid credentials and is a prerequisite for URL parameter testing. Expected outcome is access to the upload interface without errors, setting up for alleged RFI testing via external URL loading.

## Requirements

1. Valid Slack workspace credentials (email and password)
2. Web browser with developer tools for URL inspection
3. Network connectivity to Slack's domain

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for account access
- Monitor login attempts from unusual IPs for brute-force detection

## Objectives

1. Gain authenticated access to Slack dashboard
2. Reach photo upload page
3. Prepare for URL parameter interaction

## Instructions

### Step 1: Sign In to Workspace

**Context**: Authenticate to establish a session.

No command required; manually enter credentials at https://[workspace].slack.com/signin.

> Upon success, redirect to dashboard.

### Step 2: Navigate to Photo Page

**Context**: Access the vulnerable endpoint.

No command required; go to https://[workspace].slack.com/account/photo.

> Page loads with upload prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[slack]]
- [[web]]
