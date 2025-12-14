---
id: 123e4567-e89b-12d3-a456-426614174001
name: Perform-DNS-Lookup-for-Subdomain-Takeover-Discovery
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.890Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - dns-recon
commands:
  - '[[commands/nslookup-dns-lookup-for-subdomain-takeover]]'
platforms:
  - Web
tools:
  - '[[tools/nslookup]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---

# Perform-DNS-Lookup-for-Subdomain-Takeover-Discovery

## Summary

This procedure uses DNS queries to identify subdomain takeover vulnerabilities by detecting dangling CNAME records pointing to unclaimed cloud resources, such as AWS CloudFront distributions, enabling attackers to claim and control legitimate subdomains.

## Description

In the context of the Uber attack, a DNS lookup on saostatic.uber.com revealed a CNAME to an unclaimed CloudFront hostname (d3i4yxtzktqr9n.cloudfront.net), which displayed a default error page. This indicates the original service was decommissioned without removing the DNS record, leaving it vulnerable to takeover. The procedure targets public-facing web applications with cloud integrations, requiring only internet access. Expected outcomes include confirmation of takeover susceptibility, paving the way for hosting malicious content.

## Requirements

1. Access to a DNS resolver (e.g., command line or online tool)
2. Target domain/subdomain to query
3. Basic networking knowledge

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or subjack
- Implement DNS monitoring for unexpected resolutions to cloud services
- Use CAA records to restrict certificate issuance for subdomains

## Objectives

1. Discover unclaimed cloud resources linked to target subdomains
2. Confirm vulnerability to subdomain takeover
3. Gather evidence for exploitation planning

## Instructions

### Step 1: Query DNS for CNAME Record

**Context**: Perform a lookup to reveal the canonical name and check if it's unclaimed.

**Command** ([[commands/nslookup-dns-lookup-for-subdomain-takeover]]):
```bash
# nslookup saostatic.uber.com 8.8.8.8
```

> This command queries Google Public DNS (8.8.8.8) for the target subdomain. Expected output includes the CNAME (e.g., saostatic.uber.com canonical name = d3i4yxtzktqr9n.cloudfront.net.) and IP details. Follow up by visiting the resolved URL to confirm an unclaimed error page.

### Step 2: Verify Unclaimed Status

**Context**: Access the resolved hostname to check for takeover availability.

**Command** (Browser Access):
```bash
# No command; use browser: curl -I https://d3i4yxtzktqr9n.cloudfront.net
```

> Look for CloudFront's default 403/404 error indicating no distribution is configured, confirming it's claimable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques

- None

## Commands Used

- [[commands/nslookup-dns-lookup-for-subdomain-takeover]]

## Tools Used

- [[tools/nslookup]]

## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
