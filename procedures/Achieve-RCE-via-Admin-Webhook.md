---
id: 123e4567-e89b-12d3-a456-426614174004
name: Achieve-RCE-via-Admin-Webhook
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.423Z'
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[PowerShell]]'
  - '[[Execution through API]]'
sub_techniques: []
tags:
  - rce
  - webhook
  - privilege-escalation
platforms:
  - Web
commands: []
tools: []
skill_level: advanced
impact_level: critical
detection_risk: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[PowerShell]]'
  - '[[Execution through API]]'
---

# Achieve-RCE-via-Admin-Webhook

## Summary

This procedure uses stolen admin privileges to create an incoming webhook in Rocket.Chat configured with a malicious script, enabling remote code execution on the server without additional boundaries.

## Description

With admin access from XSS, navigate to integrations and set up an incoming webhook that executes arbitrary scripts (e.g., via Meteor's server-side execution or shell commands). Triggering the webhook allows full control, including database exposure and system compromise.

## Requirements

1. Admin session from XSS
2. Access to administration panel
3. Knowledge of webhook scripting for RCE payloads

## Defense

Defensive measures and detection strategies:

- Restrict webhook creation to audited scripts only
- Implement sandboxing for webhook executions
- Log and alert on new webhook creations by admins

## Objectives

1. Execute server-side code
2. Gain shell or command access
3. Expose connected systems

## Instructions

### Step 1: Access Admin Panel

**Context**: Use stolen session to reach integrations.

**Command** (No CLI; use UI):
Go to Administration > Integrations > New Incoming Webhook.

> Expected output: Webhook creation form loads.

### Step 2: Configure Malicious Webhook

**Context**: Set up payload for RCE.

**Command** (No CLI; use UI):
Define webhook with script (e.g., exec('ls') or Meteor.call for commands), enable, and save.

> Expected output: Webhook active with token.

### Step 3: Trigger Webhook

**Context**: Invoke for execution.

**Command** (No CLI; use curl or POST):
Send POST request to webhook URL with trigger payload.

> Expected output: Server executes script, e.g., command output or file changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Lateral Movement]]

### Techniques

- [[PowerShell]]
- [[Execution through API]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[webhook]]
- [[privilege-escalation]]
