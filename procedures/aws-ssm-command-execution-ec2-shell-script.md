---
id: f28a17d5-2d00-4937-b404-6fb193a5a9f8
name: aws-ssm-command-execution-ec2-shell-script
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.697991Z'
updated_at: '2023-04-10T20:20:49.923677Z'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - '[[sub-techniques/Cloud Services|T1021.007 - Cloud Services]]'
tags:
  - '[[tags/AWS - SSM - Command execution]]'
  - '[[tags/Cloud - AWS]]'
commands:
  - '[[commands/aws-ssm-describe-instance-information]]'
  - '[[commands/aws-ssm-send-shell-script-command]]'
  - '[[commands/aws-ssm-list-command-invocations]]'
platforms:
  - AWS
  - Linux
  - Windows
tools: []
validated: true
---

# aws-ssm-command-execution-ec2-shell-script

## Summary

This procedure uses AWS Systems Manager (SSM) to execute shell scripts on EC2 instances, enabling remote command execution without SSH access. In offensive security, it allows attackers with compromised AWS credentials to run arbitrary code on instances for lateral movement, data exfiltration, or persistence within a cloud environment.

## Description

AWS SSM provides a secure way to manage and execute commands on EC2 instances via the SSM Agent installed on the target. This procedure leverages the AWS CLI to describe instance information, send shell script commands using the AWS-RunShellScript document, and retrieve execution results. It requires appropriate IAM permissions like AmazonSSMFullAccess or custom policies allowing ssm:SendCommand and ssm:GetCommandInvocation. From an attacker's perspective, this technique is useful after credential compromise to pivot across instances, execute payloads, or gather information without opening inbound ports. The process works across Linux and Windows instances where the SSM Agent is active and the instance role permits SSM interactions.

## Requirements

1. AWS CLI installed and configured with compromised credentials (e.g., access key and secret key via --profile).
2. SSM Agent installed and running on the target EC2 instance.
3. IAM role attached to the EC2 instance with permissions for SSM (e.g., AmazonSSMManagedInstanceCore policy).
4. Attacker's AWS account must have permissions for ssm:DescribeInstanceInformation, ssm:SendCommand, and ssm:ListCommandInvocations.
5. Network connectivity from the attacker's environment to AWS endpoints (no direct access to the instance needed).

## Defense

- Implement least-privilege IAM policies for EC2 instance roles, restricting SSM commands to approved documents and parameters.
- Enable AWS CloudTrail logging for SSM API calls and monitor for unusual SendCommand invocations via Amazon GuardDuty or custom CloudWatch alarms.
- Regularly audit SSM Agent installations and ensure instances are not overly permissive.
- Use AWS Organizations SCPs to limit SSM usage in sensitive environments.
- Monitor EC2 instance metadata for unauthorized command executions and implement just-in-time access for SSM.

## Objectives

1. Identify SSM-managed EC2 instances using describe-instance-information.
2. Execute arbitrary shell scripts on target instances for code execution or reconnaissance.
3. Retrieve command outputs to confirm success and gather results for further attacks.

## Instructions

### Step 1: Identify SSM-Managed Instances

**Context**: Query AWS SSM to list EC2 instances registered with Systems Manager, confirming which are accessible for command execution. This step verifies prerequisites and targets specific instances by ID or tags.

**Command** ([[commands/aws-ssm-describe-instance-information]]):
```bash
aws ssm describe-instance-information --profile $_PROFILE --region $_REGION
```

> This command retrieves details like InstanceId, PingStatus, and PlatformType. Filter output using --query for specific instances (e.g., --query 'InstanceInformationList[?contains(InstanceId, `i-`)]'). Expected output includes a JSON array of instances; success is indicated by 'PingStatus': 'Online' for target instances.

### Step 2: Send Shell Script Command to Instance

**Context**: Use the send-command API to execute a shell script on the target EC2 instance via the AWS-RunShellScript document. This allows running commands like ifconfig, whoami, or custom payloads (e.g., curl to an attacker server). Replace placeholders with actual values and ensure the script is URL-encoded if multi-line.

**Command** ([[commands/aws-ssm-send-shell-script-command]]):
```bash
aws ssm send-command --instance-ids "$_INSTANCE_ID" --document-name "AWS-RunShellScript" --comment "$_COMMENT" --parameters commands="$_SHELL_SCRIPT" --output text --query "Command.CommandId" --profile $_PROFILE --region $_REGION
```

> The command returns the CommandId for tracking. For example, to run 'whoami', set $_SHELL_SCRIPT to 'whoami'. Expected output is the CommandId string (e.g., '12345678-1234-1234-1234-123456789012'). If the instance is offline or lacks permissions, it fails with an AccessDeniedException.

### Step 3: Retrieve Command Execution Results

**Context**: Poll the command invocation status and output to verify execution and collect results. This step includes decision points: if status is 'Pending', wait and retry; if 'Failed', investigate logs.

**Command** ([[commands/aws-ssm-list-command-invocations]]):
```bash
aws ssm list-command-invocations --command-id "$_COMMAND_ID" --details --query "CommandInvocations[].CommandPlugins[].{Status:Status,Output:Output}" --profile $_PROFILE --region $_REGION
```

> This retrieves the status (Success, Failed, etc.) and stdout/stderr output. For a successful 'whoami' command, output might show 'ec2-user' or similar. If status is 'Success', proceed; otherwise, check for errors like timeouts or permission issues.
