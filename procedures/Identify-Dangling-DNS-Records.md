---
id: proc-identify-dangling-dns
tags:
  - dns-enumeration
  - subdomain-takeover
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-lookup-dns]]'
verified: false
platforms:
  - Cloud
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:39.358Z'
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
# Identify Dangling DNS Records

## Summary

This procedure involves enumerating DNS records for a target domain to identify dangling CNAME records that point to non-existent or deleted cloud resources, a common precursor to subdomain takeover attacks. It is primarily used in reconnaissance phases to uncover misconfigurations in cloud-integrated domains like mozaws.net.

## Description

In the context of subdomain takeover, attackers scan for subdomains using tools or manual queries to find CNAME records linking to cloud services (e.g., AWS S3, Azure blobs). If the cloud resource was deleted without removing the DNS entry, the record 'dangles,' allowing anyone to claim it. This procedure focuses on detection via DNS lookups, assuming public access to the target's DNS zone. Prerequisites include basic networking knowledge and access to DNS query tools. Expected outcomes: a list of vulnerable subdomains ready for exploitation.

## Requirements

1. Network access to public DNS resolvers
2. Target domain with exposed subdomains (e.g., mozaws.net)
3. DNS query tool like dig installed

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like DNS linter scripts
- Implement DNS monitoring for unused records and automate cleanup on resource deletion
- Use certificate transparency logs to detect unauthorized subdomain usage

## Objectives

1. Discover subdomains and their record types
2. Identify CNAMEs pointing to unreachable resources
3. Flag potential takeover vectors for further exploitation

## Instructions

### Step 1: Enumerate Subdomains

**Context**: First, obtain a list of subdomains for the target domain using brute-forcing or passive sources, then query each for records.

**Command** ([[commands/dig-lookup-dns]]):
```bash
dig example-sub.mozaws.net ANY
```

> This command queries all record types for the subdomain. Look for CNAME responses. Expected output includes the CNAME target; if it doesn't resolve (e.g., NXDOMAIN on follow-up query), it's dangling.

### Step 2: Verify Dangling Status

**Context**: Confirm the CNAME target is non-existent by querying it directly.

**Command** ([[commands/dig-lookup-dns]]):
```bash
dig dangling-bucket.s3.amazonaws.com
```

> If no response or error, the resource is available for claiming. Repeat for multiple subdomains to build a vulnerability list.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/dig-lookup-dns]]

## Tools Used


## Tags

- [[dns-enumeration]]
- [[subdomain-takeover]]
