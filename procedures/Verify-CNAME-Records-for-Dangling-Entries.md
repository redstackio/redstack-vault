---
id: proc-uuid-2
tags:
  - dns-query
  - cname-verification
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-query]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.698Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-CNAME-Records-for-Dangling-Entries

## Summary

Query DNS CNAME records for subdomains to detect dangling pointers to expired third-party services, confirming takeover feasibility.

## Description

Dangling CNAMEs occur when DNS records point to decommissioned services without removal. For help.cloudup.com, the CNAME to cloudup.desk.com was verified, indicating an expired Desk.com account ripe for takeover.

## Requirements

1. DNS resolution access
2. Tool like dig installed
3. Target subdomain identified

## Defense

Defensive measures and detection strategies:

- Implement DNS monitoring for unresolved CNAMEs
- Automate alerts on expired service integrations
- Conduct periodic DNS audits

## Objectives

1. Confirm CNAME existence
2. Identify service endpoint
3. Validate dangling status

## Instructions

### Step 1: Query CNAME Record

**Context**: Use DNS tools to fetch the CNAME for the subdomain.

**Command** ([[commands/dig-cname-query]]):
```bash
dig cname help.cloudup.com +short
```

> This command performs a concise DNS lookup, outputting cloudup.desk.com if dangling.

### Step 2: Interpret Results

**Context**: Check if the target resolves to an active service.

Attempt to access cloudup.desk.com directly; errors suggest expiration.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-query]]

## Tools Used

- [[tools/dig]]

## Tags

- [[dns-query]]
- [[cname-verification]]
