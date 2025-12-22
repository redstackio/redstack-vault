---
id: a2a13e91-7aa1-4d67-bfdc-398daf969b89
name: AWS-ECR-Repository-Policy-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.561780+00:00'
updated_at: '2023-04-10T20:20:34.870840+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/ECR]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Repository Policy]]'
commands:
  - '[[commands/aws-ecr-get-repository-policy]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-ECR-Repository-Policy-Enumeration

## Summary

This procedure uses the AWS CLI to retrieve the JSON resource policy associated with a specified Amazon Elastic Container Registry (ECR) repository. By enumerating the policy, an attacker can identify permissions granted to various AWS principals such as users, roles, or accounts, revealing potential access paths for lateral movement, privilege escalation, or further discovery in a compromised AWS environment.

## Description

Amazon ECR is a managed Docker container registry service in AWS that allows storage, management, and deployment of container images. Each repository can have a resource policy that defines permissions for actions like pulling or pushing images. This procedure retrieves the policy using the `aws ecr get-repository-policy` command, which outputs a JSON document detailing allowed principals, actions, and conditions (e.g., IP restrictions or encryption requirements). In an attack scenario, this information helps map the AWS environment's access controls, identifying overly permissive policies that could enable unauthorized access to repositories or related resources. It is particularly useful during cloud discovery phases after initial credential compromise, providing insights into infrastructure without triggering alarms from more invasive actions.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least `ecr:GetRepositoryPolicy` permission on the target repository or broader ECR read access.
2. AWS CLI installed and configured with the compromised credentials (e.g., via `aws configure`).
3. Network access to AWS APIs (typically over HTTPS port 443); no direct VPC access to ECR is required if using public endpoints.
4. Knowledge of the target ECR repository name, which may be obtained from prior enumeration (e.g., listing repositories via `aws ecr describe-repositories`).

## Defense

- Implement least privilege access by scoping IAM policies to deny `ecr:GetRepositoryPolicy` unless explicitly needed, using conditions like MFA or source IP.
- Enable AWS CloudTrail logging for ECR API calls and monitor for anomalous `GetRepositoryPolicy` requests, especially from unexpected IPs or roles.
- Use AWS Organizations SCPs to restrict policy enumeration across accounts and integrate with SIEM for alerting on discovery patterns.
- Regularly audit and rotate ECR repository policies to minimize exposure of permission details.

## Objectives

1. Retrieve and analyze the JSON policy for a specific ECR repository to identify granted permissions and principals.
2. Discover potential misconfigurations, such as cross-account access or broad IAM role permissions, for planning lateral movement.
3. Map access controls without modifying resources, maintaining stealth during reconnaissance.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Before enumerating the policy, ensure the AWS CLI is set up with the compromised credentials and test basic ECR access to confirm permissions. This step prevents errors during policy retrieval and verifies the attacker's effective privileges.

**Command** ([[commands/aws-ecr-get-repository-policy]]):
```bash
aws ecr describe-repositories --repository-names $_REPOSITORY_NAME --region $_REGION
```

> This command lists details for the specified repository, confirming it exists and the credentials have read access. Replace `$_REPOSITORY_NAME` with the target repository (e.g., `my-app-repo`) and `$_REGION` with the AWS region (e.g., `us-east-1`). Expected output is a JSON response with repository metadata like ARN and creation date. If denied, adjust credentials or escalate privileges first.

### Step 2: Retrieve the Repository Policy

**Context**: Execute the core enumeration command to fetch the JSON policy. This reveals permissions, such as who can perform `ecr:BatchGetImage` or `ecr:PutImage`, and any conditions like IP allowlists.

**Command** ([[commands/aws-ecr-get-repository-policy]]):
```bash
aws ecr get-repository-policy --repository-name $_REPOSITORY_NAME --region $_REGION
```

> Run this after confirming repository access. The output is a JSON object under `policyText` with statements defining `Principal`, `Action`, `Effect`, and `Condition`. For example, it might show cross-account access from another AWS account ID. Pipe to `jq` for parsing if needed (e.g., `| jq '.policyText'`). Success is indicated by a valid JSON policy without access denied errors.

### Step 3: Analyze Policy for Attack Paths

**Context**: Review the retrieved policy to identify exploitable permissions. Look for broad principals (e.g., `*` or external accounts) or actions enabling further compromise, such as image pulls leading to code execution.

> Manually inspect the JSON for keys like `Principal.AWS` (IAM ARNs), `Action` (ECR operations), and `Condition` (restrictions). Document findings, such as roles with `ecr:*` permissions, for use in subsequent attacks like assuming those roles via STS. If the policy is empty or restrictive, pivot to other repositories or services.
