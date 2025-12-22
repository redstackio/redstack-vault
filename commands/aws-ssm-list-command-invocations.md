---
id: 464d14ea-991d-4394-b52e-0d67c1b7e183
name: aws-ssm-list-command-invocations
type: command
executor: bash
data: >-
  aws ssm list-command-invocations --command-id "$_COMMAND_ID" --details --query
  "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}"
  --profile $_PROFILE --region $_REGION
output: null
created_at: '2023-04-06T03:56:09.691524Z'
updated_at: '2023-04-10T20:20:49.939502Z'
platforms:
  - AWS
tags:
  - aws
  - ssm
  - post-exploitation
verified: true
validated: true
---

# aws-ssm-list-command-invocations

## Command

```bash
aws ssm list-command-invocations --command-id "$_COMMAND_ID" --details --query "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}" --profile $_PROFILE --region $_REGION
```

## Description

This command retrieves the status and output of a previously sent SSM command invocation, allowing verification of execution success and collection of results like command stdout.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --command-id $_COMMAND_ID | ID of the command to query (from send-command output) | Yes |
| --details | Include plugin output details (stdout, stderr) | Yes |
| --query | JMESPath to extract status and output | Yes |
| --profile $_PROFILE | AWS CLI profile with SSM permissions | Yes |
| --region $_REGION | AWS region of the command | Yes |

## Examples

### Basic Usage

```bash
aws ssm list-command-invocations --command-id "12345678-1234-1234-1234-123456789012" --details --query "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}" --profile stolencreds
```

### With Specific Region

```bash
aws ssm list-command-invocations --command-id "COMMAND-ID-HERE" --details --profile stolencreds --region us-east-1
```

## Expected Output

```
[
    {
        "Status": "Success",
        "Output": "ec2-user\n"
    }
]
```

Success shows 'Status': 'Success' with relevant output; failures include error details in Output.

## Related

- [[commands/aws-ssm-send-shell-script-command]]
- [[procedures/aws-ssm-command-execution-ec2-shell-script]]
