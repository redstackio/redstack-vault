---
id: proc-uuid-1
tags:
  - dns-enumeration
  - subdomain-takeover
  - recon
type: procedure
tools:
  - '[[tools/Subfinder]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subfinder-enumerate-subdomains]]'
  - '[[commands/dig-lookup-subdomain]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:31.234Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify Dangling DNS Records for Subdomain Takeover

## Summary

This procedure enumerates subdomains of a target domain and identifies dangling DNS records that point to terminated or non-existent cloud resources, such as AWS EC2 instances, enabling potential subdomain takeover attacks.

## Description

In this attack scenario, attackers scan for subdomains using passive and active reconnaissance to find DNS records (e.g., CNAMEs) that resolve to unavailable resources. For the 8x8 case, the subdomain █.staging.█.8x8.com pointed to a terminated EC2 instance, leaving it vulnerable to takeover by claiming the associated AWS resource name (e.g., S3 bucket). Prerequisites include public DNS access and tools for enumeration; outcomes include identifying takeover candidates for impersonation or phishing.

## Requirements

1. Internet access for DNS queries and subdomain enumeration
2. Installation of Subfinder or similar tools
3. Basic knowledge of DNS records and AWS resource naming

## Defense

Defensive measures and detection strategies:

- Regularly audit and clean up DNS records upon resource termination
- Implement DNS monitoring for dangling records using tools like DNSdumpster or automated scripts
- Use AWS Config rules to alert on orphaned DNS entries

## Objectives

1. Discover subdomains with misconfigured DNS
2. Identify records pointing to terminated resources
3. Prepare for takeover validation

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Generate a list of potential subdomains to check for misconfigurations.

**Command** ([[commands/subfinder-enumerate-subdomains]]):
```bash
subfinder -d 8x8.com -o subdomains.txt
```

> This command uses Subfinder to passively enumerate subdomains from various sources. Expected output: A file subdomains.txt containing discovered subdomains like staging.8x8.com.

### Step 2: Resolve and Identify Dangling Records

**Context**: Query DNS for each subdomain to find those resolving to inactive resources.

**Command** ([[commands/dig-lookup-subdomain]]):
```bash
cat subdomains.txt | while read sub; do dig +short $sub; done > resolutions.txt
```

> This loops through subdomains and performs quick DNS lookups. Expected output: resolutions.txt with CNAMEs or IPs; flag entries where the target (e.g., EC2 alias) is known terminated via manual AWS checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/subfinder-enumerate-subdomains]]
- [[commands/dig-lookup-subdomain]]

## Tools Used

- [[tools/Subfinder]]

## Tags

- [[dns-enumeration]]
- [[subdomain-takeover]]
