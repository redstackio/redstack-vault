---
id: c35b2229-01a2-4012-a7ba-b5f0c2aa94ef
name: aws-iam-list-instance-profiles
type: command
executor: bash
data: aws iam list-instance-profiles
output: null
created_at: '2023-04-06T03:56:13.506494+00:00'
updated_at: '2023-04-10T20:20:24.693573+00:00'
platforms:
  - AWS
tags:
  - cloud-aws
  - discovery
verified: true
validated: true
---

# aws-iam-list-instance-profiles

## Command

```bash
aws iam list-instance-profiles $_MAX_ITEMS --output $_OUTPUT_FORMAT
```

## Description

This command queries the AWS IAM service to list all instance profiles in the current account. Instance profiles contain IAM roles for EC2 instances, useful for discovering permissions during cloud reconnaissance and privilege escalation assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MAX_ITEMS | Maximum number of profiles to return per call (default: 100, max: 1000) | No |
| --output | Output format (json, text, table; default: json) | No |
| --query | JMESPath query to filter output (e.g., '.InstanceProfiles[].Arn') | No |

## Examples

### Basic Usage

```bash
aws iam list-instance-profiles
```
Lists all instance profiles in JSON format.

### Advanced Usage

```bash
aws iam list-instance-profiles --max-items 50 --output table --query 'InstanceProfiles[].{Name:InstanceProfileName, ARN:Arn}'
```
Returns a table of profile names and ARNs, limited to 50 items.

## Expected Output

Successful execution returns a JSON object with an InstanceProfiles array:

```json
{
    "InstanceProfiles": [
        {
            "Arn": "arn:aws:iam::123456789012:instance-profile/MyInstanceProfile",
            "CreateDate": "2023-01-01T00:00:00Z",
            "InstanceProfileId": "AIAABCDEF1234567890",
            "InstanceProfileName": "MyInstanceProfile",
            "Path": "/",
            "Roles": [
                {
                    "Arn": "arn:aws:iam::123456789012:role/MyRole",
                    "CreateDate": "2023-01-01T00:00:00Z",
                    "Path": "/",
                    "RoleId": "AROAABCDEF1234567890",
                    "RoleName": "MyRole"
                }
            ]
        }
    ]
}
```

If no profiles exist, returns an empty InstanceProfiles array. Errors occur if credentials lack iam:ListInstanceProfiles permission.

## Related

- [[procedures/AWS-Instance-Profile-Enumeration]]
- [[commands/aws-iam-get-role]]
