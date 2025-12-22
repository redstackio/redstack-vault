---
tags:
  - aws-s3
  - verification
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:51:10.545Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b2e2a05b-c4b3-43bd-869c-40cbed49f53a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify Unclaimed S3 Bucket

## Summary

This procedure confirms an S3 bucket is unclaimed by attempting to access the associated subdomain URL, expecting an AWS error indicating non-existence.

## Description

After DNS recon, visit the HTTP endpoint of the subdomain to check for bucket status. An unclaimed bucket results in a "NoSuchBucket" error, confirming takeover potential. This targets S3 website hosting in US East 1, where deleted or uncreated buckets leave DNS dangling.

## Requirements

1. Web browser or HTTP client like curl
2. The target subdomain URL
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Regularly audit S3 buckets and delete associated DNS records
- Use AWS Config to monitor bucket creation/deletion
- Implement bucket policies to restrict public access

## Objectives

1. Confirm bucket non-existence
2. Capture error screenshot for proof
3. Proceed to takeover if verified

## Instructions

### Step 1: Access Subdomain URL

**Context**: Load the HTTP URL to trigger S3 error response.

No command; use browser to visit http://example-subdomain.target.com or curl:

```bash
curl -I http://example-subdomain.target.com
```

> Returns 404-like error with XML body stating bucket not found. Screenshot the page for evidence.

### Step 2: Interpret Error

**Context**: Validate the AWS-specific error message.

Manually check response for "<Code>NoSuchBucket</Code>".

> Indicates unclaimed status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[aws-s3]]
- [[verification]]
