---
tags:
  - aws-s3
  - verification
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-subdomain]]'
platforms:
  - AWS
techniques:
  - '[[Vulnerability Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 57ba7a0e-3265-42dc-8886-29dac95b51b8
created_at: '2025-12-14T04:51:10.530Z'
updated_at: '2025-12-14T04:51:10.530Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Verify S3 Bucket Absence

## Summary

This procedure confirms that an AWS S3 bucket referenced by a CNAME is non-existent or unconfigured, validating the subdomain as claimable for takeover.

## Description

Following CNAME identification, access the subdomain URL to trigger an S3 error response. In the Ubiquiti case, this revealed no bucket named 'uwn-images' in us-west-1, allowing any AWS user to create it and seize control, potentially for phishing under the trusted domain.

## Requirements

1. HTTP client like curl
2. Public access to the subdomain
3. Knowledge of the S3 region from CNAME

## Defense

Defensive measures and detection strategies:

- Create placeholder S3 buckets for all referenced endpoints
- Monitor S3 access logs for unauthorized creation attempts
- Use AWS Config rules to alert on dangling DNS pointers

## Objectives

1. Elicit S3 error indicating absence
2. Confirm no website configuration
3. Assess takeover feasibility

## Instructions

### Step 1: Access Subdomain URL

**Context**: Send an HTTP request to the subdomain to check S3 response.

**Command** ([[commands/curl-access-subdomain]]):
```bash
curl -I https://assets.goubiquiti.com
```

> Expected output: HTTP 403/404 with XML like <Error><Code>NoSuchBucket</Code>...</Error>, confirming the bucket does not exist.

### Step 2: Inspect Error Details

**Context**: Analyze the response for S3-specific indicators.

No command; review curl output manually.

> Look for 'NoSuchBucket' or 'AccessDenied' without configuration.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-subdomain]]

## Tools Used


## Tags

- [[aws-s3]]
- [[verification]]
