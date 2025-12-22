---
id: proc-nextcloud-probe-nonexistent-001
tags:
  - ssrf
  - host-discovery
  - non-existent-probe
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:39:02.078Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Probe-Non-Existent-IP-via-SMTP

## Summary

This procedure probes a non-existent or closed internal IP using Nextcloud's SMTP field, where error messages disclose that the host does not exist or has no open ports, enabling passive host discovery.

## Description

Inputting an IP like 172.17.0.0 triggers a server-side connection attempt, resulting in a hint about non-existence. This builds on prior access and helps map empty address spaces in the internal network, useful in reconnaissance for identifying live vs. dead hosts.

## Requirements

1. SMTP settings interface open
2. List of potential internal IPs to test
3. Admin session active

## Defense

Defensive measures and detection strategies:

- Input validation to reject invalid or internal IPs
- Rate-limit test email functions
- Monitor for patterns of failed SMTP connections

## Objectives

1. Confirm host non-existence
2. Differentiate from port-closed errors
3. Narrow down live IP ranges

## Instructions

### Step 1: Input Non-Existent IP

**Context**: Select and enter an IP unlikely to resolve.

Enter '172.17.0.0' in the server address field.

> Input is accepted.

### Step 2: Initiate Probe

**Context**: Force the SSRF via configuration test.

Send test email.

> Response: Hint that address does not exist or no open ports.

### Step 3: Document Findings

**Context**: Record for topology mapping.

Capture the exact error text.

> Indicates dead space in the network.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[host-discovery]]
- [[non-existent-probe]]
