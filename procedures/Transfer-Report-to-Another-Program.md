---
id: proc-003-transfer-report
tags:
  - transfer
  - notification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.260Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Transfer-Report-to-Another-Program

## Summary

This procedure triggers the report transfer functionality in HackerOne, notifying all subscribers—including unauthorized former ones—via the persisted relationship, leaking metadata.

## Description

The 'Transfer report' feature in HackerOne uses the Report model's subscribers association to send notifications on title changes or transfers. Due to the vulnerability, removed users receive these, exposing details like report titles. Affected 2110 notifications across 21 programs.

## Requirements

1. Authorized access to source program reports
2. Target program for transfer
3. Active HackerOne session

## Defense

Defensive measures and detection strategies:

- Validate subscribers before notification dispatch
- Log transfer events with subscriber audits
- Rate-limit notifications to verified members

## Objectives

1. Move report between programs
2. Activate notification to leaked subscribers
3. Demonstrate metadata exposure

## Instructions

### Step 1: Select Report

**Context**: Identify a report for transfer.

Navigate to reports list in source program, select one with subscribers.

### Step 2: Initiate Transfer

**Context**: Use UI to start transfer process.

Click 'Transfer' action, select destination program, and confirm. This triggers <report instance>.subscribers notifications.

### Step 3: Monitor Notification Queue

**Context**: Ensure dispatch includes unauthorized users.

Check backend logs (if accessible) or wait for recipient feedback on notifications sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- transfer
- notification
