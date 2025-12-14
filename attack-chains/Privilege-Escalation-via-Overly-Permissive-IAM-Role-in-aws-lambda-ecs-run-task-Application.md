---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - aws
  - iam
  - lambda
  - privilege-escalation
  - misconfiguration
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Deploy-aws-lambda-ecs-run-task-Application]]'
  - '[[procedures/Inspect-and-Exploit-IAM-Role-Permissions]]'
step_count: 2
techniques:
  - '[[T1078.004]]'
  - '[[Sudo and Sudo Caching]]'
updated_at: '2025-12-14T17:30:27.411Z'
description: >-
  This attack chain exploits a misconfiguration in the aws-lambda-ecs-run-task
  application by deploying it to create a Lambda function with an IAM role
  granting full AdministratorAccess, enabling privilege escalation to root-level
  AWS permissions if the function is compromised.
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[T1078.004]]'
  - '[[Sudo and Sudo Caching]]'
---
# Privilege Escalation via Overly Permissive IAM Role in aws-lambda-ecs-run-task Application

Multi-stage attack chain demonstrating the deployment and exploitation of a misconfigured AWS Lambda application for privilege escalation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Deploy Application] --> B[Inspect Resources]
    B --> C[Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- AWS CLI
- AWS SAM CLI

### Target Environment

- AWS account with deployment permissions
- Required services: IAM, Lambda, ECS, SQS
- Network access: Internet connectivity for GitHub clone and AWS API calls

### Initial Access Requirements

- Valid AWS credentials with permissions to create Lambda functions, IAM roles, and deploy applications
- No prior compromise needed, but assumes legitimate deployment access

## Detailed Attack Procedures

### Step 1: Deploy the Application
procedure: [[procedures/Deploy-aws-lambda-ecs-run-task-Application]]

**Objective**: Deploy the aws-lambda-ecs-run-task sample application to create the vulnerable Lambda function and IAM role.

**Instructions**: Clone the repository from GitHub and use AWS SAM to build and deploy the application. Ensure AWS credentials are configured.

First, clone the repo:

```bash
git clone https://github.com/awslabs/aws-lambda-ecs-run-task.git
cd aws-lambda-ecs-run-task
```

Then build and deploy using SAM:

```bash
sam build
sam deploy --guided
```

Follow the prompts to set the stack name (e.g., rLambdaEcsRunTaskStack) and confirm deployment.

**Expected Output**: Successful deployment confirmation, with outputs including the Lambda function ARN and role ARN.

**Success Indicators**:
- Stack deployed without errors
- Lambda function rLambdaFunction created
- IAM role rLambdaFunctionRole attached

### Step 2: Inspect and Exploit IAM Role
procedure: [[procedures/Inspect-and-Exploit-IAM-Role-Permissions]]

**Objective**: Inspect the IAM role attached to the Lambda function to confirm AdministratorAccess policy, then demonstrate privilege escalation by invoking the function to perform unrestricted AWS actions.

**Instructions**: Use AWS CLI to describe the role and attached policies. If control is gained over the Lambda (e.g., via code injection or event trigger), invoke it to execute admin actions like listing all S3 buckets.

Describe the role:

```bash
aws iam get-role --role-name rLambdaFunctionRole
```

List attached policies:

```bash
aws iam list-attached-role-policies --role-name rLambdaFunctionRole
```

To exploit, update the Lambda code to run an admin command (e.g., via console or API) and invoke:

```bash
aws lambda invoke --function-name rLambdaFunction output.json --payload '{"command": "aws s3 ls"}'
```

**Expected Output**: Role description showing AdministratorAccess ARN (arn:aws:iam::aws:policy/AdministratorAccess). Invocation returns unrestricted AWS actions, e.g., full S3 bucket list.

**Success Indicators**:
- Policy confirms full admin access
- Lambda invocation performs root-level actions without denial

## Attack Chain Summary

### Key Achievements

1. Successful deployment of the vulnerable application
2. Identification of overly permissive IAM role
3. Demonstration of privilege escalation to full AWS administrator

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1078.004]]
- [[Sudo and Sudo Caching]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T12:00:00Z*
