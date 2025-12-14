---
tags:
  - subdomain-takeover
  - dns
  - reconnaissance
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup-for-cname]]'
verified: false
platforms:
  - Cloud
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:31.384Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 102609ee-e896-413d-b2f7-f532c8a9e88b
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Detect-Dangling-CNAME-with-DNS-Lookup

## Summary

This procedure uses DNS queries to identify dangling CNAME records pointing to unclaimed AWS CloudFront distributions, enabling subdomain takeover reconnaissance.

## Description

In scenarios where organizations fail to remove DNS entries after decommissioning CloudFront distributions, attackers can detect these via standard DNS lookups. The procedure queries the subdomain's A record, which resolves to a CNAME for a CloudFront distribution ID. If unclaimed, it returns global A records without an active origin, allowing takeover. This is common in cloud environments where services like CloudFront do not enforce CNAME validation against origins.

## Requirements

1. Access to a system with DNS resolution capabilities (e.g., Linux terminal)
2. Installation of the dig tool
3. Target subdomain suspected of misconfiguration

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or automated scripts
- Implement DNS monitoring for unexpected resolutions to cloud services
- Use AWS Config rules to alert on orphaned CloudFront distributions

## Objectives

1. Identify vulnerable subdomains with dangling CNAMEs
2. Confirm unclaimed status of CloudFront distributions
3. Gather evidence for potential takeover

## Instructions

### Step 1: Query DNS for Target Subdomain

**Context**: Perform a basic DNS lookup to resolve the subdomain and check for CNAME to CloudFront.

**Command** ([[commands/dig-dns-lookup-for-cname]]):
```bash
dig cloudfront.ubnt.com
```

> This command queries the authoritative DNS servers for the A record of cloudfront.ubnt.com. Expected output includes a CNAME section pointing to du6drkqe7qw4g.cloudfront.net and multiple A records (e.g., 52.222.171.58, 52.222.176.20), with no NS or origin details indicating it's unclaimed.

### Step 2: Validate Unclaimed Status

**Context**: Cross-check the distribution ID in AWS (manually or via API) to confirm no active origin.

**Command** ([[commands/dig-dns-lookup-for-cname]] with additional flags):
```bash
dig +short cloudfront.ubnt.com
```

> Short output shows only A records, confirming resolution without custom origin. Success if it matches known CloudFront IP ranges but lacks specific endpoint validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Identify Business Systems

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup-for-cname]]

## Tools Used

- [[tools/dig]]

## Tags

- subdomain-takeover
- dns
- reconnaissance
