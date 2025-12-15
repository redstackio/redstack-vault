---
id: proc-relateiq-analyze-ports
tags:
  - ssrf
  - port-analysis
  - localhost
type: procedure
tools:
  - '[[tools/nmap]]'
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
updated_at: '2025-12-14T17:28:20.603Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze Responses for Open Ports

## Summary

This procedure parses SSRF scan responses to identify and document open ports on the target system, such as localhost services in RelateIQ's environment.

## Description

After sending multiple RPC requests, responses are analyzed for indicators of open ports. In the RelateIQ case, scanning localhost's top 50 ports revealed services on 80 (HTTP), 135 (RPC), 445 (SMB), 3389 (RDP), and dynamic ports 49152/49154, providing insights into internal architecture for potential lateral movement.

## Requirements

1. Collected response logs from scanning
2. Text editor or grep for pattern matching
3. Knowledge of expected response strings

## Defense

Defensive measures and detection strategies:

- Centralize application logs for response anomaly monitoring
- Use IDS to detect patterns of failed internal connections
- Regularly audit open ports on application servers

## Objectives

1. Identify open ports from response patterns
2. Map internal services
3. Assess reconnaissance value

## Instructions

### Step 1: Collect and Review Responses

**Context**: Gather all RPC responses from the scan.

Save outputs to a file:

```bash
# After each curl, append to log
curl ... >> ssrf_responses.log
```

### Step 2: Parse for Indicators

**Context**: Search for open port signatures.

Use grep to filter:

```bash
grep -i "504\|connection closed\|error occurred" ssrf_responses.log
# Cross-reference with sent ports to mark opens
```

> In RelateIQ, this identifies 80, 135, 445, 3389, 49152, 49154 as open.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/nmap]]

## Tags

- ssrf
- port-analysis
- localhost
