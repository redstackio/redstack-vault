---
id: proc-nextcloud-probe-segment-001
tags:
  - ssrf
  - network-recon
  - segment-probe
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
updated_at: '2025-12-14T04:39:02.082Z'
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
# Probe-Different-Network-Segment-via-SMTP

## Summary

This procedure uses the Nextcloud SMTP server address field to probe an IP on a different network segment, eliciting error messages that confirm segment separation and aid in mapping internal topology.

## Description

By entering an IP like 172.17.1.0 (assuming the server is on 172.17.0.x), the application attempts a server-side connection, returning a specific hint about network mismatch. This SSRF variant requires admin access and reveals infrastructure boundaries without direct network tools. Expected outcomes include confirmation of isolated segments in multi-tenant setups.

## Requirements

1. Access to Nextcloud SMTP settings (from prior procedure)
2. Knowledge of suspected internal IP ranges
3. Admin privileges

## Defense

Defensive measures and detection strategies:

- Whitelist only external SMTP providers in the address field
- Log and alert on test email attempts with internal IPs
- Network segmentation to limit SSRF reach

## Objectives

1. Identify network segment boundaries
2. Confirm isolation from target IPs
3. Gather topology intel for further probes

## Instructions

### Step 1: Enter Target IP

**Context**: Input an IP from a different segment to trigger SSRF probe.

In the SMTP server address field, enter '172.17.1.0'.

> The field accepts the input without validation.

### Step 2: Trigger Test Connection

**Context**: Attempt a test email to force the server-side request.

Click "Send test email" or save and test the configuration.

> Error message displays: hint indicating not on the same network segment.

### Step 3: Analyze Response

**Context**: Interpret the error for reconnaissance value.

Note the specific wording about network segments.

> Success: Reveals relative positioning without full access.

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
- [[network-recon]]
- [[segment-probe]]
