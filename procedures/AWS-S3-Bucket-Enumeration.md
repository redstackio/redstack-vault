---
id: 7699ff61-defa-4ab2-bbd3-9e106ae079ae
name: AWS-S3-Bucket-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.978948+00:00'
updated_at: '2023-10-10T20:20:50.928372+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - cloud-aws
  - enumeration
  - s3-buckets
commands:
  - '[[commands/aws-s3-list-buckets]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-S3-Bucket-Enumeration

## Summary

AWS S3 Bucket Enumeration is a reconnaissance technique used to discover all Simple Storage Service (S3) buckets associated with an AWS account. This procedure leverages the AWS CLI to list bucket names, creation dates, and regions, enabling attackers to identify potential targets for further exploration, such as checking for public accessibility or sensitive data exposure.

## Description

In cloud environments, attackers often begin by mapping the storage infrastructure to locate misconfigured or publicly accessible resources. S3 buckets are a common vector for data exposure if not properly secured. This procedure uses the AWS Security Token Service (STS) and S3 APIs via the AWS CLI to query the account's bucket inventory. It requires authenticated access and the 's3:ListAllMyBuckets' permission. Upon success, the output provides a JSON array of buckets, which can be parsed to prioritize enumeration of high-value targets like production data stores. This technique is particularly effective in compromised AWS environments where initial credentials have been obtained through other means, such as phishing or IAM role assumption.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with 's3:ListAllMyBuckets' permission attached to the IAM user or role.
2. AWS CLI installed and configured on the attacker's system.
3. Network access to AWS endpoints (no VPC restrictions blocking outbound API calls).
4. Basic familiarity with JSON output parsing for manual review or scripting further actions.

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict 's3:ListAllMyBuckets' to only necessary roles.
- Enable AWS CloudTrail logging for S3 API calls and monitor for anomalous list-bucket requests from unusual IPs or user agents.
- Use AWS Config rules to alert on public S3 buckets and enforce bucket policies denying unauthorized listings.
- Integrate with SIEM tools to detect spikes in S3 enumeration activity correlating with credential compromise indicators.

## Objectives

1. Retrieve a complete list of all S3 buckets in the target AWS account.
2. Gather metadata such as bucket creation dates and regions to assess age and distribution.
3. Identify potential sensitive buckets for subsequent access testing or data discovery.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with the target account's credentials to avoid authentication errors during enumeration. This step confirms the session is active and permissions are sufficient.

**Command** ([[commands/aws-s3-list-buckets]]):

First, configure credentials if not already done:

```bash
aws configure set aws_access_key_id $_ACCESS_KEY_ID
aws configure set aws_secret_access_key $_SECRET_ACCESS_KEY
aws configure set default.region $_REGION
```

> This sets the necessary authentication details. Expected output: No errors; configuration file updated in ~/.aws/credentials.

### Step 2: Execute Bucket Listing

**Context**: Issue the API call to retrieve the full inventory of S3 buckets. This is the core action that queries the S3 service endpoint for account-owned buckets.

**Command** ([[commands/aws-s3-list-buckets]]):
```bash
aws s3api list-buckets --query 'Buckets[].{Name:Name,CreationDate:CreationDate,Region:Owner}' --output json
```

> The --query flag filters the JSON response to focus on bucket names and creation dates; adjust for region if multi-region. Expected output: A JSON array listing buckets, e.g., {"Buckets": [{"Name": "my-bucket", "CreationDate": "2023-01-01T00:00:00.000Z"}]}.

### Step 3: Parse and Review Output

**Context**: Analyze the results to identify actionable buckets, such as those with names suggesting sensitive content (e.g., 'prod-data' or 'backups'). This step includes manual verification or piping to tools for further processing.

**Command** ([[commands/aws-s3-list-buckets]]):

Pipe the output to jq for formatted viewing:

```bash
aws s3api list-buckets --output json | jq '.Buckets[] | {Name: .Name, CreationDate: .CreationDate}'
```

> If jq is available, this prettifies the output. Expected output: Clean list of bucket details. If no buckets exist, returns an empty array. Decision point: If permissions denied, escalate privileges or switch credentials; otherwise, proceed to test individual buckets for access.
