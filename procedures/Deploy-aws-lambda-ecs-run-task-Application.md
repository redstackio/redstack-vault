---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - aws
  - lambda
  - deployment
  - misconfiguration
type: procedure
tools:
  - '[[tools/AWS-SAM-CLI]]'
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-aws-repo]]'
  - '[[commands/sam-build-deploy]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:27.410Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-aws-lambda-ecs-run-task-Application

## Summary

This procedure deploys the aws-lambda-ecs-run-task sample application from the AWS Labs GitHub repository, creating a Lambda function and an IAM role with excessive permissions, setting the stage for privilege escalation analysis.

## Description

The aws-lambda-ecs-run-task application is a sample that allows running ECS tasks from Lambda events, often used in SQS-triggered workflows. Deploying it results in a Lambda function named rLambdaFunction attached to rLambdaFunctionRole, which incorrectly includes the AdministratorAccess managed policy. This grants full AWS permissions, enabling any action if the Lambda is compromised. The procedure assumes access to an AWS account and uses SAM CLI for deployment, mimicking how a legitimate or malicious user might introduce the vulnerability.

## Requirements

1. AWS account with IAM permissions for Lambda, IAM, ECS, and SQS creation
2. AWS CLI and SAM CLI installed and configured with credentials
3. Git installed for repository cloning
4. Internet access to GitHub and AWS endpoints

## Defense

Defensive measures and detection strategies:

- Review and least-privilege IAM roles for Lambda functions during deployment
- Use AWS Config rules to detect AdministratorAccess attachments to service roles
- Monitor CloudTrail for unusual Lambda invocations or role creations

## Objectives

1. Deploy the application to replicate the vulnerable setup
2. Create the Lambda and IAM resources for inspection
3. Validate the environment for escalation potential

## Instructions

### Step 1: Clone the Repository

**Context**: Obtain the source code from the official AWS Labs GitHub repository to prepare for deployment.

**Command** ([[commands/git-clone-aws-repo]]):
```bash
git clone https://github.com/awslabs/aws-lambda-ecs-run-task.git
cd aws-lambda-ecs-run-task
```

> This clones the repo and navigates into the directory. Expected output: Repository files downloaded, no errors.

### Step 2: Build and Deploy with SAM

**Context**: Use AWS SAM to package and deploy the application stack, creating the Lambda function and IAM role.

**Command** ([[commands/sam-build-deploy]]):
```bash
sam build
sam deploy --guided
```

> The build step compiles the application. The deploy step prompts for stack name (e.g., rLambdaEcsRunTaskStack), region, and capabilities (CAPABILITY_IAM). Confirm to proceed. Expected output: Stack creation success with ARNs for Lambda and role.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-aws-repo]]
- [[commands/sam-build-deploy]]

## Tools Used

- [[tools/AWS-SAM-CLI]]
- [[tools/AWS-CLI]]

## Tags

- aws
- lambda
- deployment
