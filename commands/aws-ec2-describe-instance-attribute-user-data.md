---
id: 622a6c09-0697-461e-972b-34ea2ea05719
name: aws-ec2-describe-instance-attribute-user-data
type: command
executor: bash
data: >-
  aws ec2 describe-instance-attribute --attribute userData --instance-id
  $_INSTANCE_ID
output: null
created_at: '2023-04-06T03:56:13.274554+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - enumeration
verified: true
validated: true
---

# aws-ec2-describe-instance-attribute-user-data

## Command

```bash
aws ec2 describe-instance-attribute --attribute userData --instance-id $_INSTANCE_ID
```

## Description

This command retrieves the User Data attribute for a specific EC2 instance using the AWS CLI. User Data contains bootstrap scripts that may include sensitive information. Use this during cloud discovery to extract potential credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --attribute userData | Specifies the instance attribute to describe (fixed to userData for this command) | Yes |
| --instance-id $_INSTANCE_ID | The ID of the EC2 instance (e.g., i-0123456789abcdef0) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 describe-instance-attribute --attribute userData --instance-id i-0123456789abcdef0
```

### With Output Formatting (JSON)

```bash
aws ec2 describe-instance-attribute --attribute userData --instance-id i-0123456789abcdef0 --output json
```

## Expected Output

```
{
    "InstanceId": "i-0123456789abcdef0",
    "UserData": {
        "Value": "IyEvYmluL2Jhc2gKZWNobyAiUGFzc3dvcmQ6IHNlY3JldDEyMyIK"
    }
}
```

A successful response includes the Base64-encoded User Data in the `Value` field. Decode it to view the script. If no User Data exists, `Value` is null.
