---
tags:
  - aws-s3
  - verification
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-s3-endpoint]]'
platforms:
  - AWS
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 36c642c0-6e42-42be-b9fd-24a46aa01ebd
created_at: '2025-12-14T05:32:31.142Z'
updated_at: '2025-12-14T05:32:31.142Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-Non-Existent-S3-Bucket

## Summary

This procedure checks if an AWS S3 bucket referenced by a DNS CNAME is active or deleted, confirming availability for takeover by attempting direct access to the bucket's website endpoint.

## Description

After identifying a dangling CNAME, attackers verify bucket existence by accessing the S3 website URL. A non-existent bucket returns errors like XML NoSuchBucket, indicating the resource is free to claim. This step is crucial in the eu-west-1 region for the specific endpoint gameday.websummit.net.s3-website-eu-west-1.amazonaws.com.

## Requirements

1. Public access to the S3 endpoint
2. HTTP client like curl
3. Awareness of region-specific S3 URLs

## Defense

Defensive measures and detection strategies:

- Monitor S3 bucket creation/deletion logs for unauthorized access
- Use AWS Config rules to alert on dangling DNS references
- Implement bucket naming policies to avoid common takeover names

## Objectives

1. Confirm bucket deletion or non-existence
2. Validate takeover feasibility
3. Document error responses for proof

## Instructions

### Step 1: Access S3 Website Endpoint

**Context**: Attempt to fetch the root of the S3 website to check for content or errors.

**Command** ([[commands/curl-access-s3-endpoint]]):
```bash
curl -I http://gameday.websummit.net.s3-website-eu-west-1.amazonaws.com
```

> Expect a 404 or NoSuchBucket XML error, confirming the bucket does not exist.

### Step 2: Check for Specific Error

**Context**: Parse the response for AWS-specific error indicators.

**Command** ([[commands/curl-access-s3-endpoint]]):
```bash
curl http://gameday.websummit.net.s3-website-eu-west-1.amazonaws.com
```

> Look for '<Error><Code>NoSuchBucket</Code>' in the output to verify availability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-s3-endpoint]]

## Tools Used


## Tags

- [[aws-s3]]
- [[verification]]
