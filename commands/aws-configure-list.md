---
id: c939a2e5-cb54-4e43-b7e6-498fc818347e-1
name: aws-configure-list
type: command
executor: bash
data: aws configure list
output: null
created_at: '2023-04-06T03:56:10.035383+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - configuration
verified: true
validated: true
---

# aws-configure-list

## Command

```bash
aws configure list
```

## Description

Displays the current configuration values for the AWS CLI, including default region, output format, and credential profile. Use this before IAM operations to verify setup without running sensitive queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; shows global config | No |

## Examples

### Basic Usage

```bash
aws configure list
```

### With Profile

```bash
aws configure list --profile custom-profile
```

## Expected Output

```
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile            <not set>             None    None
access_key     ****************ABCD   config-file   ~/.aws/config
secret_key     ****************XXXX   config-file   ~/.aws/config
region            us-east-1              config-file   ~/.aws/config
```

## Related

- [[commands/aws-iam-list-groups-for-user]]
- [[commands/aws-iam-list-groups-for-user]]
