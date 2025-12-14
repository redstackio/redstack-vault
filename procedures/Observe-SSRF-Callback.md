---
id: proc-observe-ssrf-callback
tags:
  - callback
  - oob
  - confirmation
type: procedure
tools:
  - '[[tools/interactsh]]'
  - '[[tools/Burp-Suite-Collaborator]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:46.007Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-SSRF-Callback

## Summary

This procedure monitors the external listener for callbacks from the target server, confirming successful SSRF exploitation and potentially revealing internal details.

## Description

After sending the payload, the target server interacts with the OOB URL (e.g., via HTTP or DNS). This step checks logs for these interactions, validating the vuln and enabling further pivots like port scanning. Used post-exploitation in blind scenarios.

## Requirements

1. Active listener from setup procedure
2. Access to logs/polling interface
3. Knowledge of expected interaction types (HTTP, DNS)

## Defense

Defensive measures and detection strategies:

- Log all outbound connections and correlate with inbound requests
- Block DNS resolutions to dynamic/suspicious domains
- Use SIEM to alert on OOB patterns

## Objectives

1. Detect and log callback
2. Analyze request for internal info
3. Confirm exploitation

## Instructions

### Step 1: Poll interact.sh Logs

**Context**: Check for interactions.

No command; Use interact.sh client to view interactions.

> Look for entries showing request from target IP to payload URL.

### Step 2: Check Burp Collaborator

**Context**: View callbacks in Burp.

No command; Open Collaborator client and poll.

> Events list incoming HTTP/DNS from target, including headers/timestamps.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/interactsh]]
- [[tools/Burp-Suite-Collaborator]]

## Tags

- [[callback]]
- [[confirmation]]
