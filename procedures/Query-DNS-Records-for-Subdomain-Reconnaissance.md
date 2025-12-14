---
id: proc-uuid-001
name: Query-DNS-Records-for-Subdomain-Reconnaissance
tags:
  - dns
  - reconnaissance
  - subdomain
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-query-dns]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:31.189Z'
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
# Query-DNS-Records-for-Subdomain-Reconnaissance

## Summary

This procedure involves querying DNS records for a target subdomain to reveal resolution details, such as A records and CNAMEs, identifying misconfigurations like pointers to transient cloud resources.

## Description

In AWS environments, subdomains may use CNAMEs pointing to EC2 public DNS names, which are not static. Querying these records exposes potential dangling configurations if the underlying instance is terminated without DNS updates. This reconnaissance step is crucial for detecting subdomain takeover opportunities, where an attacker can claim the subdomain by registering a matching service. The procedure targets public DNS resolvers and requires no authentication, making it a low-risk initial scan.

## Requirements

1. Access to a DNS resolver like 1.0.0.1 on port 53
2. Target subdomain name (e.g., max1.liveplan.com)
3. Basic networking tools like dig installed

## Defense

Defensive measures and detection strategies:

- Monitor DNS query logs for anomalous subdomain resolutions
- Implement DNSSEC to prevent spoofing
- Regularly audit CNAME records for transient references

## Objectives

1. Retrieve A and CNAME records for the subdomain
2. Identify if the CNAME points to a non-static resource like EC2 public DNS
3. Flag potential misconfigurations for further analysis

## Instructions

### Step 1: Query A Record

**Context**: Resolve the IP address associated with the subdomain to check current resolution.

**Command** ([[commands/dig-query-dns]]):
```bash
dig @1.0.0.1 max1.liveplan.com A +short
```

> This command uses Cloudflare's DNS resolver to fetch the A record, outputting the IP 54.68.121.128 if active.

### Step 2: Query CNAME Record

**Context**: Uncover alias records that may point to cloud-specific transient names.

**Command** ([[commands/dig-query-dns]]):
```bash
dig @1.0.0.1 max1.liveplan.com CNAME +short
```

> Expected output: ec2-54-68-121-128.us-west-2.compute.amazonaws.com, indicating a potential dangling CNAME.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dig-query-dns]]

## Tools Used


## Tags

- [[DNS]]
- [[Reconnaissance]]
