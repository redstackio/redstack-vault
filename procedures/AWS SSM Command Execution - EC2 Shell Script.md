---
id: f28a17d5-2d00-4937-b404-6fb193a5a9f8
name: AWS SSM Command Execution - EC2 Shell Script
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.697991+00:00'
updated_at: '2023-04-10T20:20:49.923677+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Windows Remote Management|T1021.006 - Windows Remote Management]]'
tags:
- '[[AWS - SSM - Command execution]]'
- '[[Cloud - AWS]]'
commands:
- '[[Describe Instance Information]]'
- '[[List Command Invocations]]'
- '[[Send Shell Script Command]]'
---

# AWS SSM Command Execution - EC2 Shell Script

## Summary

This procedure involves using AWS Systems Manager (SSM) to execute a shell script on an EC2 instance. This can be useful for automating tasks or performing actions on multiple instances at once. From an offensive perspective, an attacker could use this technique to execute malicious code on comprom

## Description

# Description

This procedure involves using AWS Systems Manager (SSM) to execute a shell script on an EC2 instance. This can be useful for automating tasks or performing actions on multiple instances at once. From an offensive perspective, an attacker could use this technique to execute malicious code on compromised instances or pivot to other systems within the AWS environment. From a technical standpoint, SSM uses a combination of AWS Identity and Access Management (IAM) roles, SSM agents, and the SSM service to securely execute commands on instances without the need for SSH access. The business value of this procedure is increased efficiency and automation of tasks, as well as improved security by limiting direct access to instances.

## Requirements

1. AWS account with SSM service enabled

1. SSM agent installed on EC2 instance

1. IAM role with SSM permissions assigned to EC2 instance

## Defense

1. Ensure that IAM roles assigned to EC2 instances have the least privilege necessary to perform their intended tasks

1. Monitor SSM activity logs for suspicious or unauthorized commands

1. Regularly update and patch EC2 instances to prevent vulnerabilities that could be exploited by attackers

## Objectives

1. Execute a shell script on one or multiple EC2 instances

1. Automate tasks and increase efficiency

1. Limit direct access to instances for improved security

# Instructions

1. To execute a shell script on an EC2 instance using AWS SSM, follow these steps:
1. Use the `aws ssm describe-instance-information` command to get details about the instance.
2. Use the `aws ssm send-command` command to send a shell script to the instance. Specify the instance ID, the name of the AWS Systems Manager document (in this case, `AWS-RunShellScript`), the comment (optional), the shell script to execute, and the output format.
3. Use the `aws ssm list-command-invocations` command to check the status and output of the command execution.
Note: Make sure that the ssm-user account is not removed from the system when SSM Agent is uninstalled.

**Code**: [[$ aws ssm describe-instance-information --profile ]]

> The `aws ssm describe-instance-information` command is used to get information about the EC2 instances that are registered with AWS Systems Manager.
The `aws ssm send-command` command is used to execute a command (in this case, a shell script) on the specified EC2 instance. The `instance-ids` parameter specifies the ID of the instance, the `document-name` parameter specifies the name of the AWS Systems Manager document (in this case, `AWS-RunShellScript`), the `comment` parameter is optional and can be used to provide additional information about the command, the `commands` parameter specifies the shell script to execute, the `output` parameter specifies the output format (in this case, `text`), and the `query` parameter specifies the ID of the command that was executed.
The `aws ssm list-command-invocations` command is used to get the details (status and output) of a command that was executed using AWS Systems Manager.

**Command** ([[Describe Instance Information]]):

```bash
$ aws ssm describe-instance-information --profile stolencreds --region eu-west-1
```

**Command** ([[Send Shell Script Command]]):

```bash
$ aws ssm send-command --instance-ids "INSTANCE-ID-HERE" --document-name "AWS-RunShellScript" --comment "IP Config" --parameters commands=ifconfig --output text --query "Command.CommandId" --profile stolencreds
```

**Command** ([[List Command Invocations]]):

```bash
$ aws ssm list-command-invocations --command-id "COMMAND-ID-HERE" --details --query "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}" --profile stolencreds
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Windows Remote Management|T1021.006 - Windows Remote Management]]

## Commands Used

- [[Describe Instance Information]]
- [[List Command Invocations]]
- [[Send Shell Script Command]]

## Tags

- [[AWS - SSM - Command execution]]
- [[Cloud - AWS]]
