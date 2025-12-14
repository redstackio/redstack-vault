---
tags:
  - reconnaissance
  - dns-enumeration
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/Subfinder]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subfinder-enumerate]]'
  - '[[commands/dig-lookup]]'
platforms:
  - DNS
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8b560950-9287-40a0-9a2e-7c0cb9d54199
created_at: '2025-12-14T04:38:39.340Z'
updated_at: '2025-12-14T04:38:39.340Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Enumerate Subdomains and Identify Dangling Records

## Summary

This procedure involves scanning a target domain like mozaws.net to enumerate subdomains and detect dangling DNS records, such as unused CNAMEs pointing to claimable external services, setting the stage for subdomain takeover.

## Description

In a subdomain takeover attack, the first step is reconnaissance to map the attack surface. Attackers enumerate subdomains using passive and active techniques, then inspect DNS records for misconfigurations like dangling CNAMEs to services (e.g., GitHub Pages, Heroku) that are no longer active. This procedure assumes public DNS access and focuses on identifying exploitable records without alerting the target. Expected outcome: A list of vulnerable subdomains ready for claiming.

## Requirements

1. Network access to public DNS resolvers
2. Installation of enumeration tools like Subfinder
3. Basic knowledge of DNS record types (CNAME, A, etc.)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated tools like DNS Dumpster or internal scripts
- Implement DNS monitoring with anomaly detection (e.g., via Cloudflare or Route 53 logs) to alert on unresolved or hijacked records
- Use subdomain management tools to expire unused services promptly

## Objectives

1. Discover all subdomains under the target domain
2. Identify DNS misconfigurations pointing to external, claimable services
3. Prepare for takeover by validating dangling status

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use passive DNS enumeration to generate a comprehensive list of subdomains without direct interaction with the target.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d mozaws.net -o subdomains.txt
```

> This command queries multiple passive sources to output a file with discovered subdomains. Expected output: A text file listing subdomains like vulnerable-sub.mozaws.net.

### Step 2: Inspect DNS Records for Dangling Entries

**Context**: For each subdomain, query DNS to find CNAME records pointing to potentially claimable services.

**Command** ([[commands/dig-lookup]]):
```bash
cat subdomains.txt | xargs -I {} dig {} CNAME +short
```

> This pipes subdomains into dig to fetch CNAME records. Look for outputs like "username.github.io" where the repo is deleted (verify manually). Expected output: List of CNAME targets; dangling if the service returns 404 or is unclaimed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/subfinder-enumerate]]
- [[commands/dig-lookup]]

## Tools Used

- [[tools/Subfinder]]

## Tags

- [[Reconnaissance]]
- [[dns-enumeration]]
- [[subdomain-takeover]]
