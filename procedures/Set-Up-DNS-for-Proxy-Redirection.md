---
id: proc-uuid-001
tags:
  - dns
  - redirection
  - proxy
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.570Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Set-Up-DNS-for-Proxy-Redirection

## Summary

This procedure configures a DNS record with a short TTL for a domain used in proxy injection, allowing quick updates to redirect traffic to localhost during SSRF exploitation in GitLab.

## Description

In the context of GitLab git config injection, a controllable DNS entry is needed to initially point to an external domain but later redirect to 127.0.0.1. This enables the injected http.proxy to route git clone requests to local internal services like Consul on port 8500. The short TTL (e.g., 60 seconds) minimizes propagation delays. Prerequisites include DNS control over a domain like aw.rs.

## Requirements

1. Access to DNS provider for domain aw.rs
2. Ability to set A records and TTLs
3. Network tools like dig for verification

## Defense

Defensive measures and detection strategies:

- Monitor DNS changes for short TTL records in security-relevant domains
- Implement DNS logging and anomaly detection for rapid updates
- Restrict DNS modifications to approved IPs

## Objectives

1. Create resolvable DNS entry for proxy.aw.rs
2. Ensure short TTL for fast redirection
3. Verify initial resolution before attack progression

## Instructions

### Step 1: Configure DNS Record

**Context**: Set up an A record for proxy.aw.rs with TTL 60 to an initial IP (e.g., a benign server), preparing for later localhost redirection.

**Command** (Manual DNS Update):
No specific command; use DNS provider panel or API to set A record proxy.aw.rs -> <initial-ip> TTL=60.

> Use tools like dig to verify: dig proxy.aw.rs should resolve correctly.

### Step 2: Verify DNS Setup

**Context**: Confirm the record is live and TTL is short to ensure quick future changes.

**Command** ([[commands/dig-verify-dns]]):
```bash
dig proxy.aw.rs
```

> Expected output includes TTL 60 and correct IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dns
- redirection
