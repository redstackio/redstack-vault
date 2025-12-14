---
tags:
  - dns
  - fakedns
  - bypass
type: procedure
tools:
  - '[[tools/FakeDns]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/fakedns-a-record-www]]'
  - '[[commands/fakedns-a-record-local]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:08:55.267Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1586fa6a-2be3-4464-adaf-b6fa82d2cbde
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Setup FakeDns with Malicious Records

## Summary

Configure a fake DNS server using FakeDns to resolve the main domain to a public IP and wildcard subdomains to 0.0.0.0, enabling SSRF bypass in Bitwarden.

## Description

FakeDns allows dynamic resolution control, mapping www.yourdomain.com externally for the initial fetch and *.local.yourdomain.com to localhost to evade the incomplete private IP check in IconsController.cs.

## Requirements

1. FakeDns installed (Go-based, compile from source)
2. Run as authoritative nameserver for the domain
3. Network interface bound to port 53 UDP/TCP

## Defense

Defensive measures and detection strategies:

- Validate DNS responses against trusted resolvers
- Monitor for rogue DNS servers in environment
- Use DNSSEC to prevent spoofing

## Objectives

1. Direct initial fetch to controlled server
2. Redirect subdomains to internal IPs
3. Preserve path in SSRF requests

## Instructions

### Step 1: Install FakeDns

**Context**: Download and build the tool.

```bash
go install github.com/Crypt0s/FakeDns@latest
```

> Expected: fakedns binary available.

### Step 2: Add A Records

**Context**: Configure resolutions for SSRF chain.

Execute [[commands/fakedns-a-record-www]]:

```bash
A www.yourdomain.com YOUR.PUBLIC.IP
```

Then [[commands/fakedns-a-record-local]]:

```bash
A *.local.yourdomain.com 0.0.0.0
```
Run `fakedns` to start server.

> Expected: Queries resolve as configured; test with dig.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Discovery

### Sub-Techniques


## Commands Used

- [[commands/fakedns-a-record-www]]
- [[commands/fakedns-a-record-local]]

## Tools Used

- [[tools/FakeDns]]

## Tags

- dns
- fakedns
- bypass
