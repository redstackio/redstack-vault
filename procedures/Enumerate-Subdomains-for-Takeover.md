---
id: proc-uuid-1
tags:
  - subdomain-enumeration
  - dns
  - recon
type: procedure
tools:
  - '[[tools/subfinder]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subfinder-enumerate]]'
  - '[[commands/dig-cname-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T05:32:23.786Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate-Subdomains-for-Takeover

## Summary

This procedure uses passive and active scanning to enumerate subdomains of a target domain, identifying those with DNS records pointing to cloud services vulnerable to takeover, such as unclaimed AWS S3 buckets.

## Description

In a subdomain takeover attack, attackers first discover subdomains via enumeration tools that query public sources and perform DNS brute-forcing. The focus is on detecting dangling CNAME records to external services like AWS S3. This step reveals potential entry points without direct interaction with the target, minimizing detection. Expected outcomes include a list of subdomains and their DNS resolutions, highlighting takeover candidates.

## Requirements

1. Network access to public DNS resolvers
2. Installation of subdomain enumeration tools like subfinder
3. Target domain name (e.g., bimedb.com)

## Defense

Defensive measures and detection strategies:

- Monitor DNS changes and subdomain registrations via tools like DNS logging in AWS Route 53
- Use services like SecurityTrails or DNSDumpster alerts for new subdomains
- Regularly audit CNAME records to ensure they point to owned resources

## Objectives

1. Discover all subdomains associated with the target
2. Identify DNS records pointing to cloud providers
3. Flag potential takeover vulnerabilities

## Instructions

### Step 1: Run Subdomain Enumeration

**Context**: Use subfinder to gather subdomains from passive sources like Certificate Transparency logs and search engines.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d bimedb.com -o subdomains.txt
```

> This command queries multiple data sources and outputs a list of subdomains to subdomains.txt. Expected output: a file with lines like "ws.bimedb.com".

### Step 2: Check DNS Records for CNAMEs

**Context**: For each subdomain, query DNS to find CNAME records that may point to claimable resources.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig ws.bimedb.com +short
```

> This performs a quick DNS lookup. Expected output: CNAME to an S3 endpoint like "ws-bimedb-com.s3.amazonaws.com" if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/subfinder-enumerate]]
- [[commands/dig-cname-lookup]]

## Tools Used

- [[tools/subfinder]]

## Tags

- [[subdomain-enumeration]]
- [[dns-recon]]
