---
tags:
  - aws-metadata
  - credential-exfil
  - iam-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-aws-iam-roles]]'
  - '[[commands/curl-aws-iam-credentials]]'
verified: false
platforms:
  - AWS
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:24:15.391Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 4b07f8f1-35b7-486e-9f8b-cc040e468a4d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
---
# Exfiltrate-AWS-IAM-Credentials

## Summary

From the reverse shell, query the AWS instance metadata service to retrieve IAM role credentials, enabling potential further compromise of S3 buckets and other resources.

## Description

EC2 instances expose metadata at 169.254.169.254, including IAM roles. Curl commands fetch role names and temporary credentials (AccessKeyId, SecretAccessKey, Token). This exfiltrates secrets without additional auth, leading to data access on the isolated instance.

## Requirements

1. Active shell on EC2 instance
2. Instance attached to IAM role
3. Curl available (standard on Linux)

## Defense

Defensive measures and detection strategies:

- Use IMDSv2 (token-required metadata)
- Least privilege IAM roles
- Monitor metadata API calls via CloudTrail
- Block unnecessary metadata access from apps

## Objectives

1. List available IAM roles
2. Retrieve active credentials
3. Enable lateral movement

## Instructions

### Step 1: List IAM Roles

**Context**: Discover attached roles.

**Command** ([[commands/curl-aws-iam-roles]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

> Outputs role name, e.g., [redacted-role].

### Step 2: Fetch Credentials

**Context**: Exfiltrate specific role details.

**Command** ([[commands/curl-aws-iam-credentials]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/[redacted-role]
```

> Returns JSON with keys, secrets, token.

**Expected Output**: Full credential set for use in AWS CLI/API.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Cloud Instance Metadata API]]

### Sub-Techniques


## Commands Used

- [[commands/curl-aws-iam-roles]]
- [[commands/curl-aws-iam-credentials]]

## Tools Used


## Tags

- aws-metadata
- credential-exfil
- iam-theft
