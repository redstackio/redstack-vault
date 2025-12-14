---
id: proc-uuid-1
tags:
  - reconnaissance
  - dns
  - s3
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-discover-subdomain]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:39.721Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Dangling S3 Bucket Reference

## Summary

This procedure identifies subdomain takeovers by querying a potentially dangling DNS record pointing to a deleted AWS S3 bucket, triggering an error that discloses the bucket name for claiming.

## Description

In scenarios where a subdomain's CNAME or alias points to an S3 bucket that has been deleted without updating DNS, accessing the subdomain results in an AWS PermanentRedirect error. This error XML includes the original bucket name and endpoint, allowing attackers to recreate the bucket in the specified region (often us-east-1) and take control. This is common in cloud misconfigurations and enables serving malicious content, phishing, or certificate issuance under the trusted domain.

## Requirements

1. Network access to the target subdomain
2. Installed [[tools/curl]] for HTTP requests
3. Basic understanding of AWS S3 and DNS resolution

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling cloud resource references using tools like dnsdumpster or cloud-specific scanners
- Implement monitoring for S3 bucket creation events in target regions
- Use AWS Config rules to detect orphaned DNS entries

## Objectives

1. Reveal the dangling S3 bucket name from error response
2. Confirm the subdomain is vulnerable to takeover
3. Extract endpoint details for subsequent claiming

## Instructions

### Step 1: Query the Subdomain

**Context**: Send an HTTP GET request to the target subdomain to trigger the S3 error disclosure.

**Command** ([[commands/curl-discover-subdomain]]):
```bash
curl https://www█████████.affirm.com
```

> This command performs a simple GET request. On success, expect an XML response with <Code>PermanentRedirect</Code>, <Bucket>affirm-prod-www-cms█████████</Bucket>, and <Endpoint>s3.amazonaws.com</Endpoint>.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-discover-subdomain]]

## Tools Used

- [[tools/curl]]

## Tags

- reconnaissance
- s3
- dns
