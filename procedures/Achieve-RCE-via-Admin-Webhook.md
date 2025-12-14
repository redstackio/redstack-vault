---
id: proc-rce-webhook
tags:
  - rce
  - webhook
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:31:18.942Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Remote File Copy]]'
---
---

# Achieve-RCE-via-Admin-Webhook

## Summary

This procedure leverages the stolen admin session from XSS to create an incoming webhook integration, enabling remote code execution on the server without additional boundaries.

## Description

Admin privileges allow setting up integrations that run scripts on incoming HTTP requests. Post-XSS, the attacker can configure a webhook to execute arbitrary commands, impacting CIA triad by allowing database manipulation and credential exposure.

## Requirements

1. Admin session hijacked via XSS
2. Access to admin panel
3. Knowledge of target scripts for execution

## Defense

Defensive measures and detection strategies:

- Restrict webhook creation to audited scripts only
- Implement webhook authentication and rate limiting
- Monitor server logs for unauthorized executions

## Objectives

1. Gain server-side execution capabilities
2. Exfiltrate or modify data remotely
3. Achieve full compromise

## Instructions

### Step 1: Access Admin Panel

**Context**: Use hijacked session to reach settings.

**Instructions**: Navigate to Administration > Integrations as admin.

### Step 2: Create Incoming Webhook

**Context**: Configure a malicious integration.

**Instructions**: Select Incoming type, enable script execution, and define a payload that runs system commands (e.g., via child_process in Node.js).

**Expected Output**: Webhook URL generated.

### Step 3: Trigger RCE

**Context**: Send requests to execute code.

**Instructions**: POST to the webhook URL with command payload; observe server response.

**Expected Output**: Command output in response, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- webhook
- privilege-escalation

