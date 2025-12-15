---
id: proc-s3-public-access-001
tags:
  - aws
  - s3
  - misconfiguration
  - data-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-list-s3-bucket]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:24:56.368Z'
skill_level: novice
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
---
# Access-and-Enumerate-Public-S3-Bucket-Contents

## Summary

This procedure exploits AWS S3 bucket misconfigurations by directly accessing the public endpoint to list and download contents, enabling unauthorized exposure of sensitive data such as system diagnostics from an Acronis Appliance.

## Description

In cloud environments like AWS, S3 buckets can be inadvertently set to public read access due to improper bucket policies or ACLs. Attackers discover these via bucket name guessing, web searches, or known endpoints. Accessing the bucket URL triggers an unauthenticated ListBucket API call, returning an XML manifest of objects. This can reveal confidential files, leading to data leaks that aid further attacks like reconnaissance or privilege escalation. The target here is the 'acronis.1' bucket, exposing a ZIP file with system information from 2018.

## Requirements

1. Internet access to the public S3 endpoint (no VPN or proxy needed)
2. HTTP client like curl or a web browser
3. Knowledge of the bucket name (e.g., via public sources or enumeration)

## Defense

Defensive measures and detection strategies:

- Enforce least-privilege bucket policies: Deny public read access using AWS IAM policies
- Enable S3 access logging and monitor for anomalous ListBucket requests from unknown IPs
- Use AWS Config rules to audit public buckets and alert on misconfigurations
- Implement bucket encryption and versioning to mitigate impact of leaks

## Objectives

1. Enumerate S3 bucket contents without authentication
2. Identify and exfiltrate sensitive files like system info archives
3. Assess potential for broader data compromise

## Instructions

### Step 1: List Bucket Contents

**Context**: Send an HTTP GET request to the S3 bucket root endpoint to invoke the ListBucket operation and retrieve the XML listing of objects.

**Command** ([[commands/curl-list-s3-bucket]]):
```bash
curl http://acronis.1.s3.amazonaws.com
```

> This command fetches the bucket's object list. Expected output is an XML <ListBucketResult> document showing keys like 'sysinfo_AcronisAppliance_2018-08-01_15-16-21.zip', with no authentication required if public.

### Step 2: Download Sensitive File

**Context**: Once contents are listed, target and retrieve specific sensitive objects via direct download to exfiltrate data.

**Command** ([[commands/curl-list-s3-bucket]] with output flag):
```bash
curl -O http://acronis.1.s3.amazonaws.com/sysinfo_AcronisAppliance_2018-08-01_15-16-21.zip
```

> Downloads the ZIP file locally. Success is indicated by a 200 OK response and the file saved without errors. Inspect the ZIP for system diagnostics, configs, or credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Cloud Storage]]

### Sub-Techniques


## Commands Used

- [[commands/curl-list-s3-bucket]]

## Tools Used


## Tags

- aws
- s3
- misconfiguration
- data-leak
