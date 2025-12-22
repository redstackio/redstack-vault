---
id: proc-uuid-001
tags:
  - subdomain-enumeration
  - reconnaissance
  - dns
type: procedure
tools:
  - '[[tools/knockpy]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/knockpy-enumerate-subdomains]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:23.006Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Subdomain-Enumeration-with-Knockpy

## Summary

This procedure uses the knockpy tool to perform brute-force and permutation-based subdomain enumeration on a target domain, uncovering hidden subdomains that may indicate vulnerabilities like dangling DNS records for takeover.

## Description

In offensive security testing, subdomain enumeration is a critical reconnaissance step to map the attack surface. Knockpy leverages wordlists and permutations to query DNS records, identifying subdomains such as those pointing to third-party services like Heroku. In this scenario, it revealed 'www.gratipay.com.herokudns.com', a potential dangling record from a deleted Heroku app. Prerequisites include Python 3 and internet access; no target credentials are needed.

## Requirements

1. Installed knockpy tool
2. Target domain resolvable via public DNS
3. Basic command-line access on Linux/macOS/Windows

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like dnsdumpster or internal scans
- Implement DNS monitoring with services like Cloudflare or Route 53 to alert on unresolved subdomains
- Use certificate transparency logs to track subdomain registrations

## Objectives

1. Discover all subdomains associated with the target
2. Identify anomalous subdomains pointing to external services
3. Flag potential takeover vectors for further investigation

## Instructions

### Step 1: Run Subdomain Enumeration

**Context**: Initiate the scan to brute-force and permute potential subdomains.

**Command** ([[commands/knockpy-enumerate-subdomains]]):
```bash
knockpy gratipay.com
```

> This command queries DNS for permutations of common subdomain names against 'gratipay.com'. Expected output includes a list of valid subdomains, such as 'www.gratipay.com.herokudns.com', along with any wildcards or NXDOMAIN responses.

### Step 2: Review Output for Vulnerabilities

**Context**: Analyze the results for subdomains with service-specific suffixes (e.g., herokudns.com) that may be unclaimed.

No specific command; manually inspect the knockpy output file or console log.

> Look for subdomains that resolve but serve error pages from the service provider.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/knockpy-enumerate-subdomains]]

## Tools Used

- [[tools/knockpy]]

## Tags

- [[subdomain-enumeration]]
- [[Reconnaissance]]
