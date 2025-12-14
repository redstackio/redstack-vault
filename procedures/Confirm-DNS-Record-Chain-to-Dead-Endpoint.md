---
tags:
  - dns-tracing
  - endpoint-verification
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-trace-dns]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.771Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 12f08287-5d38-4295-9e0e-194bf8a4610a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Confirm-DNS-Record-Chain-to-Dead-Endpoint

## Summary

This procedure traces the full DNS resolution chain for a suspicious subdomain to confirm it leads to a decommissioned and claimable endpoint.

## Description

By manually walking the CNAME and A record chain, attackers verify the misconfiguration. In Azure scenarios, this reveals pointers to dead CloudApp VMs. Outcomes: Confirmation of dead status via no response. Requires basic DNS tools.

## Requirements

1. DNS resolution tools like dig or nslookup
2. Identified subdomain from enumeration
3. Public DNS access

## Defense

Defensive measures and detection strategies:

- Audit DNS chains periodically with scripts
- Remove stale CNAMEs in Azure Traffic Manager
- Log and alert on repeated queries to dead endpoints

## Objectives

1. Map full resolution path
2. Verify endpoint inactivity
3. Assess claimability

## Instructions

### Step 1: Trace DNS Chain

**Context**: Start with the subdomain and follow CNAMEs.

**Command** ([[commands/dig-trace-dns]]):
```bash
dig +trace svcardproxydevus.starbucks.com
```

> Reveals chain: svcardproxydevus.starbucks.com -> s00307ntmp0svcardproxydev0.trafficmanager.net -> s00307dpipsvcardproxy00.eastus.cloudapp.azure.com.

### Step 2: Probe Endpoint

**Context**: Check if the final endpoint responds.

**Command** ([[commands/dig-trace-dns]]):
```bash
dig s00307dpipsvcardproxy00.eastus.cloudapp.azure.com
```

> Expected: Resolution to IP but no HTTP service (timeout or 404), confirming dead.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-trace-dns]]

## Tools Used


## Tags

- [[dns-tracing]]
