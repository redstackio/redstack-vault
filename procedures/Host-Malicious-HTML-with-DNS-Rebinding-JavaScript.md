---
id: 63440ef1-4c9f-4137-8b21-2f0e0d1a8832
name: Host Malicious HTML with DNS Rebinding JavaScript
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.616Z'
updated_at: '2025-12-11T06:10:15.616Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - javascript
  - dns-rebinding
commands:
  - '[[commands/flask-app-run]]'
  - '[[commands/flask-sleep]]'
  - '[[commands/flask-print-log]]'
  - '[[commands/flask-set-log-level]]'
platforms:
  - Web
tools:
  - '[[tools/Flask]]'
  - '[[tools/flask_cors]]'
  - '[[tools/XMLHttpRequest]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---

# Host Malicious HTML with DNS Rebinding JavaScript

## Summary

This procedure hosts an HTML file containing JavaScript that performs timing-based DNS rebinding to fetch internal metadata.

## Description

The JavaScript uses loops for timing, rebinds to 169.254.169.254, and exfiltrates data from GCP metadata endpoints using XMLHttpRequest.

## Requirements

1. Attacker-controlled domain for hosting
2. Ability to serve HTML/JS files
3. Integration with timing server

## Defense

Defensive measures and detection strategies:

- Enable metadata concealment in GCP
- Use network segmentation to protect metadata services

## Objectives

1. Facilitate rebinding via JavaScript
2. Fetch sensitive metadata
3. Log exfiltrated data

## Instructions

### Step 1: Create and Host HTML

**Context**: Develop JavaScript for logging, timing loops, and metadata fetching.

Host the HTML on demon.███████/ssrf.html with JS that uses [[tools/XMLHttpRequest]] for synchronous GET requests to endpoints like /computeMetadata/v1beta1/project/attributes/ssh-keys, adding header 'X-Google-Metadata-Request: True'.

> The script logs to the timing server and rebinds DNS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/XMLHttpRequest]]

## Tags

- [[JavaScript]]
- [[dns-rebinding]]
