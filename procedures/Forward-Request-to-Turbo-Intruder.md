---
id: proc-weblate-forward-intruder-001
tags:
  - forward
  - extension
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.952Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forward-Request-to-Turbo-Intruder

## Summary

This procedure transfers the captured trial request from Burp Suite to the Turbo Intruder extension for concurrent execution.

## Description

Bridging the interception to exploitation, this step loads the POST /trial/ request into Turbo Intruder. Targets the web endpoint in a Django app. Expected outcome: Request ready in the intruder's interface.

## Requirements

1. Captured request in Burp
2. Turbo Intruder extension installed in Burp
3. Active Burp session

## Defense

Defensive measures and detection strategies:

- Block rapid request bursts from single sessions
- Validate request signatures to prevent replays
- Monitor extension-like traffic anomalies

## Objectives

1. Seamlessly transfer request data
2. Enable race condition setup
3. Preserve original request integrity

## Instructions

### Step 1: Send to Extension

**Context**: Move from standard proxy to specialized intruder.

In Burp's intercept tab, right-click the held POST /trial/ request and select 'Send to Turbo Intruder'.

> The request appears in Turbo Intruder's window, with full headers and body intact for configuration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Turbo-Intruder]]

## Tags

- forward
- extension
