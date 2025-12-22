---
tags:
  - reconnaissance
  - ip-discovery
type: procedure
tools:
  - '[[tools/Censys]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bfe954e8-8d30-418e-af3c-47885f1220df
created_at: '2025-12-14T03:15:05.045Z'
updated_at: '2025-12-14T03:15:05.045Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Reconnaissance-of-Origin-IPs-with-Censys

## Summary

This procedure uses Censys to query and identify origin IP addresses associated with a target domain, revealing backend infrastructure that may be misconfigured and directly accessible.

## Description

In scenarios where load balancers or CDNs expose origin IPs through certificate transparency logs or search engines, attackers can bypass front-end protections. This targets domains like go.exchange to find Google Cloud IPs hosting internal services. Prerequisites include internet access; no authentication is needed for basic queries.

## Requirements

1. Access to Censys.io (free tier sufficient for domain queries)
2. Target domain with potential IP exposure (e.g., via DNS or certificates)
3. Basic understanding of IP ranges (e.g., 35.0.0.0/8 for GCP)

## Defense

Defensive measures and detection strategies:

- Monitor certificate transparency logs for unexpected domain associations
- Use private DNS and avoid exposing origin IPs in public queries
- Implement IP allowlisting on internal services

## Objectives

1. Gather list of origin IPs for the target domain
2. Identify cloud provider and potential internal exposure
3. Prepare for direct access attempts

## Instructions

### Step 1: Query Censys for Domain-Associated IPs

**Context**: Perform an IPv4 search on Censys to retrieve IPs linked to the domain via services or certificates.

**Command** ([[Censys Query]]):
No direct command; use web interface.

> Navigate to https://censys.io/ipv4?q=go.exchange and execute the query. Expected output: Table of IPs like 35.244.200.254 with associated services.

### Step 2: Export and Analyze Results

**Context**: Download or note IPs for further mapping.

**Command** (Manual):
```bash
# No command; copy IPs from browser
```

> Review results for subdomains or services hinted in the data.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Censys]]

## Tags

- [[Reconnaissance]]
- [[ip-discovery]]
