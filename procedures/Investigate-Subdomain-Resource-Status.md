---
tags:
  - investigation
  - dns
  - third-party
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.721Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 571dda22-aa1e-4cd6-985a-9b0cd99dede8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Investigate Subdomain Resource Status

## Summary

This procedure checks the status of a third-party resource referenced by a subdomain's DNS record to determine if it is inactive or available for takeover.

## Description

After identifying a subdomain pointing to a third-party service, verify if the resource (e.g., a bucket or app) exists. Inactive resources allow claiming, leading to subdomain control. Targets are web domains with misconfigured DNS; prerequisites include the DNS record from reconnaissance.

## Requirements

1. DNS record details from prior recon
2. Access to the third-party service's public status or API
3. Web browser for manual checks

## Defense

Defensive measures and detection strategies:

- Monitor third-party resource deletions and update DNS promptly
- Use automated scanners for dangling DNS records
- Implement certificate transparency logs for subdomain monitoring

## Objectives

1. Confirm resource inactivity
2. Assess takeover feasibility
3. Document findings for exploitation

## Instructions

### Step 1: Re-Query DNS Record

**Context**: Confirm the subdomain's pointer to the third-party resource.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig inactive-resource.thirdparty.com
```

> Output should show if the record resolves or returns NXDOMAIN/empty, indicating inactivity.

### Step 2: Manual Status Check

**Context**: Visit the resource URL or service dashboard to verify existence.

No command; use browser: Navigate to http://inactive-resource.thirdparty.com. If 404 or no content, it's inactive.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used


## Tags

- [[investigation]]
- [[DNS]]
- [[third-party]]
