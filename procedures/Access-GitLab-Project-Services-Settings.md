---
id: proc-gitlab-access-services-settings
tags:
  - gitlab
  - settings-access
  - integrations
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:31.013Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-GitLab-Project-Services-Settings

## Summary

This procedure details navigating to the services configuration in a GitLab project, enabling setup of vulnerable integrations like the custom issue tracker for XSS injection.

## Description

To exploit the persistent XSS, the attacker must access the project settings where third-party integrations are configured. GitLab's services page allows enabling custom issue trackers without proper input validation, storing malicious URLs that render on the Issues page.

## Requirements

1. Ownership or maintainer access to the target project.
2. Web browser for UI navigation.
3. Project must exist and be accessible.

## Defense

Defensive measures and detection strategies:

- Role-based access controls to restrict settings modifications.
- Audit logs for service configuration changes.
- Input sanitization on all integration fields.

## Objectives

1. Reach the configuration interface for custom integrations.
2. Identify vulnerable fields like Project URL.
3. Prepare for payload injection.

## Instructions

### Step 1: Enter Project Settings

**Context**: From the project dashboard, access administrative controls.

Click the "Settings" gear icon in the left sidebar of the project page.

### Step 2: Select Services

**Context**: Navigate to integration options.

In the Settings menu, click "Services" to load the list of available integrations.

**Expected Output**: Services page with options like Custom Issue Tracker.

### Step 3: Enable Custom Issue Tracker

**Context**: Activate the vulnerable integration.

Scroll to "Custom Issue Tracker" and click "Configure" or the toggle to enable it.

**Expected Output**: Form fields for URLs appear, ready for input.

**Success Indicators**:
- Services page loaded.
- Custom Issue Tracker form accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[settings-access]]
