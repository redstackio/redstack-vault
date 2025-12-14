---
tags:
  - dns
  - blackhole
  - timeout
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
  - POSIX
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:18.698Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ca16b48f-f7aa-4a74-ba7c-7ede1a4deb3f
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Configure DNS to Blackhole Server

## Summary

Redirects DNS queries to a non-responsive blackhole server to simulate timeouts and trigger the libcurl race condition.

## Description

By pointing resolv.conf to 3.219.212.117 (blackhole.webpagetest.org), DNS resolutions fail to respond, forcing the 2-second timeout in the multi-threaded example and activating the vulnerable sigjmp_buf handling.

## Requirements

1. Root or sudo access for /etc/resolv.conf
2. Network connectivity (ironically, to set up failure)

## Defense

Defensive measures and detection strategies:

- Monitor DNS config changes; use hardened resolvers like systemd-resolved
- Detect anomalous DNS servers in logs
- Implement fallback DNS for reliability

## Objectives

1. Force DNS timeouts in test environment
2. Simulate real-world resolution failures
3. Enable race condition during concurrent queries

## Instructions

### Step 1: Edit DNS Configuration

**Context**: Update resolver to blackhole IP.

**Command** (Sudo Edit):
```bash
sudo sh -c 'echo "nameserver 3.219.212.117" > /etc/resolv.conf'
```

> Sets DNS to non-responsive server. Expected output: resolv.conf updated; test with dig to confirm timeout.

### Step 2: Verify Timeout

**Context**: Test DNS failure.

**Command** (Dig Test):
```bash
dig example.com
```

> Should timeout without response. Expected output: Query timeout after ~2s.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dns-config
- simulation
- timeout

