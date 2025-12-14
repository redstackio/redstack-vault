---
id: proc-uuid-3
tags:
  - s3-verification
  - bucket-check
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-s3-check]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:51:10.834Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Verify-Non-Existent-S3-Buckets

## Summary

This procedure checks AWS S3 endpoints derived from DNS CNAMEs to confirm buckets have been deleted, creating opportunities for takeover.

## Description

Accessing S3 URLs directly tests for bucket existence; a NoSuchBucket error indicates deletion without DNS update. For Khan Academy, this confirms vulnerability on event subdomains. Target is AWS cloud; prerequisites are CNAME targets; outcomes validate squattable names.

## Requirements

1. Internet access to S3 endpoints
2. Identified S3 CNAMEs
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Sync DNS updates with infrastructure deletions
- Enable S3 access logging to detect probes
- Use AWS Config to monitor bucket lifecycles

## Objectives

1. Probe S3 endpoints for errors
2. Confirm bucket non-existence
3. Document vulnerable names

## Instructions

### Step 1: HTTP Probe S3 Endpoint

**Context**: Send a HEAD request to the bucket URL to check status.

**Command** ([[commands/curl-s3-check]]):
```bash
 curl -I https://healthyhackathon.khanacademy.org.s3.amazonaws.com
```

> Expects a 404-like NoSuchBucket XML error, confirming deletion. No content served indicates availability.

### Step 2: Repeat for Additional Buckets

**Context**: Test all candidate endpoints.

Apply to hackweek.khanacademy.org.s3.amazonaws.com for consistent errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability

### Sub-Techniques


## Commands Used

- [[commands/curl-s3-check]]

## Tools Used


## Tags

- [[s3-verification]]
- [[bucket-check]]
