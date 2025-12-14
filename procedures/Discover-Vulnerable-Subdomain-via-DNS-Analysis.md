---
tags:
  - dns
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-query]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:31.275Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 885a6cb9-d245-4499-9440-3359085e06b0
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Vulnerable-Subdomain-via-DNS-Analysis

## Summary

This procedure identifies subdomains with misconfigured DNS records pointing to external services like GitHub, enabling potential subdomain takeovers by revealing dangling pointers.

## Description

In a subdomain takeover attack, attackers scan for subdomains whose DNS records (e.g., CNAME) point to third-party services without active claims. For dev.rbk.money, the DNS was set to GitHub's infrastructure but unassociated with any repository, leaving it vulnerable. This step involves enumerating subdomains and querying their records to spot such issues. Prerequisites include public DNS access; expected outcome is a list of potentially takeover-able subdomains.

## Requirements

1. Access to DNS resolution tools (e.g., dig installed on Linux/macOS)
2. Target domain name (e.g., rbk.money)
3. Basic knowledge of DNS record types (CNAME, A)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like DNSdumpster or automated scanners
- Implement domain monitoring services (e.g., Certificate Transparency logs) to detect unused subdomains
- Use services like GitHub's domain verification to claim and secure pointers proactively

## Objectives

1. Enumerate and identify target subdomains
2. Analyze DNS for unclaimed service pointers
3. Flag vulnerabilities for further verification

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use subdomain enumeration to find potential targets like dev.rbk.money. Tools like subfinder can be used, but here we focus on manual DNS query post-enumeration.

Assume subdomains are listed; proceed to query.

### Step 2: Query DNS Records

**Context**: Execute a DNS lookup to reveal CNAME records pointing to services like GitHub.

**Command** ([[commands/dig-dns-query]]):
```bash
dig dev.rbk.money CNAME
```

> This command queries the CNAME record. Expected output includes lines like "dev.rbk.money. 3600 IN CNAME github.map.fastly.net." indicating a GitHub pointer. If it resolves to unclaimed infrastructure, note it as vulnerable.

### Step 3: Validate Resolution

**Context**: Check if the subdomain resolves to active content or errors.

Use curl or browser to visit http://dev.rbk.money and look for 404 or service-specific errors.

**Command** ([[commands/curl-http-check]]):
```bash
curl -I http://dev.rbk.money
```

> Look for HTTP 404 or GitHub-specific headers confirming no claim.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-query]]
- [[commands/curl-http-check]]

## Tools Used


## Tags

- [[DNS]]
- [[Reconnaissance]]
