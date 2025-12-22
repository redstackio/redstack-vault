---
id: 70a37702-4067-4cd6-858d-6b76ff12c9f7
name: Extract-AWS-EC2-Instance-User-Data
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.278262+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/aws]]'
  - '[[tags/cloud]]'
  - '[[tags/ec2]]'
  - '[[tags/enumeration]]'
  - '[[tags/user-data-extraction]]'
commands:
  - '[[commands/aws-ec2-describe-instance-attribute-user-data]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Extract-AWS-EC2-Instance-User-Data

## Summary

This procedure uses the AWS CLI to retrieve the User Data attribute from a specified EC2 instance, which may contain sensitive information such as bootstrap scripts with embedded passwords, API keys, or other configuration secrets passed during instance launch. It is useful in cloud penetration testing or red team engagements to discover credentials for further lateral movement or privilege escalation within an AWS environment.

## Description

In AWS, User Data allows administrators to pass configuration scripts to EC2 instances at boot time, often including sensitive data like database credentials or SSH keys. An attacker with compromised AWS credentials that permit EC2 describe permissions can extract this Base64-encoded User Data to uncover secrets. This technique targets the EC2 API and is particularly effective after initial access via misconfigured IAM roles or stolen keys. The output is a JSON response containing the User Data value, which can be decoded to reveal plaintext scripts. This procedure assumes the attacker has valid AWS credentials and focuses on a single instance; it can be chained with enumeration procedures to identify target instance IDs first.

## Requirements

1. Valid AWS credentials (access key and secret key) with at least `ec2:DescribeInstanceAttribute` permissions.
2. AWS CLI installed and configured with the target account's credentials (e.g., via `aws configure`).
3. The instance ID of the target EC2 instance.
4. Network access to AWS APIs (no direct instance access required).

## Defense

- Encrypt sensitive data in User Data scripts using tools like AWS KMS before launch.
- Implement least-privilege IAM policies to restrict `ec2:DescribeInstanceAttribute` access.
- Monitor AWS CloudTrail logs for unauthorized `DescribeInstanceAttribute` API calls, especially those targeting `userData`.
- Use AWS Config rules to audit and alert on exposed User Data containing secrets.

## Objectives

1. Retrieve the User Data attribute for a specified EC2 instance.
2. Decode and analyze the Base64-encoded script for sensitive information like passwords or API keys.
3. Use extracted secrets to enable further attacks such as lateral movement or privilege escalation.

## Instructions

### Step 1: Retrieve User Data Attribute

**Context**: Use the AWS CLI to query the EC2 API for the User Data of the target instance. This step requires knowing the instance ID, which can be obtained from prior enumeration (e.g., via `aws ec2 describe-instances`). The command returns a JSON object with the Base64-encoded User Data; decode it manually if needed using `base64 -d`.

**Command** ([[commands/aws-ec2-describe-instance-attribute-user-data]]):
```bash
aws ec2 describe-instance-attribute --attribute userData --instance-id $_INSTANCE_ID
```

> This command queries the specified instance's User Data. Replace `$_INSTANCE_ID` with the actual ID (e.g., `i-0123456789abcdef0`). If successful, it outputs JSON with a `UserData` field containing the Base64 value. Decode the value to inspect for secrets. If the instance has no User Data, the field will be empty or null.

### Step 2: Decode and Analyze Output

**Context**: The raw output is Base64-encoded, so decode it to reveal the script. This step verifies the presence of sensitive data and documents findings for reporting or further exploitation.

**Command**:
```bash
echo '$_USER_DATA_BASE64' | base64 -d
```

> Pipe the Base64 string from the previous step's output into `base64 -d` (on Linux/macOS) or use PowerShell's `[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('$_USER_DATA_BASE64'))` on Windows. Look for patterns like `password=`, `API_KEY=`, or SSH commands indicating secrets.
