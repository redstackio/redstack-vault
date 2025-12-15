---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - discovery
  - logs
  - monitoring
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Network Device
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:31:19.070Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Review-Device-Logs-for-History

## Summary

This procedure examines the Cisco TelePresence SX80's internal logs post-compromise to uncover usage history, identify monitoring gaps, and assess persistence risks in unmaintained devices.

## Description

Admin access reveals logs detailing conferences, logins, and errors. In this case, logs showed inactivity since 2017, indicating low oversight. Attackers use this to gauge detection likelihood and plan long-term access. Logs are stored locally and accessible via the web UI without additional auth.

## Requirements

1. Active admin session
2. Access to logging section in the dashboard
3. Basic understanding of log formats (timestamps, events)

## Defense

Defensive measures and detection strategies:

- Enable remote syslog forwarding to a central server
- Set log retention policies and alert on access to logs
- Regularly review device logs for anomalies like unexpected queries

## Objectives

1. Identify last activity timestamps
2. Confirm monitoring status
3. Inform persistence strategy

## Instructions

### Step 1: Navigate to Logs

**Context**: Locate the logging interface in admin controls.

From the dashboard, select maintenance > logs or similar.

> Logs display in a browsable format with filters.

### Step 2: Analyze Entries

**Context**: Scan for usage patterns and inactivity.

Review timestamps and events, noting last conference in 2017.

> Output: Evidence of dormancy, e.g., no logins post-2017, suggesting reduced alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- discovery
- logs
- monitoring
