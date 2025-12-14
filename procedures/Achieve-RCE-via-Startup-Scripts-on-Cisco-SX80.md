---
id: rce-cisco-sx80-scripts
tags:
  - rce
  - startup-scripts
  - cisco
  - telepresence
  - backdoor
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Hardware
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:31.074Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
---
# Achieve RCE via Startup Scripts on Cisco SX80

## Summary

This procedure leverages authenticated access to upload arbitrary startup scripts on the Cisco TelePresence SX80, enabling remote code execution and persistent compromise for data interception or backdoor establishment.

## Description

The SX80's web interface includes an unrestricted endpoint for managing startup scripts, allowing admins to add custom code that executes on boot or trigger. Attackers can upload malicious scripts (e.g., shell commands) to run arbitrarily. Target: Authenticated SX80 at /web/scripts. Outcomes: Code execution, device takeover, and potential exfiltration from sensitive comms.

## Requirements

1. Full administrative session from prior steps
2. Custom script file prepared (e.g., bash or device-specific)
3. Knowledge of script execution triggers (e.g., reboot)

## Defense

Defensive measures and detection strategies:

- Disable or restrict script upload features
- Validate and sandbox uploaded content
- Monitor for unexpected script executions in logs

## Objectives

1. Upload arbitrary code via scripts endpoint
2. Ensure persistent execution
3. Compromise device for interception/backdoor

## Instructions

### Step 1: Navigate to Scripts Endpoint

**Context**: Access the upload interface for startup scripts.

From the config menu, go to https://██████████/web/scripts.

> The upload form or file manager appears.

### Step 2: Upload and Activate Script

**Context**: Add custom code for execution.

Select and upload your script file containing RCE payload (e.g., commands for reverse shell).

> Confirmation shows script added; trigger via reboot to execute.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[startup-scripts]]
