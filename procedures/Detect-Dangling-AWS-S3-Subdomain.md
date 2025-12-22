---
id: 123e4567-e89b-12d3-a456-426614174001
name: Detect Dangling AWS S3 Subdomain
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.533Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
tags:
  - subdomain-takeover
  - dns
  - aws-s3
commands:
  - '[[commands/dig-resolve-subdomain]]'
platforms:
  - Web
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
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

# Detect Dangling AWS S3 Subdomain

## Summary

This procedure identifies subdomains with DNS records pointing to AWS S3 hosting endpoints that lack a corresponding bucket, exposing them to takeover by revealing a 'NoSuchBucket' error.

## Description

In a subdomain takeover attack, attackers scan for dangling DNS records where a CNAME or alias points to cloud services like AWS S3 without the bucket being provisioned. For users.tweetdeck.com, the record pointed to s3-website-us-east-1.amazonaws.com, but no bucket existed, allowing anyone to claim it. This step focuses on DNS resolution and error confirmation to validate the vulnerability.

## Requirements

1. Access to DNS resolution tools like dig or nslookup
2. Internet connectivity to query public DNS
3. Basic knowledge of AWS S3 error responses

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records against cloud resource inventories
- Implement DNS monitoring for dangling records using tools like DNSDumpster
- Use AWS Config rules to alert on unclaimed S3 endpoints

## Objectives

1. Confirm DNS points to S3 without bucket
2. Validate error page exposure
3. Identify takeover feasibility

## Instructions

### Step 1: Resolve Subdomain DNS

**Context**: Query the DNS to check if it resolves to an AWS S3 endpoint.

**Command** ([[commands/dig-resolve-subdomain]]):
```bash
dig users.tweetdeck.com
```

> This command outputs the CNAME or A record; look for s3-website-*.amazonaws.com indicating S3 hosting.

### Step 2: Verify Missing Bucket

**Context**: Access the subdomain URL to trigger the AWS error page.

**Command** ([[commands/curl-http-head]]):
```bash
curl -I http://users.tweetdeck.com
```

> Expect a 404-like response with XML body containing <Code>NoSuchBucket</Code>, confirming the bucket is unclaimed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/dig-resolve-subdomain]]
- [[commands/curl-http-head]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
