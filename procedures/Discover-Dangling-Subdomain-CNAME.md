---
tags:
  - subdomain-takeover
  - dns-recon
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-check-cname]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 32f44b11-f596-4981-bbbe-b2ad3300404d
created_at: '2025-12-14T04:51:26.422Z'
updated_at: '2025-12-14T04:51:26.422Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Dangling-Subdomain-CNAME

## Summary

This procedure identifies subdomains with dangling CNAME records pointing to unclaimed cloud resources, such as AWS S3 buckets, enabling potential subdomain takeover attacks.

## Description

In this scenario, attackers scan for misconfigured DNS records on target domains like gnipcentral.com. A dangling CNAME occurs when a subdomain points to a decommissioned service's cloud resource without proper cleanup, leaving it claimable. The procedure involves DNS queries to detect such records, verifying if the pointed resource is unclaimed by checking for 404 responses or non-resolution. Prerequisites include access to DNS resolution tools and knowledge of common cloud endpoints.

## Requirements

1. Network access for DNS queries (UDP/TCP port 53)
2. Target domain or subdomain list
3. Basic understanding of DNS records and cloud services like AWS S3

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like DNS linter
- Implement domain monitoring services to alert on unclaimed subdomains
- Use CAA records to restrict certificate issuance for subdomains

## Objectives

1. Discover misconfigured subdomains vulnerable to takeover
2. Verify the dangling nature of the CNAME
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Query DNS for CNAME Record

**Context**: Perform a DNS lookup on the target subdomain to retrieve its CNAME record and identify if it points to a cloud service.

**Command** ([[commands/dig-check-cname]]):
```bash
dig blog.gnipcentral.com
```

> This command queries the DNS server for the subdomain's records. Look for a CNAME entry pointing to an S3-like endpoint (e.g., bucketname.s3-region.amazonaws.com). If present and the HTTP response is empty or 404, it's likely dangling.

### Step 2: Verify Unclaimed Resource

**Context**: Test HTTP access to the CNAME target to confirm it's unclaimed.

**Command** ([[commands/curl-access-url]]):
```bash
curl -I http://blog.gnipcentral.com/
```

> Expect a 404 or no content response, indicating the resource is available for claiming.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-check-cname]]
- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
