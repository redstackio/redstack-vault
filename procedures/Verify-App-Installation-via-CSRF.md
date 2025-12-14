---
tags:
  - verification
  - installation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.878Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 2a4a89cc-449f-4f9e-a656-cec2ec0ebac9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-App-Installation-via-CSRF

## Summary

This procedure checks for successful app installations triggered by the CSRF attack, confirming the expanded attack surface in Nextcloud.

## Description

After the request, the endpoint installs recommended apps. Verification involves logging into the admin panel to observe changes, highlighting risks from unused or vulnerable plugins.

## Requirements

1. Access to Nextcloud admin credentials (or prior access)
2. Completion of prior CSRF trigger steps
3. Ability to view app management section

## Defense

Defensive measures and detection strategies:

- Audit logs for unauthorized installations
- Disable auto-install of recommended apps
- Regular reviews of installed plugins

## Objectives

1. Confirm apps were installed without consent
2. Assess new vulnerabilities introduced
3. Document impact for reporting

## Instructions

### Step 1: Access Admin Panel

**Context**: Log in to Nextcloud as admin and navigate to Apps section.

Browse to https://target-nextcloud.com/settings/apps

> Expected output: List of installed apps updated with new recommendations.

### Step 2: Check Logs

**Context**: Review server logs for installation events.

Look for entries like "Installing app: recommended-app-name"

> Expected output: Log confirms processing of the GET request and installations.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[nextcloud]]
