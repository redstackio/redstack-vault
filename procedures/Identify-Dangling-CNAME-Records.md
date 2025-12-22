---
tags:
  - dns
  - cname
  - dangling
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T04:51:10.736Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7a015574-2a63-4c66-9a9d-7ae2fe4a89ea
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Identify-Dangling-CNAME-Records

## Summary

This procedure detects subdomains with CNAME records pointing to third-party services like Feed.Press that lack active accounts, enabling potential takeovers.

## Description

Dangling DNS records occur when a CNAME points to a service (e.g., redirect.feedpress.me) but no account claims it. For podcasts.slack-core.com, this misconfiguration allows anyone to register and control the subdomain, leading to arbitrary content serving on port 80.

## Requirements

1. DNS query access
2. Knowledge of third-party services (e.g., Feed.Press for RSS/podcasts)
3. Ability to check service dashboards for domain availability

## Defense

Defensive measures and detection strategies:

- Automate DNS audits to flag unclaimed CNAMEs
- Remove or secure dangling records promptly
- Monitor third-party service logs for unauthorized claims

## Objectives

1. Locate misconfigured DNS entries
2. Confirm lack of active service association
3. Prepare for takeover exploitation

## Instructions

### Step 1: Query Subdomain DNS

**Context**: Check for CNAME records on suspected subdomains.

Use [[commands/dig-dns-lookup]]:

```bash
dig podcasts.slack-core.com
```

> Reveals CNAME to redirect.feedpress.me.

### Step 2: Verify Service Claim

**Context**: Confirm no active account on the service.

Manually visit Feed.Press and attempt to search for the domain.

> Expected: Domain unclaimed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Software Discovery

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[cname]]
