---
tags:
  - dos-execution
  - resource-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-12-14T10:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:48.486Z'
sub_techniques: []
id: 233fc0b3-1aa7-44db-a4ec-b33ade26ef82
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Initiate-Playbook-Run-to-Trigger-DoS

## Summary

This procedure initiates a run on the oversized playbook in Mattermost, causing the server to process the 50MB template and leading to excessive CPU/memory usage, server crash, and denial of service.

## Description

Once the playbook with oversized run_summary_template is created, starting a run triggers backend processing of the large data, resulting in uncontrolled resource consumption. This crashes the server, making the application unavailable to all users, with lingering issues post-restart like blank playbook pages.

## Requirements

1. Created playbook with oversized template
2. Access to Mattermost UI as authenticated user
3. Server monitoring tools (optional for observation)

## Defense

Defensive measures and detection strategies:

- Limit playbook run resources (e.g., timeouts, memory caps)
- Scan for oversized data during creation and reject
- Implement resource monitoring and auto-scaling alerts

## Objectives

1. Trigger processing of oversized template
2. Cause server resource exhaustion and crash
3. Achieve widespread DoS impact

## Instructions

### Step 1: Navigate to Playbook

**Context**: Open the malicious playbook in the UI.

Go to Playbooks section and click the created playbook.

> Expected output: Details page loads.

### Step 2: Start the Run

**Context**: Initiate execution to process the template.

Click 'Run' button and enter a run name (e.g., 'TestRun').

> Expected output: Run starts; monitor for resource spike within seconds.

### Step 3: Observe and Confirm Impact

**Context**: Verify DoS by checking application availability.

Attempt logins or page loads; after manual restart, check playbook runs.

> Expected output: Server crashes, app down; post-restart, blank screens on run pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos-execution
- resource-exhaustion
