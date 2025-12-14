---
id: proc-uuid-2
tags:
  - user-execution
  - terminal-file
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Malicious File]]'
updated_at: '2025-12-14T17:24:08.125Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Open-Malicious-Terminal-File-in-Slack-or-Finder

## Summary

This procedure describes how a victim opens the malicious .terminal file delivered via Slack, triggering the macOS Terminal app to parse and execute its contents without additional barriers.

## Description

The attack relies on user interaction: the victim uses Shift+Click in Slack to open the file directly or downloads it to Finder and launches it. The .terminal format is natively handled by Terminal.app, which interprets the XML and runs any embedded commands. This step is user-assisted and succeeds due to the lack of quarantine flags from Slack's download process. Target environment is macOS with Slack installed; no special privileges are needed.

## Requirements

1. Victim has received and trusts the file in Slack
2. macOS Terminal app available (default on macOS)
3. No Gatekeeper blocks (enabled by prior bypass)

## Defense

Defensive measures and detection strategies:

- Educate users on risks of opening unknown files from chat apps
- Configure macOS to prompt for all unknown app executions
- Use endpoint detection to monitor Terminal.app launches from unexpected files

## Objectives

1. Initiate the execution chain by launching the file
2. Ensure seamless handover to Terminal for parsing
3. Avoid any user hesitation through lack of warnings

## Instructions

### Step 1: Direct Open in Slack

**Context**: Use Slack's built-in open functionality to launch without downloading.

Instruct the victim to hold Shift and click the file attachment in Slack chat.

> This invokes Terminal directly, parsing the XML and executing the <command> element.

### Step 2: Open via Finder After Download

**Context**: Alternative path if file is saved locally.

Download the file from Slack to Downloads folder, then double-click in Finder.

> macOS associates .terminal with Terminal.app, running the embedded script immediately.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Malicious File]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[user-execution]]
- [[terminal-file]]
