---
id: proc-nextcloud-probe-closed-port-001
tags:
  - ssrf
  - port-scan
  - closed-port-probe
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
updated_at: '2025-12-14T04:39:02.061Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Probe-Existing-Host-Non-Open-Port-via-SMTP

## Summary

This procedure probes a non-open port (e.g., 22) on a known existing host using Nextcloud's SMTP SSRF, where errors distinguish host liveness from port inaccessibility.

## Description

Specifying port 22 on IP 172.17.0.1 triggers a failed connection, but the message confirms the host exists while the port is closed. This refines port scanning without external tools, exposing service footprints.

## Requirements

1. Confirmed live host from prior probe
2. Target port (e.g., 22 for SSH)
3. Active admin session

## Defense

Defensive measures and detection strategies:

- Port-specific firewalls for internal services
- Application-level port validation in configs
- Log analysis for unusual port tests in SMTP

## Objectives

1. Map closed ports on live hosts
2. Infer running services indirectly
3. Complete port reconnaissance

## Instructions

### Step 1: Input Host and Port

**Context**: Combine known host with test port.

Enter '172.17.0.1' as address and '22' as port.

> Configuration accepts values.

### Step 2: Execute Probe

**Context**: Trigger SSRF connection attempt.

Send test email.

> Error: Address exists but port not accessible.

### Step 3: Interpret Results

**Context**: Use response for intel.

Note distinction between host and port status.

> Reveals potential other open ports to test.

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
- [[port-scan]]
- [[closed-port-probe]]
