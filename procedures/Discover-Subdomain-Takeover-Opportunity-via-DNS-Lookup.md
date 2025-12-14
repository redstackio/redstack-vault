---
tags:
  - reconnaissance
  - dns
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/host-DNS-Lookup]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/host-dns-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.550Z'
sub_techniques: []
id: 4f8ba23c-f155-4b76-8c45-e6590ffa4b2d
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Subdomain-Takeover-Opportunity-via-DNS-Lookup

## Summary

This procedure uses DNS lookup tools to identify subdomain takeover vulnerabilities by detecting CNAME records pointing to inactive or unclaimed third-party services, such as Ghost.io, enabling further exploitation for domain control.

## Description

In a subdomain takeover attack, attackers scan for DNS records where a subdomain CNAME points to an external service that is no longer active or monitored by the owner. This procedure focuses on querying the target's DNS to reveal such misconfigurations, specifically checking for aliases to platforms like Ghost.io. The target environment is public DNS infrastructure, and success leads to identifying claimable subdomains for impersonation or phishing. Prerequisites include basic command-line access on a Unix-like system.

## Requirements

1. Unix-like OS (Linux/macOS) with 'host' command installed
2. Network access to perform public DNS queries
3. Target subdomain name (e.g., engineering.udemy.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or subjack
- Monitor third-party service usage and deactivate unused subdomains promptly
- Implement DNS monitoring alerts for changes in resolution

## Objectives

1. Reveal CNAME records pointing to inactive services
2. Confirm subdomain inactivity for takeover potential
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the target subdomain to extract CNAME and IP details, identifying if it aliases to an unclaimed service.

**Command** ([[commands/host-dns-lookup]]):
```bash
host engineering.udemy.com
```

> This command resolves the hostname, showing the CNAME alias (e.g., to udemy-engineering-blog.ghost.io) and associated IPs. If the IPs are generic or the service is known to be inactive, it indicates a takeover opportunity. Expected output includes the alias and IPs like 141.101.114.35.

### Step 2: Analyze Output for Vulnerability

**Context**: Review the results to confirm the service (e.g., Ghost.io) and check if the subdomain is claimable by visiting the aliased URL.

No command needed; manually inspect output and browse the CNAME target (e.g., http://udemy-engineering-blog.ghost.io) to verify inactivity (e.g., 404 or no content).

> Success if the target shows as abandoned.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/host-dns-lookup]]

## Tools Used

- [[tools/host-DNS-Lookup]]

## Tags

- [[Reconnaissance]]
- [[DNS]]
- [[subdomain-takeover]]
