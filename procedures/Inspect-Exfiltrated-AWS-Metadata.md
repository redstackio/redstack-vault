---
tags:
  - metadata-inspection
  - aws-exfil
  - recon
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-post-xapi-to-metadata]]'
  - '[[commands/curl-get-xapi-from-metadata]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T04:39:10.038Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: aaf8a513-bf68-47d1-bbac-dc27d6750165
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Inspect-Exfiltrated-AWS-Metadata

## Summary

This procedure analyzes the downloaded log to extract and interpret the AWS instance metadata obtained through the SSRF attack, revealing sensitive details for further exploitation.

## Description

The log captures the server's HTTP requests to 169.254.169.254, including responses listing metadata paths like ami-id, instance-id, security-groups, and potentially IAM credentials. Inspection confirms SSRF success and provides reconnaissance data, such as instance details, enabling attacks like key theft or lateral movement. This targets misconfigured AWS apps without IMDSv2 enforcement.

## Requirements

1. Downloaded 'log' file from test results
2. Text editor or viewer (e.g., Notepad++, VS Code)
3. Basic understanding of HTTP and AWS metadata format

## Defense

Defensive measures and detection strategies:

- Enable IMDSv2 on EC2 instances to require session tokens
- Rotate IAM roles and monitor metadata access logs via CloudTrail
- Scan logs for anomalous internal requests post-SSRF mitigations

## Objectives

1. Confirm SSRF exploitation via metadata response
2. Extract instance details for reconnaissance
3. Identify paths to credentials or internal hosts

## Instructions

### Step 1: Open and Review Log File

**Context**: Examine the contents for SSRF evidence.

Open the 'log' file in a text editor to locate the HTTP exchange with 169.254.169.254.

**Expected Output**: Entries showing POST/GET requests and 200 OK response with text/plain content listing paths (e.g., ami-id, instance-id; ~326 bytes).

### Step 2: Validate Metadata Paths

**Context**: Cross-reference with known AWS metadata to assess impact.

Look for responses like:

HTTP/1.0 200 OK
Content-Type: text/plain

ami-id
hostname
instance-id
...

To simulate and verify expected output, run [[commands/curl-get-xapi-from-metadata]]:

```bash
curl -X GET "http://169.254.169.254/latest/meta-data?/statements?statementId=3b9e4565-07ac-475f-be1f-d5f590f40779" \
  -H "X-Experience-API-Version: 1.0.3" \
  -H "Authorization: Basic dGVzdDp0ZXN0" \
  -H "Host: 169.254.169.254" \
  --connect-timeout 5
```

> Expect the same metadata listing; failure indicates non-AWS or blocked access.

**Expected Output**: Directory of available metadata endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xapi-to-metadata]]
- [[commands/curl-get-xapi-from-metadata]]

## Tools Used


## Tags

- metadata-inspection
- aws-exfil
- recon
