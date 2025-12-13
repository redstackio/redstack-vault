---
tags:
  - xxe
  - exfiltration
type: procedure
tools:
  - '[[tools/Web-Server]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c9b1324c-f03e-448d-80da-854ab8638e0b
created_at: '2025-12-13T09:00:27.962Z'
updated_at: '2025-12-13T09:00:27.962Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Exfiltrate Data via XXE

## Summary

This procedure checks the attacker's web server logs for base64-encoded leaked data exfiltrated through the XXE vulnerability.

## Description

After triggering the XXE, the payload loads the external DTD and sends sensitive file contents (e.g., /etc/passwd) to the attacker's server logs in base64 format.

## Requirements

1. Access to web server logs
2. Successful prior upload and trigger

## Defense

Defensive measures and detection strategies:

- Monitor outbound traffic for data exfiltration
- Use intrusion detection for anomalous log patterns

## Objectives

1. Retrieve leaked sensitive data
2. Confirm successful exploitation

## Instructions

### Step 1: Monitor Server Logs

**Context**: Check for exfiltrated data.

View access logs of [[tools/Web-Server]] for base64-encoded file contents.

> Data appears due to XXE payload execution.

### Step 2: Decode Data

**Context**: Extract and decode.

Copy base64 strings from logs and decode to view original content.

> Reveals sensitive information like /etc/passwd.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Server]]

## Tags

- xxe
- exfiltration
