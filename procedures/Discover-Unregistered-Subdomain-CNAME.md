---
tags:
  - dns
  - recon
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
platforms:
  - Web
techniques:
  - '[[Scanning IP Blocks]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6bef2c02-cb70-4717-9ea5-3f446aecdacb
created_at: '2025-12-14T04:38:39.956Z'
updated_at: '2025-12-14T04:38:39.956Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Scanning IP Blocks]]'
---
# Discover-Unregistered-Subdomain-CNAME

## Summary

This procedure involves querying DNS records to discover CNAME configurations for subdomains that point to third-party services like Fastly, identifying potential takeover opportunities when the subdomain is not properly claimed.

## Description

In a subdomain takeover attack, the first step is reconnaissance to analyze DNS records. By querying the CNAME for a target subdomain such as addons-preview-cdn.mozilla.net, the attacker reveals if it points to a CDN like addons.allizom.org on Fastly. If unclaimed, this allows external registration. This targets web environments with misconfigured DNS and CDN setups, leading to opportunities for impersonation.

## Requirements

1. Access to DNS resolution tools (e.g., dig installed on Linux/macOS)
2. Knowledge of the target domain
3. Internet connectivity for queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs to unclaimed services
- Monitor CDN provider logs for unauthorized domain registrations
- Implement DNS validation tools to alert on unresolved subdomains

## Objectives

1. Identify CNAME pointing to exploitable CDN
2. Confirm potential for takeover
3. Gather evidence for further steps

## Instructions

### Step 1: Query DNS CNAME

**Context**: Use dig to lookup the CNAME record for the target subdomain.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig CNAME addons-preview-cdn.mozilla.net
```

> This command resolves the DNS record, expecting output showing the CNAME to addons.allizom.org. Success is indicated by the alias confirmation.

### Step 2: Analyze Resolution

**Context**: Review the output to confirm Fastly hosting.

**Command** (Manual review):
No command; parse the dig output for the target service.

> Look for Fastly indicators in the resolved domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Scanning IP Blocks]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used


## Tags

- [[DNS]]
- [[recon]]
- [[subdomain-takeover]]
