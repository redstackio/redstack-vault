---
id: c939a2e5-cb54-4e43-b7e6-498fc818347e
name: aws-iam-list-groups-for-user
type: command
executor: bash
data: aws iam list-groups-for-user --user-name $_USER_NAME
output: null
created_at: '2023-04-06T03:56:10.035383+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - iam
  - discovery
verified: true
validated: true
---

# aws-iam-list-groups-for-user

## Command

```bash
aws iam list-groups-for-user --user-name $_USER_NAME
```

## Description

Lists all IAM groups that the specified user belongs to, returning group names and ARNs. Requires iam:ListGroupsForUser permission; useful for mapping user access in reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_USER_NAME | The name of the IAM user (e.g., 'target-user') | Yes |
| --output json | Format output as JSON (default) | No |

## Examples

### Basic Usage

```bash
aws iam list-groups-for-user --user-name target-user
```

### With JSON Output Specified

```bash
aws iam list-groups-for-user --user-name target-user --output json
```

## Expected Output

```json
{
    "Groups": [
        {
            "GroupName": "Administrators",
            "GroupId": "AIDACKCEVSQ6C2EXAMPLE",
            "Arn": "arn:aws:iam::123456789012:group/Administrators"
        }
    ]
}
```

If no groups: {"Groups": []}

## Related

- [[commands/aws-configure-list]]
- [[commands/aws-iam-list-groups-for-user]]
