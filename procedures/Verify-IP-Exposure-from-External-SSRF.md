---
id: proc-tumblr-ip-exposure-001
tags:
  - ssrf
  - ip-exposure
  - recon
  - tumblr
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:39:09.732Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify-IP-Exposure-from-External-SSRF

## Summary

This procedure analyzes logs from the external SSRF test to extract and verify the internal IP address of the Tumblr backend server.

## Description

Upon successful external SSRF, the source IP of the incoming request to the attacker's server reveals internal infrastructure details. In this case, the IP 74.114.154.11 belongs to Automattic (Tumblr's parent, AS2635, range 74.114.152.0/22). This reconnaissance step aids in mapping the target's network without direct access.

## Requirements

1. Logs from external server callback
2. IP lookup tools (e.g., whois)

## Defense

Defensive measures and detection strategies:

- Use NAT or proxies to mask internal IPs in outbound requests
- Monitor for unexpected outbound connections from application servers
- Implement IP allowlisting for external callbacks

## Objectives

1. Identify backend server IP
2. Confirm ownership and range
3. Gather intel for further attacks

## Instructions

### Step 1: Review Server Logs

**Context**: Extract source IP from access logs.

No command; grep logs for remote_addr or similar.

> Log entry shows source IP: 74.114.154.11 connecting to /test.

### Step 2: Verify IP Details

**Context**: Confirm the IP's attribution.

Use whois 74.114.154.11 to check ownership.

> Output: NetRange: 74.114.152.0 - 74.114.155.255, Organization: Automattic, Inc., ASNumber: 2635.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- ip-exposure
- recon
- tumblr
