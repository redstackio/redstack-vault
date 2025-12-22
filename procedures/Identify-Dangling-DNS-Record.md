---
id: proc-uuid-1
tags:
  - dns-enumeration
  - reconnaissance
  - dangling-record
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.886Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Dangling DNS Record

## Summary

This procedure involves enumerating DNS records for target subdomains to identify dangling entries pointing to unmanaged external services, such as expired cloud resources, enabling potential subdomain takeover.

## Description

In a subdomain takeover attack, attackers scan for DNS records (e.g., CNAMEs) that point to third-party services no longer controlled by the domain owner. For mozaws.net, reconnaissance reveals a subdomain with a dangling record. This step uses passive and active DNS queries to spot these without direct interaction. Prerequisites include public DNS access and knowledge of common takeover-prone services like Heroku, AWS S3, or GitHub Pages.

## Requirements

1. Network access to public DNS resolvers (port 53 UDP/TCP)
2. Basic DNS knowledge and tools like dig
3. List of target subdomains (e.g., from brute-forcing or certificate transparency logs)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using automated tools like dnsrecon
- Implement DNS monitoring for unexpected changes or unresolved records
- Use subdomain management tools to track and cleanup unused records

## Objectives

1. Discover vulnerable DNS configurations
2. Identify takeover-eligible services
3. Gather evidence for exploitation feasibility

## Instructions

### Step 1: Enumerate Target Subdomains

**Context**: Start by listing potential subdomains under the target domain to focus enumeration.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d mozaws.net -o subdomains.txt
```

> This command uses passive sources to find subdomains. Expected output: A file with subdomain list like example-sub.mozaws.net.

### Step 2: Query DNS Records for Dangling Entries

**Context**: For each subdomain, query DNS to check for records pointing to external services.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig example-sub.mozaws.net +short
```

> This performs a DNS lookup. Look for CNAMEs to services like herokudns.com. If the resolved service returns a 404 or registration prompt when accessed via browser, it's dangling. Expected output: CNAME example-sub.herokuapp.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-lookup]]
- [[commands/subfinder-enumerate]]

## Tools Used

- None specific

## Tags

- [[DNS]]
- [[Reconnaissance]]
