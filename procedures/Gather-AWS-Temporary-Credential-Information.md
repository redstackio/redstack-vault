---
id: 929d1942-4196-4035-b124-fdb69d785f6f
name: Gather-AWS-Temporary-Credential-Information
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.959307+00:00'
updated_at: '2023-04-10T20:19:57.210492+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - aws
  - cloud
  - discovery
  - credentials
commands:
  - '[[commands/aws-sts-get-caller-identity]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Gather-AWS-Temporary-Credential-Information

## Summary

This procedure uses the AWS Security Token Service (STS) GetCallerIdentity API call via the AWS CLI to retrieve details about the current IAM entity and AWS account associated with the active credentials. It is particularly useful in cloud environments to identify if temporary credentials are in use, such as those attached to an EC2 instance role, allowing attackers to assess their access scope and plan further privilege escalation or resource discovery.

## Description

In AWS, temporary credentials are often provided to EC2 instances through attached IAM roles, accessible via the instance metadata service or assumed via STS. This procedure focuses on querying the STS service to obtain the caller's ARN, account ID, and user ID, which reveals whether the credentials are temporary (e.g., assumed role sessions) and their originating role or user. This information is critical for discovery in compromised AWS environments, enabling attackers to map permissions, identify resource limits, and pivot to other services. The technique aligns with cloud service discovery by enumerating credential metadata without requiring additional permissions beyond basic STS access.

## Requirements

1. AWS CLI installed and configured with valid credentials (access key, secret key, and optional session token) or executed on an EC2 instance with an attached IAM role providing STS access.
2. Network access to AWS STS endpoints (typically over HTTPS on port 443).
3. Basic IAM permissions for sts:GetCallerIdentity (often granted by default to most roles/users).

## Defense

- Implement least privilege by restricting sts:GetCallerIdentity calls to necessary roles and monitor via AWS CloudTrail for anomalous usage.
- Enable AWS Config rules to detect overly permissive IAM policies and rotate credentials regularly to limit exposure.
- Use AWS GuardDuty to alert on unusual STS API calls from compromised instances.

## Objectives

1. Retrieve the AWS account ID, IAM entity ARN, and user ID associated with current credentials.
2. Determine if credentials are temporary and identify the assuming role or user for privilege assessment.
3. Validate credential configuration to support further discovery or escalation in the AWS environment.

## Instructions

### Step 1: Retrieve Caller Identity Information

**Context**: This step executes the AWS STS GetCallerIdentity command to fetch metadata about the active credentials. It helps confirm the credential type (e.g., temporary session from an EC2 role) and provides the foundation for understanding access boundaries. Run this from a shell on the target instance or a machine with AWS CLI configured.

**Command** ([[commands/aws-sts-get-caller-identity]]):

```bash
aws sts get-caller-identity
```

> The command queries the STS service and returns JSON output including the Account ID, UserId (unique identifier), and Arn (Amazon Resource Name of the caller). For temporary credentials from an EC2 role, the Arn will resemble "arn:aws:sts::ACCOUNT_ID:assumed-role/ROLE_NAME/SESSION_NAME". If the output shows an assumed role, it indicates temporary credentials with a limited lifespan (typically 1-12 hours). Verify the JSON for session indicators to confirm success.
