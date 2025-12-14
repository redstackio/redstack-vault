---
id: proc-phpbb-iterate-scanning-001
tags:
  - port-scanning
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:29:10.140Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Iterate-SSRF-for-Port-Scanning

## Summary

This procedure repeats the SSRF trigger across multiple ports and internal IPs to conduct comprehensive port scanning and service enumeration on the server or network.

## Description

By cycling through ports (e.g., 1-1024 or known service ports) and IPs (e.g., 127.0.0.1, 10.0.0.0/8), attackers map open services using phpBB's unvalidated connections. In phpBB 3.3.1, error responses aggregate to reveal network topology. Requires admin access and prior single-port test. Outcomes: Full scan results for internal recon.

## Requirements

1. Functional SSRF trigger from previous steps
2. List of ports/IPs to test (e.g., common services: 22, 80, 3306)
3. Patience for manual iterations (automatable if API-wrapped, but form-based here)

## Defense

Defensive measures and detection strategies:

- Rate-limit ACP submissions to prevent scanning
- Block all internal outbound connections from web server via network ACLs
- Alert on anomalous localhost connection attempts in app logs

## Objectives

1. Scan multiple ports systematically
2. Enumerate services across internal network
3. Compile reconnaissance data

## Instructions

### Step 1: Modify Port and Resubmit

**Context**: Test next port in sequence.

Change 'Jabber port' to next value (e.g., from 2222 to 3306), submit, and note response.

> Expected output: Updated error for new port.

### Step 2: Target Different Internal IPs

**Context**: Extend to network scanning.

Set 'jabber server' to internal IP (e.g., 192.168.1.1), specify port, and submit repeatedly.

> Expected output: Responses indicating network service status.

### Step 3: Document Results

**Context**: Aggregate findings for analysis.

Record open ports and service inferences from errors.

> Expected output: List of open services, e.g., SSH on 2222, MySQL on 3306.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- port-scanning
- ssrf
