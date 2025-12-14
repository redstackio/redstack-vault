---
tags:
  - dns
  - recon
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup-for-subdomain]]'
platforms:
  - Cloud
  - AWS
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2ead8fa6-e3c3-4c3e-91cb-8264d707517c
created_at: '2025-12-14T05:32:31.168Z'
updated_at: '2025-12-14T05:32:31.168Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# DNS Enumeration for Subdomain Takeover

## Summary

This procedure uses DNS lookup tools to enumerate subdomains and identify dangling CNAME records pointing to unclaimed cloud resources, such as AWS S3 buckets, enabling subdomain takeover attacks.

## Description

In a subdomain takeover attack, attackers scan for misconfigured DNS records where a CNAME points to a service (e.g., AWS S3) that is no longer in use but not properly cleaned up. By querying DNS with tools like dig, the attacker reveals these dangling records. If the target resource is unclaimed, it can be registered to hijack the subdomain. This procedure focuses on the reconnaissance phase, targeting AWS-hosted subdomains, and assumes public DNS access. Expected outcomes include identifying vulnerable records that lead to full subdomain control, with impacts like hosting phishing pages or bypassing security policies.

## Requirements

1. Internet access for public DNS queries
2. Installed DNS resolution tool like dig
3. Target subdomain name (e.g., www.example.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or subjack
- Implement DNS monitoring for changes and unclaimed resource alerts
- Use AWS Config rules to detect unclaimed S3 buckets

## Objectives

1. Discover misconfigured DNS records vulnerable to takeover
2. Verify if pointed resources (e.g., S3 buckets) are unclaimed
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the target subdomain to resolve its DNS records and check for CNAMEs pointing to cloud services.

**Command** ([[commands/dig-dns-lookup-for-subdomain]]):
```bash
dig www.███████
```

> This command performs a DNS query for the subdomain, outputting sections like ANSWER, AUTHORITY, and ADDITIONAL. Look for a CNAME record in the ANSWER section pointing to an S3 endpoint (e.g., bucket.s3.amazonaws.com). If the bucket is unclaimed, it will resolve but show no active content.

### Step 2: Analyze Output for Vulnerabilities

**Context**: Parse the dig output to confirm a dangling record.

No specific command; manually inspect for unclaimed indicators like expired or available service endpoints.

> Expected: CNAME to unclaimed resource; success if resolution succeeds but bucket access returns 404 or claimable status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup-for-subdomain]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[recon]]
- [[subdomain-takeover]]
