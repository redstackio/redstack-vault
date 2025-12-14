---
id: tool-hetzner-vps
url: 'https://www.hetzner.de/us/hosting/produktmatrix_vserver/vserver-produktmatrix'
tags:
  - vps
  - cloud
  - ipv6
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.752Z'
validated: true
submitted: true
---
# Hetzner-VPS

**Status**: Unverified

## Overview

Cloud VPS provider offering affordable instances with large IPv6 subnets for network-intensive tasks like IP rotation in attacks.

## Description

Hetzner provides CX11 plan (512 MB RAM, 1 CPU, 20 GB SSD, 100 Mbit/s, $3.9/month) with /64 IPv6 subnet (18 quintillion addresses). Ideal for assigning multiple IPs to one interface for bypassing rate limits.

## Features

- Feature 1: /64 IPv6 subnet per VPS
- Feature 2: Low cost, high bandwidth
- Feature 3: OpenVZ-based with venet0 interface

## Installation

### Requirements

- Hetzner account

### Install Commands

N/A (web provisioning)

## Basic Usage

Provision via dashboard, SSH in, configure IPs.

### Common Options

| Option | Description |
|--------|-------------|
| CX11 | Basic plan with IPv6 |

## Examples

### Example 1: Basic Usage

Create VPS, add IPv6:

```bash
# Post-provision: ip addr add <ipv6>/64 dev venet0
```

### Example 2: Advanced Usage

Script bulk add:

```bash
for i in {1..500}; do ip addr add 2a04:XXXX:0:32::${i}/64 dev venet0; done
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic from Hetzner IP ranges (e.g., 5.75.0.0/16)
- Sequential IPv6 from /64 blocks

## Related Procedures

- [[procedures/Setup-VPS-with-IPv6-Addresses]]

## Related Tools

- [[tools/RamNode]]
- [[tools/Vultr]]

## References

- https://www.hetzner.com
