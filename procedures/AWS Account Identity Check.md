---
id: "574953ed-45fa-4436-8c6e-9f0f4b11b6b8"
name: "AWS Account Identity Check"
type: procedure
verified: false
submitted: false
created_at: "2023-04-06T03:56:11.626346+00:00"
updated_at: "2023-04-10T20:19:48.459605+00:00"
tactics: []
techniques: []
sub_techniques: []
tags: []
commands: []
platforms: []
tools: []
---

# AWS Account Identity Check

## Summary

The AWS Account Identity Check procedure is used to determine which user is currently executing commands within an AWS environment. By using the 'Get AWS Caller Identity' command, the user can retrieve information about the AWS account that is currently being used. This information can be used to identify potential security risks, monitor user activity, and ensure proper access controls.

## Description

The AWS Account Identity Check procedure is used to determine which user is currently executing commands within an AWS environment. By using the 'Get AWS Caller Identity' command, the user can retrieve information about the AWS account that is currently being used. This information can be used to identify potential security risks, such as unauthorized access, and to monitor user activity within the environment. Additionally, this procedure can be used to ensure that the correct user is executing commands and to troubleshoot any issues related to user access. The attack scenario typically involves an adversary or tester verifying their assumed identity in a compromised AWS environment to facilitate further discovery or persistence. The target environment is AWS cloud infrastructure, with expected outcomes including the retrieval of account ID, ARN, and user ID for verification purposes. Prerequisites include valid AWS credentials and the AWS CLI installed.

## Requirements

1. Valid AWS credentials with appropriate permissions
2. AWS CLI installed and configured

## Defense

Defensive measures and detection strategies:

- Ensure that AWS credentials are securely stored and not shared among users
- Implement multi-factor authentication for AWS accounts
- Regularly monitor AWS account activity for suspicious behavior

## Objectives

1. Identify the user currently executing commands within an AWS environment
2. Monitor user activity within the environment
3. Ensure correct user access and troubleshoot access issues

## Instructions

### Step 1: Retrieve Caller Identity

**Context**: This step retrieves details about the AWS account associated with the credentials used, including the account ID, ARN, and user ID, to verify the current identity.

**Command** ([[Get AWS Caller Identity]]):
```bash
aws sts get-caller-identity
```

> The 'aws sts get-caller-identity' command is used to retrieve the AWS account identity. This command is useful when you need to verify which AWS account you are currently using. The command returns the account ID, ARN (Amazon Resource Name), and user ID associated with the credentials used to call the command. This information can be used to ensure that you are using the correct AWS account and to troubleshoot any issues related to AWS permissions or access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[Get AWS Caller Identity]]

## Tools Used


## Tags

- [[Checking which user is executing]]
- [[Cloud - AWS]]
- [[Persistence]]
