---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - reconnaissance
  - dns
  - subdomain-enumeration
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-lookup]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:51:10.873Z'
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
# Enumerate Subdomains and DNS Records

## Summary

This procedure involves scanning for subdomains of a target domain and querying their DNS records to identify dangling CNAMEs pointing to cloud services like AWS S3, which can lead to subdomain takeover opportunities.

## Description

In scenarios like the TikTok musical.ly vulnerability, attackers enumerate subdomains to find unused ones with DNS records still pointing to decommissioned cloud resources. This misconfiguration allows claiming the resource and hijacking the subdomain for phishing or redirects. The procedure targets public DNS and requires no authentication initially, focusing on passive and active reconnaissance to map the attack surface.

## Requirements

1. Access to DNS resolution tools like dig or nslookup
2. Target domain name (e.g., example.com)
3. Optional: Subdomain enumeration tool like subfinder for broader discovery

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or internal scripts
- Implement DNS monitoring for changes and alert on unresolved cloud pointers
- Use domain registrar locks and cloud resource cleanup policies to prevent unclaimed buckets

## Objectives

1. Discover subdomains potentially vulnerable to takeover
2. Identify CNAME records pointing to unclaimed S3 buckets
3. Gather evidence for exploitation without alerting defenders

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use passive sources or brute-force to list potential subdomains, focusing on legacy ones like 'musical.ly'.

**Command** ([[commands/subfinder-enumerate]]):
```bash
subfinder -d example.com -o subdomains.txt
```

> This command queries passive sources to output a list of subdomains to subdomains.txt. Expected output: A file with lines like 'musical.ly.example.com'.

### Step 2: Query DNS for CNAME Records

**Context**: For each subdomain, check if it has a CNAME pointing to an S3 endpoint, indicating a potential dangling record.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig +short CNAME musical.ly.example.com
```

> This performs a DNS lookup for the CNAME record. Expected output: Something like 'legacy-bucket.s3.amazonaws.com' if dangling; empty or error if resolved elsewhere.

### Step 3: Batch Check Multiple Subdomains

**Context**: Automate queries for efficiency using a script or loop over the subdomain list.

**Command** ([[commands/dig-cname-lookup]]):
```bash
while read sub; do echo "$sub:"; dig +short CNAME $sub; done < subdomains.txt
```

> This loops through subdomains.txt, querying each. Expected output: List of subdomains with their CNAME targets, highlighting S3 pointers.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-cname-lookup]]
- [[commands/subfinder-enumerate]]

## Tools Used

- [[tools/dig]]
- [[tools/subfinder]]

## Tags

- [[Reconnaissance]]
- [[DNS]]
- [[subdomain-takeover]]
