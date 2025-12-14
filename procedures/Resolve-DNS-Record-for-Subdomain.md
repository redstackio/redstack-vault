---
id: proc-uuid-001
name: Resolve-DNS-Record-for-Subdomain
tags:
  - dns
  - recon
  - subdomain
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-resolve-a-record]]'
verified: false
platforms:
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Scanning IP Blocks]]'
updated_at: '2025-12-14T04:51:10.932Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Scanning IP Blocks]]'
---
# Resolve-DNS-Record-for-Subdomain

## Summary

This procedure resolves the A record of a target subdomain to identify its associated IP, checking for dangling AWS Elastic IPs that can be reused for takeover attacks.

## Description

In scenarios like the Uber subdomain mta1a1.spmail.uber.com, a decommissioned resource may leave a DNS A record pointing to a released Elastic IP. Resolving this reveals the IP, which if available in AWS's pool, enables an IP-use-after-free attack. This step is reconnaissance-focused and requires no special access, only public DNS queries.

## Requirements

1. Access to a DNS resolver tool like dig
2. Knowledge of the target subdomain
3. Internet connectivity for public DNS queries

## Defense

Defensive measures and detection strategies:

- Monitor DNS records for dangling entries post-decommissioning
- Use AWS IP blacklisting or Route 53 private hosted zones to prevent reuse
- Implement DNS monitoring tools like DNSSec or anomaly detection for unexpected resolutions

## Objectives

1. Obtain the IP address tied to the subdomain
2. Verify if it's a reusable AWS Elastic IP
3. Identify potential for subdomain takeover

## Instructions

### Step 1: Query A Record

**Context**: Use dig to resolve the A record and extract the IP.

**Command** ([[commands/dig-resolve-a-record]]):
```bash
dig mta1a1.spmail.uber.com A +short
```

> This command queries the authoritative DNS server for the A record, outputting the IP (e.g., 52.XX.XX.XX). Check AWS IP ranges to confirm it's an Elastic IP.

### Step 2: Validate IP Availability

**Context**: Manually verify if the IP is active or dangling by attempting resolution multiple times or checking AWS status.

**Command** ([[commands/dig-resolve-a-record]]):
```bash
dig mta1a1.spmail.uber.com A +short
```

> Repeated queries should show the same IP; if it's dangling, it won't resolve to an active service.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Scanning IP Blocks]]

### Sub-Techniques


## Commands Used

- [[commands/dig-resolve-a-record]]

## Tools Used


## Tags

- [[DNS]]
- [[recon]]
