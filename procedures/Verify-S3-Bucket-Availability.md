---
id: proc-uuid-002
name: Verify-S3-Bucket-Availability
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.312Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - aws-s3
  - recon
platforms:
  - AWS
commands:
  - '[[commands/curl-bucket-check]]'
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Verify-S3-Bucket-Availability

## Summary

This procedure checks if an AWS S3 bucket referenced in a DNS record is registered, confirming if it's vulnerable to takeover by returning an unregistered error.

## Description

After identifying a potential S3 endpoint from DNS, attempt anonymous access to the bucket. If unregistered, AWS returns a NoSuchBucket error, indicating claimability. This targets public cloud misconfigurations; requires no auth, outcomes confirm availability for next steps.

## Requirements

1. Identified bucket name from DNS (e.g., shopify-assets)
2. HTTP client like curl
3. Public internet access

## Defense

Defensive measures and detection strategies:

- Proactively register all DNS-pointed cloud resources
- Use AWS Config to monitor bucket existence
- Scan for dangling records with tools like dnsdumpster

## Objectives

1. Validate bucket non-existence
2. Assess takeover feasibility
3. Prepare for claiming if available

## Instructions

### Step 1: Attempt Bucket Access

**Context**: Query the S3 endpoint to check registration status.

**Command** ([[commands/curl-bucket-check]]):
```bash
curl https://shopify-assets.s3.amazonaws.com
```

> Expects XML error like <Code>NoSuchBucket</Code> if unregistered.

### Step 2: Verify via Browser or Additional Probe

**Context**: Confirm error persists across methods.

Navigate to https://shopify-assets.s3.amazonaws.com in a browser; look for AWS error page.

**Expected Output**: Bucket not found message.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning: Scanning IP Blocks

### Sub-Techniques


## Commands Used

- [[commands/curl-bucket-check]]

## Tools Used


## Tags

- [[aws-s3]]
- [[recon]]
