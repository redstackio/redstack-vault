---
id: proc-004-receive-notification
tags:
  - info-leak
  - notification
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:28:28.256Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Receive-Unauthorized-Notification

## Summary

This procedure captures the unauthorized in-app notification sent to a former subscriber, confirming the leak of report metadata like titles during transfers.

## Description

Amplified by prior incidents like SAML JIT adding extra subscribers, the notification includes sensitive details despite program removal. No full report access is gained, but metadata exposure erodes trust. Fixed by updating removal logic and record cleanup.

## Requirements

1. Removed user account with active HackerOne session
2. Recent report transfer in the ex-program
3. Notification preferences enabled

## Defense

Defensive measures and detection strategies:

- Purge invalid subscribers pre-notification
- Encrypt or anonymize metadata in alerts
- Alert on notifications to non-members

## Objectives

1. Intercept leaked notification
2. Extract report title and transfer details
3. Validate unauthorized access scope

## Instructions

### Step 1: Monitor Inbox

**Context**: Check for incoming alerts post-transfer.

Log in as removed user, navigate to notifications tab.

### Step 2: View Notification

**Context**: Access the leaked content.

Open the transfer notification; note included details like report title.

### Step 3: Document Leak

**Context**: Record evidence of exposure.

Screenshot or log the notification, confirming metadata without program access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- info-leak
- notification
