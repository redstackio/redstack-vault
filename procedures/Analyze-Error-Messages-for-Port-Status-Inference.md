---
tags:
  - port-scanning
  - error-analysis
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 317c02e1-3c69-4055-b5d5-d0aa608bcf2b
created_at: '2025-12-13T09:00:27.518Z'
updated_at: '2025-12-13T09:00:27.518Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze Error Messages for Port Status Inference

## Summary

This procedure involves examining variations in error messages from SSRF responses to infer the status of internal ports, effectively performing port scanning without direct access.

## Description

After triggering SSRF via XXE OOB, the server may return different error messages depending on whether the targeted internal port is open or closed. For instance, a connection to an open port might result in a timeout or specific error, while a closed port could yield a 'connection refused' message. This analysis allows attackers to map internal network services.

## Requirements

1. Collected responses from SSRF exploitation attempts
2. Basic scripting or manual review tools for comparing messages
3. Understanding of common error patterns (e.g., timeouts vs. refusals)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitize XML inputs
- Log and alert on repeated error patterns from the same source

## Objectives

1. Identify open internal ports
2. Map potential internal services for further attacks
3. Achieve internal reconnaissance

## Instructions

### Step 1: Collect and Compare Responses

**Context**: Gather all server responses from payload submissions and compare error messages.

> Manually review or use a script to diff responses. Look for patterns like 'timeout' indicating open ports vs. 'refused' for closed.

### Step 2: Infer Port Status

**Context**: Based on discrepancies, classify ports as open or closed.

> For example, if a payload targeting port 80 returns a different error than port 81, infer port 80 is open. Compile a list of open ports.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[port-scanning]]
- [[error-analysis]]
