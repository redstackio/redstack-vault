---
tags:
  - cname-check
  - dns
  - azure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud (Azure)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:39:02.019Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9e1d3fab-dc12-4dcd-a35d-d1457978aa4c
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Check CNAME Records for Azure Services

## Summary

This procedure inspects CNAME records of enumerated subdomains to identify those pointing to Azure Websites (azurewebsites.net), flagging potential dangling records for takeover.

## Description

Dangling CNAMEs occur when a subdomain points to a cloud resource that no longer exists or is unclaimed. By querying each subdomain's DNS, attackers can spot pointers to services like Azure App Services. In this case, datacafe-cert.starbucks.com's CNAME to s00397nasv101-datacafe-cert.azurewebsites.net was identified as vulnerable.

## Requirements

1. List of subdomains from prior enumeration
2. DNS query capabilities
3. Knowledge of Azure naming conventions

## Defense

Defensive measures and detection strategies:

- Regularly scan for dangling DNS records using tools like dnsdumpster
- Implement automated alerts for NXDOMAIN on CNAME targets
- Remove unused CNAMEs promptly

## Objectives

1. Detect cloud service pointers in DNS
2. Isolate Azure-specific dangling candidates
3. Document targets for verification

## Instructions

### Step 1: Query CNAME for Each Subdomain

**Context**: Use DNS tools to fetch CNAME records for subdomains.

**Command** (Using dig):

```bash
dig +short CNAME datacafe-cert.starbucks.com
```

> Returns s00397nasv101-datacafe-cert.azurewebsites.net if present.

### Step 2: Filter for Azure Targets

**Context**: Parse results to match azurewebsites.net patterns.

**Command** (Scripted grep):

```bash
grep -i azurewebsites subdomains_cnames.txt
```

> Lists matching subdomains for further action.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Network Information

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-cname-query]]
- [[grep-filter]]

## Tools Used

- None specific

## Tags

- [[cname-check]]
- [[DNS]]
