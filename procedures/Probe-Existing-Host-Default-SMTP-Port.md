---
id: proc-nextcloud-probe-smtp-port-001
tags:
  - ssrf
  - port-scan
  - smtp-probe
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
updated_at: '2025-12-14T04:39:02.074Z'
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
# Probe-Existing-Host-Default-SMTP-Port

## Summary

This procedure tests an existing internal host's default SMTP port (25) via Nextcloud SSRF, confirming host liveness and port openness through successful test email delivery.

## Description

Using an IP like 172.17.0.1 with default port, the server-side request succeeds if the SMTP service responds, directly validating service availability. This escalates reconnaissance by pinpointing active internal servers.

## Requirements

1. Prior successful segment probes
2. Suspected live IP
3. SMTP mode configured

## Defense

Defensive measures and detection strategies:

- Firewall rules to block internal connections from app servers
- Disable test email in production
- Anomaly detection on SMTP traffic from web apps

## Objectives

1. Verify host existence
2. Confirm SMTP port open
3. Identify potential mail relay targets

## Instructions

### Step 1: Enter Host IP

**Context**: Target a likely existing host.

Input '172.17.0.1' as server address.

> Field populates.

### Step 2: Default Port Test

**Context**: Leave port empty to use 25.

Do not specify port; send test email.

> Test succeeds if port open.

### Step 3: Validate Success

**Context**: Confirm via email delivery.

Check for success message.

> Indicates live host and open port.

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
- [[smtp-probe]]
