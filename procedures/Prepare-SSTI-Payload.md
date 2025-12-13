---
tags:
  - payload
  - ssti
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/encode-uri-component-payload]]'
platforms:
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a45790b0-f5ea-4137-af27-c430f981db77
created_at: '2025-12-13T09:01:16.895Z'
updated_at: '2025-12-13T09:01:16.895Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Prepare SSTI Payload

## Summary

This procedure encodes an ERB template payload containing a command injection for safe inclusion in a URL parameter.

## Description

The payload "<% `touch me` %>" is encoded using encodeURIComponent to prevent URL parsing issues, preparing it for injection into the content parameter of the /echo endpoint.

## Requirements

1. JavaScript console or tool for encoding
2. Knowledge of ERB syntax

## Defense

Defensive measures and detection strategies:

- Input sanitization in templates
- Monitor for encoded payloads in requests

## Objectives

1. Create URL-safe SSTI payload
2. Enable command execution via template

## Instructions

### Step 1: Encode Payload

**Context**: Generate encoded string.

**Command** ([[commands/encode-uri-component-payload]]):
```bash
encodeURIComponent("<% `touch me` %>")
```

> Produces "%3C%25%20%60touch%20me%60%20%25%3E".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/encode-uri-component-payload]]

## Tools Used



## Tags

- payload
- ssti
