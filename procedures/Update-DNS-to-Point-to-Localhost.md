---
id: proc-uuid-004
tags:
  - dns
  - redirection
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
updated_at: '2025-12-14T03:53:38.550Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Update-DNS-to-Point-to-Localhost

## Summary

This procedure updates the DNS record for the proxy domain to resolve to 127.0.0.1, hijacking the injected git proxy to route to local internal services.

## Description

After project creation, change the A record for proxy.aw.rs to localhost. Short TTL ensures quick propagation, allowing the next git clone (via mirror) to SSRF through the proxy to port 8500.

## Requirements

1. DNS control for aw.rs
2. Initial DNS setup from prior step
3. Verification tools like dig

## Defense

Defensive measures and detection strategies:

- Alert on DNS updates to localhost IPs
- Rate-limit DNS changes
- Use DNSSEC to prevent unauthorized updates

## Objectives

1. Redirect proxy.aw.rs to 127.0.0.1
2. Wait for propagation
3. Confirm resolution

## Instructions

### Step 1: Update DNS Record

**Context**: Modify A record to point proxy.aw.rs to 127.0.0.1 via DNS provider.

**Command** (Manual Update):
No CLI; use DNS panel to set A record proxy.aw.rs -> 127.0.0.1 TTL=60.

> Wait 1-2 minutes for propagation.

### Step 2: Verify Redirection

**Context**: Check that DNS now resolves to localhost.

**Command** ([[commands/dig-verify-dns]]):
```bash
dig proxy.aw.rs
```

> Expected output: IP 127.0.0.1.

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
