---
id: d4c5bebe-3612-4705-9418-75032b8a7d13
name: Enumerate-AWS-ECR-Repositories
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.533403+00:00'
updated_at: '2023-04-10T20:19:57.949584+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/ECR]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing all repositories in container registry]]'
commands:
  - '[[commands/aws-ecr-describe-repositories]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Enumerate-AWS-ECR-Repositories

## Summary

This procedure uses the AWS CLI to list all repositories in an Elastic Container Registry (ECR), providing details such as repository names, URIs, creation dates, and image counts. It enables attackers to map out available container images for potential exploitation, such as identifying sensitive or outdated images that could be pulled and analyzed for vulnerabilities or embedded credentials.

## Description

In a cloud attack scenario, enumerating ECR repositories allows discovery of container assets within an AWS environment. With valid AWS credentials (e.g., access keys or IAM roles), the AWS CLI tool queries the ECR service to retrieve a comprehensive list of repositories. This information reveals the structure of the container registry, helping attackers prioritize targets for further actions like image pulling, credential extraction from images, or lateral movement via container workloads. The procedure assumes the AWS CLI is configured with appropriate permissions (e.g., ecr:DescribeRepositories). Expected outcomes include a JSON response detailing repository metadata, which can be parsed for actionable intelligence. This technique is particularly useful in post-compromise scenarios where initial access to AWS services has been achieved.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., via `aws configure` or environment variables).
2. IAM permissions including `ecr:DescribeRepositories` for the authenticated principal.
3. Network access to AWS endpoints (no VPC-specific restrictions).
4. Target AWS region set (default is us-east-1 if not specified).

## Defense

- Implement least-privilege IAM policies to restrict `ecr:DescribeRepositories` access to necessary roles only.
- Enable AWS CloudTrail logging for ECR API calls to monitor unauthorized enumeration attempts.
- Use AWS Organizations SCPs to deny broad ECR access across accounts.
- Regularly audit ECR repositories and rotate credentials to limit exposure.

## Objectives

1. Retrieve a list of all ECR repositories and their metadata.
2. Identify potentially valuable container images for subsequent exploitation.
3. Gain insight into the target's container registry structure without alerting defenses.

## Instructions

### Step 1: Verify AWS CLI Configuration and Authentication

**Context**: Ensure the AWS CLI is properly set up and authenticated to avoid permission errors during enumeration. This step confirms access to ECR services.

Use [[commands/aws-configure-list]] to check current configuration:

```bash
aws configure list
```

> This command displays profile settings, region, and output format. Expected output includes credential source (e.g., shared-credentials-file) and no errors. If not configured, run `aws configure` to set access key, secret key, region, and output format (json).

**Success Criteria**: Output shows valid credential source and default region without authentication failures.

### Step 2: Execute ECR Repository Enumeration

**Context**: Query the ECR service to list all repositories, retrieving details like names and image counts for attack planning.

Execute [[commands/aws-ecr-describe-repositories]]:

```bash
aws ecr describe-repositories
```

> This command calls the AWS ECR API to return a JSON array of repository objects. If repositories exist, it lists details; otherwise, returns an empty array. Use `--region` flag if targeting a specific region (e.g., `aws ecr describe-repositories --region us-west-2`).

**Success Criteria**: JSON response with "repositories" array populated; no AccessDenied errors.

### Step 3: Parse and Review Output for Insights

**Context**: Analyze the JSON output to extract key details, such as repository URIs for potential image pulls or identification of sensitive repositories.

Use [[commands/jq-parse-json]] or manual inspection:

```bash
aws ecr describe-repositories | jq '.repositories[] | {repositoryName, repositoryUri, createdAt, imageCount}'
```

> This pipes the output to jq for formatted viewing. Expected output: Structured list of repositories with names, URIs, creation dates, and image counts. Look for high-image-count repositories indicating active use.

**Success Criteria**: Extracted details reveal at least one repository; URIs can be used for follow-on actions like `aws ecr get-login-password` for pulls.
