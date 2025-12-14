---
id: proc-uuid-5678
tags:
  - subdomain-takeover
  - aws-s3
  - dns-recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-subdomain]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:23.675Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Detect Dangling S3 Bucket Via DNS

## Summary

This procedure identifies subdomain takeover vulnerabilities by querying DNS records that point to non-existent AWS S3 buckets, revealing 404 errors with specific AWS messages indicating an expired or deleted resource.

## Description

In a subdomain takeover attack, a dangling DNS CNAME record points to an S3 bucket endpoint (e.g., s3-website-eu-west-1.amazonaws.com) that no longer exists. Accessing the subdomain triggers an AWS error page exposing the bucket name and confirming availability for hijacking. This is common in cloud misconfigurations where resources are deleted without updating DNS. The procedure uses HTTP requests to probe for these indicators, applicable to targets like websummit.net subdomains.

## Requirements

1. Internet access to resolve DNS and make HTTP requests
2. Target domain and suspected subdomain (e.g., s3.websummit.net)
3. Basic knowledge of AWS S3 error responses

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records against active cloud resources using tools like AWS Config or DNS scanners
- Implement monitoring for 404 errors on subdomains with automated alerts
- Use domain registrar locks and cloud policies to prevent unauthorized bucket creation

## Objectives

1. Confirm the presence of a dangling DNS record for S3
2. Extract bucket details from error messages for further exploitation
3. Validate vulnerability without alerting the target

## Instructions

### Step 1: Resolve and Access Subdomain

**Context**: Start by navigating to or curling the subdomain to trigger the S3 response, checking for the NoSuchBucket error.

**Command** ([[commands/curl-check-subdomain]]):
```bash
curl -v http://s3.websummit.net/
```

> This command sends a verbose HTTP request to the subdomain. Expected output includes a 404 status, XML body with <Code>NoSuchBucket</Code>, <Message>The specified bucket does not exist</Message>, and <BucketName>s3.websummit.net</BucketName>. The HostId and RequestId confirm it's an AWS S3 response.

### Step 2: Analyze DNS Resolution

**Context**: Verify the DNS CNAME points to an S3 endpoint, indicating potential takeover.

**Command** ([[commands/curl-check-subdomain]]):
```bash
nslookup s3.websummit.net
```

> Look for CNAME to dws-content.s3-website-eu-west-1.amazonaws.com or similar. If it resolves to AWS but the bucket is missing, the subdomain is vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Hardware

### Sub-Techniques


## Commands Used

- [[commands/curl-check-subdomain]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[aws-s3]]
- [[dns-recon]]
