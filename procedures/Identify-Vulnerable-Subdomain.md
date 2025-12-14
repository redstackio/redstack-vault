---
tags:
  - subdomain-takeover
  - reconnaissance
  - dns
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.366Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 522cbc40-0ca2-4086-a49a-3e8a26013cf8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Vulnerable-Subdomain

## Summary

This procedure involves reconnaissance to identify subdomains of a target that are configured in DNS but appear inactive or vulnerable to takeover, such as those with dangling records pointing to unused third-party services.

## Description

In a subdomain takeover attack, the first step is to enumerate and assess subdomains for misconfigurations. Attackers scan for subdomains like demo.greenhouse.io that resolve but lead to non-existent resources on external platforms. This procedure focuses on manual or tool-assisted identification, checking for signs like 404 errors or service-specific inactive states, setting the stage for DNS verification and exploitation.

## Requirements

1. Internet access for public DNS queries
2. Basic knowledge of domain enumeration techniques
3. Access to DNS resolution tools

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners
- Implement subdomain monitoring tools to alert on inactive configurations
- Remove unused subdomains promptly

## Objectives

1. Discover potential takeover targets
2. Flag inactive subdomains for further investigation
3. Build a list of vulnerable assets

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Start by listing all subdomains associated with the target domain to identify candidates.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d greenhouse.io -o subdomains.txt
```

> This command uses Subfinder to passively enumerate subdomains. Expected output: A file subdomains.txt with entries like demo.greenhouse.io. Manually review for inactive ones by attempting HTTP requests or noting configurations.

### Step 2: Initial Inactivity Check

**Context**: Probe identified subdomains for signs of vulnerability, such as no response or error pages.

**Command** ([[commands/httpx-probe]]):
```bash
cat subdomains.txt | httpx -silent -o inactive.txt
```

> Filter for subdomains that resolve but show errors (e.g., 404 or service-specific messages). Expected output: List of potentially vulnerable subdomains.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/subfinder-enumerate]]
- [[commands/httpx-probe]]

## Tools Used


## Tags

- [[subdomain-enumeration]]
- [[dns-recon]]
