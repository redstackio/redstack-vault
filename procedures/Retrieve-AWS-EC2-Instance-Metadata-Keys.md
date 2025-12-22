---
id: aaa1ed44-fb7f-4711-bba9-50d5e03793bc
name: Retrieve-AWS-EC2-Instance-Metadata-Keys
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.373872+00:00'
updated_at: '2023-04-10T20:19:58.599948+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/AWS Metadata]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Grabbing the keys in metadata version 2]]'
  - '[[tags/Remote code execution]]'
commands:
  - '[[commands/retrieve-aws-ec2-metadata-with-token]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# Retrieve-AWS-EC2-Instance-Metadata-Keys

## Summary

This procedure retrieves sensitive information from the AWS EC2 Instance Metadata Service (IMDS) version 2, including potential IAM access keys, secret keys, and other instance details. By obtaining a session token and querying the metadata endpoint, an attacker with initial access to an EC2 instance can exfiltrate credentials attached via IAM roles, enabling further lateral movement or resource compromise within the AWS environment.

## Description

The AWS Instance Metadata Service provides data about the running EC2 instance, such as its ID, type, network configuration, and IAM role credentials if assigned. IMDSv2 requires token authentication to prevent unauthorized access from within the instance, but if an attacker gains code execution on the instance (e.g., via RCE), they can still request a token and access this metadata. This technique is particularly dangerous in misconfigured environments where IAM roles grant excessive permissions, allowing credential theft for API calls to other AWS services like S3 or EC2. The procedure uses curl to interact with the metadata endpoint at 169.254.169.254, which is only accessible from within the instance itself.

## Requirements

1. Initial access to an EC2 instance (e.g., shell access via RCE or compromised application).
2. curl tool installed on the instance (standard on most Linux distributions).
3. The instance must be configured for IMDSv2 (token-required mode); IMDSv1 is insecure but this procedure targets v2.
4. The instance should have an attached IAM role with credentials for the metadata to include access keys.

## Defense

- Enforce IMDSv2 on all EC2 instances and disable IMDSv1 to require token authentication.
- Use least-privilege IAM roles and avoid long-lived access keys; prefer temporary credentials.
- Monitor CloudTrail for unusual API calls originating from instance metadata queries.
- Implement network controls to limit instance access and enable instance metadata options like hop limit to prevent SSRF access.

## Objectives

1. Obtain a session token from the IMDSv2 endpoint.
2. Retrieve instance metadata, including IAM credentials if available.
3. Use extracted keys for further AWS resource access or exfiltration.

## Instructions

### Step 1: Request IMDSv2 Session Token

**Context**: First, generate a one-time token valid for up to 6 hours (21600 seconds) by sending a PUT request to the token endpoint. This token is required for all subsequent metadata queries in IMDSv2, preventing unauthenticated access.

**Command** ([[commands/retrieve-aws-ec2-metadata-token]]):
```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
```

> This command sends a PUT request with the TTL header to obtain a token stored in the TOKEN variable. The token is a long string used for authentication. If successful, the output is the raw token value; errors may indicate IMDSv1-only configuration or network issues.

### Step 2: Retrieve Instance Metadata Using Token

**Context**: With the token, query the metadata service to fetch details about the instance. This includes basic info like instance ID and, crucially, IAM security credentials if a role is attached. The -v flag enables verbose output for debugging.

**Command** ([[commands/query-aws-ec2-metadata-with-token]]):
```bash
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v "http://169.254.169.254/latest/meta-data/"
```

> This command authenticates with the token and lists available metadata paths. Successful output includes a directory listing of metadata categories (e.g., ami-id, instance-id, iam/security-credentials/). To get specific IAM keys, follow up with a targeted query like http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name. Look for AccessKeyId, SecretAccessKey, and Token in the response for temporary credentials.
