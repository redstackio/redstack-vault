---
tags:
  - ssrf
  - port-scanning
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Active Scanning]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Vulnerability Scanning]]'
id: 25b9d6b7-2850-4113-807e-3f0b72235585
created_at: '2025-12-14T03:46:14.360Z'
updated_at: '2025-12-14T03:46:14.360Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Perform Port Scanning via SSRF

## Summary

Uses the SSRF to scan the target's outbound TCP ports by attempting connections to attacker-server on each port, revealing filtering (e.g., port 113 blocked).

## Description

By embedding multiple <image> elements with port-specific URLs (e.g., http://attacker-server:port/test), the parser attempts fetches, generating SYN packets. This scans all 65535 ports, limited by outbound filters.

## Requirements

1. Script to generate SVG with 65535 <image> tags (may need batching due to size)
2. Attacker server listening on all ports (e.g., nc -l -p all)
3. Tools to monitor TCP SYNs (tcpdump)

## Defense

Defensive measures and detection strategies:

- Firewall outbound connections from image processors to specific ports/protocols
- Rate-limit external fetches per upload
- Detect port sweeps in logs

## Objectives

1. Map outbound port accessibility
2. Identify filtered ports like 113
3. Gather network recon

## Instructions

### Step 1: Generate Port-Specific SVG

**Context**: Create payload with port URLs.

Manually or script: <image xlink:href="http://attacker-server:1/test.png" /> ... up to :65535.

> Batch if SVG too large; upload multiple times.

### Step 2: Upload and Monitor Connections

**Context**: Trigger and capture SYNs.

Upload disguised SVG; use tcpdump on attacker: tcpdump -i any tcp portrange 1-65535.

> Expect SYNs on all except 113.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks

## Commands Used


## Tools Used


## Tags

- [[port-scan]]
- [[ssrf]]
