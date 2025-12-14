---
id: proc-uuid-003
name: Access-AWS-Resources-with-Stolen-Credentials
tags:
  - initial-access
  - aws
  - cloud-exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:29.058Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-AWS-Resources-with-Stolen-Credentials

## Summary

This procedure uses extracted AWS credentials to authenticate and interact with AWS services, demonstrating potential for data breaches, service disruptions, and financial impact.

## Description

With the Access Key and Secret Key, attackers configure AWS tools like the CLI to impersonate the legitimate user, accessing S3 for data exfiltration, EC2 for instance control, or Lambda for code execution. The environment is AWS cloud infrastructure, with outcomes including resource manipulation. Prerequisites: Valid leaked credentials and AWS CLI installed.

## Requirements

1. Extracted AWS Access Key and Secret Key
2. AWS CLI installed and configured
3. Internet access to AWS endpoints

## Defense

Defensive measures and detection strategies:

- Enable AWS IAM monitoring for unusual access patterns
- Use multi-factor authentication (MFA) and least-privilege policies
- Rotate credentials immediately upon leak detection and monitor CloudTrail logs

## Objectives

1. Authenticate to AWS using stolen keys
2. Access and manipulate resources (e.g., list S3 buckets)
3. Achieve persistence or exfiltration

## Instructions

### Step 1: Configure AWS CLI with Stolen Credentials

**Context**: Set up authentication using the leaked keys to enable API calls.

Export environment variables:

```bash
export AWS_ACCESS_KEY_ID=AKIAEXAMPLEKEY
export AWS_SECRET_ACCESS_KEY=exampleSecretKey
export AWS_DEFAULT_REGION=us-east-1
```

> Prepares CLI for use. Expected output: No errors on export.

### Step 2: Test Access to AWS Resources

**Context**: Verify access by querying services like S3 or EC2.

Run AWS CLI command to list S3 buckets:

```bash
aws s3 ls
```

> Confirms permissions. Expected output: List of accessible buckets.

### Step 3: Escalate Impact

**Context**: Perform actions like downloading from S3 or launching EC2 instances.

Example: Download a bucket object:

```bash
aws s3 cp s3://bucket-name/object.txt .
```

> Enables data breach. Expected output: File downloaded successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used

- [[commands/aws-s3-ls]]
- [[commands/aws-s3-cp]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[initial-access]]
- [[aws]]
- [[cloud-exploitation]]
