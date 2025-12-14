---
tags:
  - dns-verification
  - unclaimed-resource
  - azure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Cloud (Azure)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.011Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5ff06e6d-231b-47bc-b928-53131e462071
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify Unclaimed Azure App Service via DNS

## Summary

This procedure confirms if an Azure App Service targeted by a CNAME is unclaimed by querying its DNS for an NXDOMAIN response, indicating availability for registration.

## Description

Unclaimed cloud resources respond with NXDOMAIN when queried directly, as they are not provisioned. For s00397nasv101-datacafe-cert.azurewebsites.net, this verification step ensures the dangling CNAME can be exploited via takeover.

## Requirements

1. CNAME target name (e.g., s00397nasv101-datacafe-cert.azurewebsites.net)
2. DNS resolver access
3. Understanding of Azure DNS behavior

## Defense

Defensive measures and detection strategies:

- Monitor for NXDOMAIN queries on internal resources
- Use Azure Monitor to track unregistered App Service names
- Conduct periodic DNS audits

## Objectives

1. Validate resource availability
2. Confirm takeover feasibility
3. Avoid false positives

## Instructions

### Step 1: Direct DNS Query on Target

**Context**: Query the exact Azure App Service name to check resolution.

**Command** (Using dig):

```bash
dig +short s00397nasv101-datacafe-cert.azurewebsites.net
```

> NXDOMAIN response indicates unclaimed status.

### Step 2: Cross-Verify with Azure Portal

**Context**: Optionally check Azure's public endpoint for confirmation.

**Command** (Browser or curl):

```bash
curl -I https://s00397nasv101-datacafe-cert.azurewebsites.net/
```

> 404 or connection error confirms unclaimed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-nxdomain-check]]
- [[commands/curl-verify]]

## Tools Used

- None specific

## Tags

- [[dns-verification]]
- [[unclaimed-resource]]
