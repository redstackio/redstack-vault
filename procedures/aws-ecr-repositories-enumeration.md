---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/ECR Enumeration]]'
  - '[[tags/Cloud Discovery]]'
commands:
  - '[[commands/aws-ecr-describe-repositories]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
skill_level: beginner
impact_level: low
detection_risk: medium
verified: true
validated: true
---

# AWS ECR Repositories Enumeration

## Summary

This procedure uses the AWS CLI to enumerate repositories in Amazon Elastic Container Registry (ECR), revealing details such as repository names, ARNs, creation dates, and image counts. It aids attackers in discovering potential targets for further exploitation, like accessing sensitive container images, while defenders can use it to inventory and monitor ECR resources for unauthorized access.

## Description

Amazon Elastic Container Registry (ECR) is a fully managed Docker container registry that integrates with AWS services for storing, managing, and deploying container images. Enumerating ECR repositories allows identification of all repositories in an AWS account, providing insights into the target's containerized applications, potential secrets in images, or misconfigurations. This technique maps to MITRE ATT&CK's Cloud Service Discovery, as it involves querying cloud infrastructure to map resources. In an offensive scenario, an attacker with compromised AWS credentials can run this to scout for valuable repositories. Defensively, regular enumeration helps detect anomalies like unexpected new repositories. The procedure assumes access to AWS CLI v2 and appropriate IAM permissions (e.g., ecr:DescribeRepositories).

## Requirements

1. AWS CLI installed and configured with valid credentials (via `aws configure` or environment variables).
2. IAM permissions: At minimum, `ecr:DescribeRepositories` policy attached to the credentials.
3. Network access to AWS ECR endpoints (no VPC restrictions blocking API calls).
4. Optional: Specific AWS region set via `--region` if not default.

## Defense

- Implement least privilege access: Restrict `ecr:DescribeRepositories` to only necessary roles and monitor usage via AWS CloudTrail.
- Enable AWS GuardDuty and CloudTrail logging to detect anomalous ECR API calls from unusual IPs or roles.
- Use AWS Organizations SCPs to deny broad ECR access across accounts.
- Regularly audit ECR repositories with AWS Config rules to identify unauthorized creations or accesses.

## Objectives

1. List all ECR repositories in the target AWS account to identify potential sensitive container images.
2. Gather metadata like ARNs and creation dates for further targeting or persistence planning.
3. Verify repository existence and image counts to assess the target's container deployment scale.

## Instructions

### Step 1: Configure AWS CLI and Verify Access

**Context**: Before enumerating repositories, ensure the AWS CLI is set up with credentials that have the required permissions. This step prevents authentication errors and confirms connectivity to ECR.

Use the [[tools/aws-cli]] to configure credentials if not already done:

```bash
aws configure
```

> Enter your Access Key ID, Secret Access Key, default region (e.g., us-east-1), and output format (json). Expected output: No errors, and subsequent `aws sts get-caller-identity` should return your account details without permission denied errors.

### Step 2: Enumerate ECR Repositories

**Context**: Execute the describe-repositories command to retrieve a list of all ECR repositories. This reveals the full inventory, helping identify targets for deeper inspection like pulling images or scanning for vulnerabilities.

**Command** ([[commands/aws-ecr-describe-repositories]]):

```bash
aws ecr describe-repositories
```

> This command queries the ECR service and returns a JSON array of repository objects. If repositories exist, it lists details; if none, an empty array. Review the output for repository names and ARNs to prioritize sensitive ones (e.g., those with 'prod' or 'secret' in the name).
