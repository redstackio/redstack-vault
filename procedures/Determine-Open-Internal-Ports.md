---
id: proc-determine-open-ports-uber
tags:
  - port-scanning
  - ssrf
  - internal-recon
type: procedure
tools: []
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
updated_at: '2025-12-14T04:39:10.102Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Determine-Open-Internal-Ports

## Summary

This procedure maps open internal ports based on error message analysis from SSRF XXE OOB exploitation, enabling targeted follow-on attacks.

## Description

Using discrepancies from prior error analysis, this step compiles a list of accessible internal ports, such as web services on 80/443 or databases on 3306. It applies to SSRF scenarios where OOB responses indirectly confirm connectivity. Outcomes include a reconnaissance report for further exploitation.

## Requirements

1. Analysis results from error message review
2. Knowledge of common internal services and ports
3. Optional scripting for automation

## Defense

Defensive measures and detection strategies:

- Network segmentation to isolate internal services
- Intrusion detection on internal traffic patterns
- Regular vulnerability scanning for SSRF/XXE

## Objectives

1. List confirmed open ports
2. Assess potential service vulnerabilities
3. Guide subsequent attack planning

## Instructions

### Step 1: Aggregate Findings

**Context**: Compile error inferences into a port status list.

Create a markdown or text file:

Open Ports: 80 (web), 443 (https)
Closed Ports: 22 (ssh), 3306 (mysql)

> Base on patterns like successful OOB for open ports.

### Step 2: Validate and Document

**Context**: Cross-check with known services and note implications.

For open port 80, infer HTTP service exposure; for 443, TLS-enabled.

> This documentation supports chaining to service-specific exploits.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- port-scanning
- internal-recon
