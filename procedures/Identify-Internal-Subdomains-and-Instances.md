---
tags:
  - discovery
  - subdomain-enumeration
type: procedure
tools:
  - '[[tools/Censys]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 351dffab-3425-4fee-a9fe-70e517411bc2
created_at: '2025-12-14T03:15:05.044Z'
updated_at: '2025-12-14T03:15:05.044Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Internal-Subdomains-and-Instances

## Summary

This procedure analyzes reconnaissance data to map internal subdomains and development instances to exposed origin IPs, identifying targets like PgHero for exploitation.

## Description

Following IP discovery, manual or semi-automated analysis reveals internal naming conventions (e.g., dev-go.exchange subdomains). This exposes misconfigured services without proper Host validation. Targets cloud environments where development instances are inadvertently public.

## Requirements

1. List of origin IPs from prior reconnaissance
2. Knowledge of common internal subdomain patterns (e.g., *.dev-*)
3. Access to tools for header manipulation testing

## Defense

Defensive measures and detection strategies:

- Enforce strict Host header validation on all services
- Use internal-only DNS for development subdomains
- Regularly audit exposed IPs with tools like Shodan or Censys

## Objectives

1. Associate IPs with specific internal services
2. Identify vulnerable instances like PgHero or Grafana
3. Prioritize targets based on sensitivity

## Instructions

### Step 1: Review Censys Output for Subdomain Hints

**Context**: Examine query results for any embedded subdomain data or certificates.

**Command** (Manual Analysis):
```bash
# No command; parse JSON export if available
```

> Look for patterns like pghero.dev-go.exchange on IP 35.244.200.254.

### Step 2: Cross-Reference with Known Services

**Context**: Match IPs to services such as PostgreSQL tools or monitoring dashboards.

**Command** (Manual):
```bash
# Document mappings in a file
echo "35.244.200.254: pghero.dev-go.exchange" >> ip_mappings.txt
```

> Expected output: Text file with IP-subdomain pairs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Host Information: Hardware

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Censys]]

## Tags

- [[Discovery]]
- [[subdomain-enumeration]]
