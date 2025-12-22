---
tags:
  - configuration
  - phabricator
  - navigation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T04:08:46.190Z'
sub_techniques: []
id: 81abd02a-98c1-4003-82bb-d569a05b9482
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Navigate-to-Notification-Servers-Configuration

## Summary

This procedure details accessing the specific configuration section in Phabricator for notification servers, enabling modifications that lead to SSRF exploitation.

## Description

Once authenticated, administrators can navigate Phabricator's web-based config interface to the notifications.server setting. This JSON-configurable option defines client and admin servers for notifications, lacking validation on host/port/protocol, which allows SSRF when Phabricator connects and follows redirects.

## Requirements

1. Active administrator session in Phabricator
2. Web browser with JavaScript enabled
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Audit logs for config access and changes
- Validate all config inputs server-side
- Restrict admin navigation to audited paths

## Objectives

1. Reach the editable notifications.server interface
2. View existing configuration for modification planning
3. Identify the Database Value editor

## Instructions

### Step 1: Enter Configuration Menu

**Context**: From the dashboard, access the global settings.

Click on 'Config' in the admin menu.

> Expected output: Settings overview page loads.

### Step 2: Locate Notification Servers

**Context**: Drill down to the specific setting.

Navigate to Settings > notification.servers.

> Expected output: JSON configuration form appears with 'Simple Example' and 'Database Value' fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[configuration]]
- [[phabricator]]
- [[navigation]]
