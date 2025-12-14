---
id: proc-uuid-discover-subdomains
tags:
  - reconnaissance
  - subdomain-enum
  - dns
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nslookup-cname-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:23.848Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-and-Enumerate-Subdomains-for-Misconfigurations

## Summary

This procedure involves reconnaissance to discover subdomains during bug hunting and identify those pointing to cloud services like AWS S3, uncovering potential misconfigurations for takeover.

## Description

In the context of ethical hacking or bug bounty programs, attackers often stumble upon loosely related hosts while targeting a primary domain. By enumerating subdomains via DNS queries, one can reveal CNAME records pointing to unused cloud resources, such as AWS S3 buckets. This sets the stage for subdomain takeover attacks, where control over the subdomain can lead to phishing or spoofing. Prerequisites include public DNS access and basic networking knowledge; no special privileges are needed.

## Requirements

1. Internet access for DNS resolution.
2. Basic tools like nslookup or dig for querying.
3. Knowledge of target domain and related scopes.

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs to cloud services.
- Monitor for unexpected bucket creations in AWS via CloudTrail logs.
- Implement DNSSEC and automated subdomain cleanup.

## Objectives

1. Uncover hidden subdomains linked to cloud infrastructure.
2. Flag potential misconfigurations for further exploitation.
3. Expand attack surface during reconnaissance.

## Instructions

### Step 1: Perform DNS Enumeration

**Context**: Start by querying known or suspected subdomains to find those related to the target.

**Command** ([[commands/nslookup-cname-query]]):
```bash
nslookup -type=CNAME suspected-subdomain.target.com
```

> This command resolves the CNAME record, revealing if the subdomain points to an AWS S3 endpoint like `bucket.s3.amazonaws.com`. Expected output includes the target bucket name if misconfigured.

### Step 2: Validate Subdomain Relevance

**Context**: Cross-check if the subdomain is in scope or loosely related to the primary target.

**Command** ([[commands/nslookup-cname-query]]):
```bash
nslookup target.com
```

> Use this to map the ecosystem. Expected output: List of authoritative nameservers and potential subdomain hints.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/nslookup-cname-query]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomain-enum]]
