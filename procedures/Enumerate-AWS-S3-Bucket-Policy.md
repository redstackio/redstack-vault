---
id: 849fc679-6a2c-4a17-8a50-528e3726eed4
name: Enumerate-AWS-S3-Bucket-Policy
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.020459+00:00'
updated_at: '2023-04-10T20:20:44.613573+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - cloud-aws
  - enumeration
  - s3-bucket-policy
commands:
  - '[[commands/aws-s3api-get-bucket-policy]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Enumerate-AWS-S3-Bucket-Policy

## Summary

This procedure uses the AWS CLI to retrieve and analyze the policy attached to a specific S3 bucket, helping identify misconfigurations such as public access permissions that could allow unauthorized data exfiltration. It is particularly useful in cloud reconnaissance to map permissions granted to AWS identities and uncover overly permissive policies.

## Description

In AWS environments, S3 bucket policies define access controls for buckets and their objects, specifying permissions for principals like IAM users, roles, or external accounts. Attackers enumerate these policies to discover misconfigurations, such as buckets allowing public read or write access, which can lead to sensitive data exposure. This procedure focuses on authenticated retrieval of the policy document via the AWS CLI, parsing the JSON output to evaluate statements for risks like wildcard principals (e.g., "*" allowing public access) or excessive permissions (e.g., s3:GetObject on all objects). It assumes the attacker has valid AWS credentials with s3:GetBucketPolicy permission and is targeted at production or development S3 buckets in an AWS account. Successful enumeration provides insights into the bucket's access model, enabling further attacks like data exfiltration if vulnerabilities are found.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables or ~/.aws/credentials file) with at least s3:GetBucketPolicy permission on the target bucket.
2. AWS CLI installed and accessible in the PATH (version 2.x recommended for full S3 API support).
3. Network access to AWS endpoints (no VPC endpoints required for public S3, but ensure no restrictive security groups block outbound HTTPS to s3.amazonaws.com).
4. Knowledge of the target S3 bucket name, obtained via prior reconnaissance (e.g., DNS enumeration or AWS account discovery).

## Defense

- Implement least-privilege access by regularly auditing S3 bucket policies with AWS IAM Access Analyzer to detect public or cross-account exposures.
- Enable S3 Block Public Access at the account and bucket levels to prevent accidental public configurations.
- Use AWS CloudTrail to log s3:GetBucketPolicy API calls and set up CloudWatch alarms for anomalous policy retrievals from unexpected IPs or principals.
- Enforce MFA and short-lived credentials for IAM users interacting with S3 management APIs.

## Objectives

1. Retrieve the JSON policy document for a specified S3 bucket to inspect permissions and principals.
2. Identify misconfigurations like public access or overly broad permissions that could enable data exfiltration.
3. Gather intelligence on AWS identity access patterns to support lateral movement or privilege escalation in the cloud environment.

## Instructions

### Step 1: Retrieve the S3 Bucket Policy

**Context**: Begin by using the AWS CLI to fetch the policy document for the target bucket. This step requires authenticated access and will return the policy as JSON if it exists, or an empty response if no policy is attached (indicating default bucket-level ACLs or no explicit policy). Review the output for risky statements, such as those allowing "Principal": "*" with actions like s3:GetObject.

**Command** ([[commands/aws-s3api-get-bucket-policy]]):
```bash
aws s3api get-bucket-policy --bucket $_BUCKET_NAME
```

> This command queries the S3 API for the bucket's policy. Replace $_BUCKET_NAME with the actual bucket name (e.g., my-sensitive-bucket). If successful, it outputs a JSON object with a "Policy" key containing the policy document. Parse this JSON manually or with jq (e.g., pipe to `jq '.Policy.Statement[] | select(.Principal == "*")'` to find public grants). If the bucket has no policy, expect {"Policy": ""}, signaling potential reliance on object ACLs—follow up by enumerating ACLs separately. Verify your credentials are scoped correctly; errors like AccessDenied indicate insufficient permissions.

### Step 2: Analyze the Policy for Misconfigurations

**Context**: Once retrieved, examine the policy structure to identify vulnerabilities. Look for allow statements with broad effects, such as Resource: "*" or Condition blocks that bypass IP restrictions. This manual analysis step helps prioritize buckets for further testing, like attempting anonymous downloads.

**Command** ([[commands/aws-s3api-get-bucket-policy]] piped with jq for analysis):
```bash
aws s3api get-bucket-policy --bucket $_BUCKET_NAME | jq '.Policy.Statement[] | {Effect, Principal, Action}'
```

> Assuming jq is installed, this enhances the output to filter and display key policy elements. Expected results include a list of statements showing Effect (Allow/Deny), Principal (users/roles/*), and Action (e.g., s3:*). Success is indicated by parsed JSON revealing permissive rules; if no jq, use a text editor or Python json module. Document findings, such as public read access, to inform exfiltration procedures.
