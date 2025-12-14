---
tags:
  - account-switch
  - ui-restriction
  - twitter-media-studio
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 88bcffdf-2bb5-46fd-bd5c-b6a0ebe17f0a
created_at: '2025-12-14T17:25:13.096Z'
updated_at: '2025-12-14T17:25:13.096Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Switch-to-Victim-Account-and-Verify-UI-Restrictions

## Summary

This procedure uses analyst credentials to switch to the victim account in Twitter Media Studio and verifies that UI elements like the Sources section are hidden, confirming role-based restrictions that can be bypassed via API.

## Description

Twitter Media Studio allows users with added roles to switch between accounts, but the Analyst role intentionally hides sensitive UI sections such as Sources in the producer dashboard. This step demonstrates the UI enforcement while setting up for API exploitation. The attack scenario involves an analyst with legitimate but limited access, targeting the web platform. Prerequisites include prior analyst addition; outcomes confirm the bypass opportunity exists.

## Requirements

1. Analyst credentials (Account B) with access to victim account
2. Web browser session
3. Prior completion of analyst addition

## Defense

Defensive measures and detection strategies:

- Enforce strict session management and log account switches
- Implement UI and API parity in access controls
- Alert on cross-account switches by limited-role users

## Objectives

1. Switch to victim account using analyst login
2. Verify Sources section is hidden in UI
3. Confirm setup for API bypass

## Instructions

### Step 1: Log In with Analyst Credentials

**Context**: Initiate login to enable account switching.

Navigate to https://studio.twitter.com/ and log in with Account B credentials.

> Expected output: Successful login to analyst dashboard.

### Step 2: Switch to Victim Account and Check Producer Page

**Context**: Switch accounts and inspect the producer interface for restrictions.

Select the victim account (Account A) from the switcher, then go to https://studio.twitter.com/producer.

> Expected output: Producer page loads, but Sources section is absent or hidden due to Analyst role.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[account-switch]]
- [[ui-restriction]]
- [[twitter-media-studio]]
