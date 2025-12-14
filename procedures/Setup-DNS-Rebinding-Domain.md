---
tags:
  - dns-rebinding
  - bypass
type: procedure
tools:
  - '[[tools/1u-ms]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.898Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 11af1a7c-5ad7-44de-a165-78ae35a5d466
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup DNS Rebinding Domain

## Summary

Configure a DNS rebinding domain using an external service to initially resolve to an allowed external IP and then to the internal AWS metadata IP, bypassing static IP checks.

## Description

DNS rebinding tricks the server into resolving the same domain to different IPs over time. Using a service like 1u.ms, set a short TTL (e.g., 1 second) for initial external resolution (bypassing whitelist), followed by rebinding to 169.254.169.254. This exploits the timing between IP check and actual fetch in the CMS backend.

## Requirements

1. Access to DNS rebinding service account
2. Target internal IP (169.254.169.254)
3. Timing control for rebinding

## Defense

Defensive measures and detection strategies:

- Implement DNS pinning or fixed TTL enforcement
- Block short TTL domains or known rebinding services
- Use multiple IP resolutions before fetch

## Objectives

1. Create rebinding domain for SSRF bypass
2. Test rebinding functionality
3. Prepare for exploitation

## Instructions

### Step 1: Register Domain on 1u.ms

**Context**: Use the service to create a custom rebinding domain.

Visit http://1u.ms/ and configure: Initial IP 8.8.8.8 (1s TTL), rebind to 169.254.169.254.

> Expected: Generated domain like rebind.1u.ms.

### Step 2: Verify Rebinding

**Context**: Test resolution changes.

Use `dig rebind.1u.ms` repeatedly to observe IP switch.

> Expected: First query external, subsequent internal.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/1u-ms]]

## Tags

- [[dns-rebinding]]
