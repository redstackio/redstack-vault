---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - reconnaissance
  - subdomain-enumeration
  - dns
  - github
type: procedure
tools:
  - '[[tools/GitHub-Recon-Techniques]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:10.607Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Hardware]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Dangling Subdomains Using GitHub Recon

## Summary

This procedure uses GitHub reconnaissance techniques to identify subdomains of a target domain that have dangling DNS records pointing to unused or decommissioned services, enabling potential subdomain takeovers.

## Description

In this attack scenario, attackers scan public GitHub repositories for configurations, secrets, or references to cloud services (e.g., GitHub Pages, Heroku) linked to the target domain. Dangling records occur when services are decommissioned without updating DNS, leaving CNAMEs resolvable but uncontrolled. This procedure targets domains like {REDACTED}.data.gov, discovering 7 such subdomains. Prerequisites include public access to GitHub and DNS tools; expected outcomes are a list of vulnerable subdomains for further exploitation.

## Requirements

1. Internet access to query GitHub API and DNS records
2. Familiarity with GitHub search syntax for repository mining
3. No credentials required, but API rate limits apply

## Defense

Defensive measures and detection strategies:

- Regularly audit and remove dangling DNS records using tools like DNS linter
- Monitor GitHub for leaked configs via secret scanning services
- Implement DNSSEC and strict CNAME validation

## Objectives

1. Enumerate subdomains via GitHub references
2. Identify dangling records pointing to claimable services
3. Prepare for takeover by listing vulnerable hosts

## Instructions

### Step 1: Search GitHub for Domain References

**Context**: Mine GitHub for repositories containing the target domain in configs or secrets, focusing on services like GitHub Pages that use CNAMEs.

Use GitHub search with the [[tools/GitHub-Recon-Techniques]] methodology:

Search query example: `org:{target-org} {REDACTED}.data.gov` or filename-based searches for `.github` workflows.

> Manually review results for DNS pointers to unused services; note potential dangling CNAMEs.

### Step 2: Query DNS for Subdomains

**Context**: Resolve identified subdomains to check for dangling records.

Use standard DNS tools like dig or nslookup to query CNAMEs:

For example, query a suspected subdomain:

```bash
dig sub.example.{REDACTED}.data.gov CNAME
```

> Expected output: CNAME to a service like `unused.github.io` that can be claimed. Repeat for multiple subdomains to identify 7+ candidates.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Hardware]] Domains

## Commands Used


## Tools Used

- [[tools/GitHub-Recon-Techniques]]

## Tags

- [[Reconnaissance]]
- [[subdomain-enumeration]]
