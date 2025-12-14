---
tags:
  - dns
  - reconnaissance
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:49.274Z'
sub_techniques: []
id: c99455c9-d709-4d3a-a8b3-724029b46404
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify Dangling DNS Record for Takeover

## Summary

This procedure performs a DNS lookup to confirm that a target subdomain is dangling (unused but configured) and points via CNAME to GitLab's Pages infrastructure, a prerequisite for subdomain takeover attacks.

## Description

In subdomain takeover scenarios, attackers identify domains with DNS records pointing to external services like GitLab Pages but no active hosting. This procedure uses DNS queries to verify the CNAME record, ensuring the domain resolves to gitlab-com.gitlab.io. It's typically the first step in reconnaissance for GitLab-specific takeovers, enabling subsequent claiming of the domain without ownership verification. Expected outcomes include confirmation of exploitability, with impacts like serving malicious content on victim subdomains for phishing or data theft.

## Requirements

1. Access to a DNS resolution tool like dig (available on Linux/macOS or via online alternatives)
2. Knowledge of the target dangling subdomain (e.g., from prior subdomain enumeration)
3. Network connectivity for DNS queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or internal scanners
- Implement DNS monitoring for unexpected resolutions to third-party services like GitLab
- Enforce strict domain verification in hosting platforms and automate removal of unused records

## Objectives

1. Confirm CNAME points to vulnerable infrastructure (gitlab-com.gitlab.io)
2. Validate dangling status (no active content)
3. Identify takeover opportunities for further exploitation

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the target domain to retrieve its CNAME and A records, verifying the pointer to GitLab Pages.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig docs-dev.gitlab.com
```

> This command resolves the domain's records. Look for a CNAME to gitlab-com.gitlab.io and an A record to an IP like 35.185.44.232. If present without active hosting, the domain is dangling and takeover-ready.

### Step 2: Analyze Output for Vulnerability

**Context**: Manually inspect the output to confirm exploitability; automate with scripts for larger scans.

**Command** (No specific command; parse output):

> Expected: CNAME confirmation. If resolved differently, the domain is not vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[Reconnaissance]]
- [[subdomain-takeover]]
