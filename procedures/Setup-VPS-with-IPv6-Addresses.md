---
id: proc-setup-vps-ipv6
tags:
  - vps
  - ipv6
  - ip-rotation
type: procedure
tools:
  - '[[tools/Hetzner-VPS]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Connection Proxy]]'
updated_at: '2025-12-14T17:31:52.790Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Connection Proxy]]'
---
# Setup-VPS-with-IPv6-Addresses

## Summary

This procedure provisions a low-cost VPS with a large IPv6 subnet to enable IP address rotation, bypassing per-IP rate limits in brute-force attacks.

## Description

Using Hetzner VPS (512 MB RAM, 1 CPU, $3.9/month), a /64 IPv6 subnet provides 18 quintillion addresses. Configure 500+ addresses on the venet0 interface, ensuring 4+ seconds between reuses to avoid blocks. This setup allows scaling brute-force attempts without triggering limits.

## Requirements

1. VPS provider account (e.g., Hetzner) with IPv6 support
2. SSH access to VPS
3. Basic Linux networking knowledge

## Defense

Defensive measures and detection strategies:

- Rate limit at account or global level, not just IP
- Detect traffic from VPS IP ranges or IPv6 bursts
- Block known VPS providers in high-security endpoints

## Objectives

1. Assign multiple IPv6 addresses to a single interface
2. Enable rotation for parallel requests
3. Maintain stealth by spacing IP reuses

## Instructions

### Step 1: Provision VPS

**Context**: Create and deploy the VPS instance.

No command; use provider dashboard to select CX11 plan with IPv6.

> Expected: VPS IP (IPv4/IPv6) assigned, SSH login successful.

### Step 2: Configure IPv6 Addresses

**Context**: Add multiple IPv6 addresses to venet0.

Use provider tools or scripts to assign from /64 subnet (e.g., 2a04:XXXX:0:32::/64).

```bash
# Example: Add addresses via ifconfig or ip command (provider-specific)
ip addr add 2a04:XXXX:0:32::1001/64 dev venet0
```

> Repeat for 500+ addresses. Expected: Addresses bound to interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Connection Proxy]] Proxy

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Hetzner-VPS]]

## Tags

- [[vps]]
- [[ipv6]]
- [[ip-rotation]]
