---
tags:
  - aws
  - serverless
  - deployment
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
  - '[[tools/SAM-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/aws-serverlessrepo-create-cloud-formation-change-set]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:30:26.677Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d82d6251-87c9-46f8-b0bb-998695a1d700
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Deploy-AWS-Serverless-Application

## Summary

This procedure deploys the experimental-programmatic-access-ccft application from the AWS Serverless Application Repository, creating a Lambda function with an associated IAM role that has overly permissive policies.

## Description

In an AWS environment, the Serverless Application Repository allows quick deployment of pre-built applications. The target application includes a Lambda function (ExtractCarbonEmissionsFunction) whose IAM role grants sts:AssumeRole on all resources, enabling potential privilege escalation. This step sets up the vulnerable resources in the deploying account, assuming the attacker has deployment permissions.

## Requirements

1. AWS CLI installed and configured with credentials having serverlessrepo:CreateCloudFormationChangeSet and iam:CreateRole permissions
2. Access to the us-east-1 region (or adjust ARN accordingly)
3. AWS account within the target organization

## Defense

Defensive measures and detection strategies:

- Implement AWS Organizations SCPs to restrict Serverless Application Repository deployments
- Use IAM permissions boundaries on all roles created via CloudFormation/Serverless
- Monitor CloudTrail for CreateCloudFormationChangeSet events on sensitive applications

## Objectives

1. Deploy the application stack successfully
2. Create the vulnerable IAM role
3. Prepare for policy review and exploitation

## Instructions

### Step 1: Configure AWS CLI

**Context**: Ensure AWS credentials are set for the deploying account.

**Command** ([[commands/aws-configure]]):
```bash
aws configure
```

> Enter access key, secret key, region (e.g., us-east-1), and output format (json). This authenticates the session.

### Step 2: Deploy the Application

**Context**: Create a CloudFormation change set for the Serverless application, which deploys the Lambda and IAM role.

**Command** ([[commands/aws-serverlessrepo-create-cloud-formation-change-set]]):
```bash
aws serverlessrepo create-cloud-formation-change-set --application-id arn:aws:serverlessrepo:us-east-1:123456789012:applications~experimental-programmatic-access-ccft --stack-name experimental-app --capabilities CAPABILITY_IAM
```

> This command initiates deployment. Monitor status with `aws cloudformation describe-stacks --stack-name experimental-app`. Expected output includes StackId upon success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used

- [[commands/aws-configure]]
- [[commands/aws-serverlessrepo-create-cloud-formation-change-set]]

## Tools Used

- [[tools/AWS-CLI]]
- [[tools/SAM-CLI]]

## Tags

- aws
- deployment
- serverless
