---
id: proc-bypass-execution-001
tags:
  - ssrf
  - bypass
  - execution
type: procedure
tools:
  - '[[tools/libcurl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.533Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Bypassing-Request

## Summary

This procedure executes the libcurl request with the parsed URL, resulting in connection to the IPv6 address on an unintended default interface, enabling SSRF to internal resources and access control bypass.

## Description

After parsing strips the zone ID, libcurl connects to fe80::1 via the default interface instead of eth0, ignoring application-enforced restrictions. This allows access to firewall-protected internal services, potentially leaking sensitive data. Impact includes SSRF for metadata access or unauthorized service interaction. Monitor with network tools to confirm anomalous routing.

## Requirements

1. Running libcurl-based application processing the malformed URL.
2. Internal network with IPv6 services on specific interfaces.
3. Tools for traffic monitoring (e.g., tcpdump).

## Defense

Defensive measures and detection strategies:

- Enforce interface binding in application code beyond URL parsing.
- Detect cross-interface traffic anomalies via IDS.
- Patch libcurl or use wrappers for zone ID handling.

## Objectives

1. Trigger the fetch and observe routing bypass.
2. Access restricted internal resources via SSRF.
3. Confirm information leakage potential.

## Instructions

### Step 1: Trigger libcurl Fetch

**Context**: In the application context, initiate the HTTP request using the parsed URL components.

**Command** (integrated in app; simulate with curl if direct):
```bash
curl http://[fe80::1]/ --interface lo  # But libcurl uses default
```

> Request routes to default interface, bypassing eth0 restriction. Expected: Response from internal service.

### Step 2: Validate Bypass

**Context**: Check access to resources only available on specific interfaces.

Monitor with tcpdump on interfaces to see unexpected traffic.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/libcurl]]

## Tags

- ssrf
- bypass
- execution
