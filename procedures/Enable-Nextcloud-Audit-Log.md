---
tags:
  - nextcloud
  - audit-log
  - enable
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
techniques: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bc81db33-ca0f-4c66-86ab-557d7b8b5032
created_at: '2025-12-14T17:29:09.994Z'
updated_at: '2025-12-14T17:29:09.994Z'
verified: false
validated: true
submitted: true
---
# Enable-Nextcloud-Audit-Log

## Summary

This procedure activates the built-in audit logging app in Nextcloud to track administrative and user actions, essential for monitoring share modifications in vulnerability assessments.

## Description

In the context of testing Nextcloud's logging capabilities, enabling the audit log ensures that subsequent actions like file sharing and expiration changes are captured (where the system functions correctly). This step requires administrative access and uses the web interface. The expected outcome is an active logging mechanism that writes events to a configurable log file or viewer, aiding in the detection of logging deficiencies.

## Requirements

1. Administrative credentials for the Nextcloud instance
2. Access to the Nextcloud web interface via a browser
3. Nextcloud instance with the Audit Log app available (default in most installations)

## Defense

Defensive measures and detection strategies:

- Ensure audit logging is always enabled in production environments
- Regularly review log configurations for completeness
- Use external monitoring tools to supplement built-in logging

## Objectives

1. Activate audit logging to baseline normal behavior
2. Prepare for testing share expiration modifications
3. Verify logging activation without errors

## Instructions

### Step 1: Access Admin Settings

**Context**: Log in and navigate to the apps management section to locate the audit log feature.

No command required; use the web UI:

- Log in as admin
- Go to Settings > Apps > Active apps
- Search for "Audit Log"

> Upon enabling, the app status changes to active, and logging begins immediately for qualifying events.

### Step 2: Confirm Enablement

**Context**: Verify that the audit log is operational by checking settings or performing a test action.

No command required; use the web UI:

- Return to admin settings
- Check that Audit Log is listed as enabled

> Successful enablement shows no configuration errors; logs can now be viewed via the admin log viewer.

## MITRE ATT&CK Mapping

### Tactics

- None

### Techniques

- None

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[nextcloud]]
- [[audit-log]]
