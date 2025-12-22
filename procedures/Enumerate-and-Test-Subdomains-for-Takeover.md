---
id: proc-uuid-002
tags:
  - enumeration
  - dns
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T04:38:39.503Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Enumerate-and-Test-Subdomains-for-Takeover

## Summary

This procedure enumerates subdomains of a target domain and tests them for subdomain takeover vulnerabilities, focusing on DNS records that may point to abandoned or misconfigured services.

## Description

Subdomain enumeration reveals the attack surface, allowing testers to check for dangling DNS records. In this scenario, inspired by prior reports, subdomains of affirm.com are checked for CNAMEs leading to unregistered TLDs, enabling takeover by registering the domain and hosting malicious content to mimic legitimate services.

## Requirements

1. Network access to public DNS resolvers
2. List of potential subdomains from reconnaissance
3. Tools for DNS querying (e.g., dig)

## Defense

Defensive measures and detection strategies:

- Conduct regular subdomain audits and remove dangling records
- Monitor DNS changes via logging and alerts
- Reserve internal TLDs and avoid pointing to public unregistered domains

## Objectives

1. List all subdomains of the target
2. Identify candidates for takeover testing
3. Flag DNS entries with potential vulnerabilities

## Instructions

### Step 1: Generate Subdomain List

**Context**: Compile a list of subdomains based on inspiration from prior reports.

Manually curate or use tools to generate subdomains like those mentioned in reports.

> Expected: A text file or list of subdomains to inspect.

### Step 2: Initial DNS Check

**Context**: Perform basic checks on enumerated subdomains for takeover indicators.

Use [[commands/dig-query-cname]] on each:

```bash
dig potential-subdomain.example.com
```

> Look for CNAMEs to third-party services or unregistered domains.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/dig-query-cname]]

## Tools Used

- [[tools/dig]]

## Tags

- [[enumeration]]
- [[DNS]]
- [[subdomain-takeover]]
