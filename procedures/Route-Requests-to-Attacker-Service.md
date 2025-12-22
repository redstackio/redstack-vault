---
tags:
  - traffic-interception
  - fastly
  - routing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.662Z'
sub_techniques: []
id: 886c0b0e-263e-4bb6-9e37-d145431e9331
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Route-Requests-to-Attacker-Service

## Summary

This procedure leverages DNS CNAME and CDN SNI to route all traffic for a subdomain to the attacker's service.

## Description

Once the service is created, the existing CNAME chain (registry.nodejs.org -> registry.npmjs.org -> a.sni.fastly.net) causes Fastly to match SNI headers to the attacker's service instead of the official one, due to the domain addition. This intercepts requests, as seen with 300+ npm package queries. Outcomes: Full traffic hijacking.

## Requirements

1. Active Fastly service with domain added
2. Monitoring access in Fastly logs
3. Understanding of SNI-based routing

## Defense

Defensive measures and detection strategies:

- Implement strict SNI validation in CDN configs
- Monitor for anomalous traffic spikes on subdomains
- Use certificate transparency logs to detect unauthorized certs

## Objectives

1. Exploit resolution chain for routing
2. Intercept and log incoming requests
3. Enable malicious content delivery

## Instructions

### Step 1: Activate Service

**Context**: Ensure the service is live and domains are propagated.

In Fastly dashboard, activate the service and wait ~1 minute for global propagation.

### Step 2: Monitor Incoming Traffic

**Context**: Observe requests hitting the service.

View Real-time logs in dashboard; expect HTTP requests for /<package> paths from users mistyping the registry URL.

**Expected Output**: Logs showing 300+ requests for packages like express, lodash.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[interception]]
- [[sni]]
