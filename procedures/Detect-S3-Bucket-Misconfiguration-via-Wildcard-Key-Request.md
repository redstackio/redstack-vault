---
tags:
  - s3
  - misconfiguration
  - information-disclosure
  - aws
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-request-url]]'
platforms:
  - AWS
  - Cloud
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Vulnerability Scanning]]'
id: 199954e4-201e-4d7b-bf55-0f39badaa3b5
created_at: '2025-12-14T17:26:11.923Z'
updated_at: '2025-12-14T17:26:11.923Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Detect-S3-Bucket-Misconfiguration-via-Wildcard-Key-Request

## Summary

This procedure demonstrates how to identify a misconfigured AWS S3 bucket by requesting a wildcard key path, such as https://security.olx.com/*, which triggers a 'NoSuchKey' error. The error response discloses backend infrastructure details like AWS S3 usage, RequestId, and HostId, providing minor information about the target's cloud setup without accessing sensitive data.

## Description

In scenarios where a web endpoint or blog is backed by an S3 bucket, requesting non-existent keys (e.g., via wildcard paths) can reveal the underlying storage service through error messages. This is common in misconfigured static site hosts or CDNs pointing to S3. The technique is useful during reconnaissance to map cloud infrastructure. In this case, accessing https://security.olx.com/* exposed S3 details, confirming the service's existence but yielding no exploitable data. Prerequisites include internet access to the target URL; no authentication is needed for public endpoints.

## Requirements

1. Network access to the target URL (e.g., https://security.olx.com/*).
2. Basic HTTP client like curl or a web browser.
3. No special credentials, as this targets public-facing misconfigurations.

## Defense

Defensive measures and detection strategies:

- Configure S3 buckets with proper access controls and error handling to suppress detailed error messages (e.g., use custom error documents).
- Implement web application firewalls (WAF) to block anomalous requests like wildcard paths.
- Monitor S3 access logs for unusual key requests and enable AWS CloudTrail for auditing.
- Use least-privilege IAM policies to limit public exposure of buckets.

## Objectives

1. Confirm the presence of an S3-backed service behind a web endpoint.
2. Gather infrastructure details from error responses for further reconnaissance.
3. Assess potential misconfigurations without triggering alerts on sensitive operations.

## Instructions

### Step 1: Request the Target URL with Wildcard Path

**Context**: Initiate an HTTP request to the suspected S3-backed endpoint using a wildcard or non-existent key to provoke an error response that discloses backend details.

**Command** ([[commands/curl-request-url]]):
```bash
curl -v https://security.olx.com/*
```

> This command sends a verbose GET request to the URL with a wildcard path, expecting a 404-like 'NoSuchKey' error from S3. The verbose flag (-v) displays headers and response body, revealing details like x-amz-request-id and x-amz-id-2, which confirm AWS S3 usage.

### Step 2: Analyze the Error Response

**Context**: Parse the returned error for indicators of S3 misconfiguration, such as specific error codes and metadata.

**Command** ([[commands/curl-request-url]]):
```bash
curl https://security.olx.com/* | grep -i 'NoSuchKey\|RequestId\|HostId'
```

> This pipes the response through grep to filter for key S3 error elements. Successful output includes phrases like '<Code>NoSuchKey</Code>' and associated IDs, indicating public or misconfigured bucket exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

## Commands Used

- [[commands/curl-request-url]]

## Tools Used


## Tags

- [[s3]]
- [[misconfiguration]]
- [[information-disclosure]]
- [[aws]]
- [[Reconnaissance]]
