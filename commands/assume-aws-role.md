---
id: 1d6c3e9f-d184-49e4-bddb-80f30ed29da0
name: assume-aws-role
type: command
executor: bash
data: aws sts assume-role --role-arn $_ROLE_ARN --role-session-name $_SESSION_NAME
output: null
created_at: '2023-04-06T03:56:10.902494+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - iam
  - persistence
verified: true
validated: true
---

# assume-aws-role

## Command

```bash
aws sts assume-role --role-arn $_ROLE_ARN --role-session-name $_SESSION_NAME
```

## Description

This command requests temporary security credentials from AWS STS to assume an IAM role. It allows an entity with permission to obtain short-lived credentials that grant the permissions defined in the role's policy. Use this during post-exploitation to escalate privileges or maintain access in an AWS environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --role-arn ($_ROLE_ARN) | The Amazon Resource Name (ARN) of the role to assume (e.g., arn:aws:iam::account-id:role/RoleName) | Yes |
| --role-session-name ($_SESSION_NAME) | An identifier for the assumed role session, used for logging and tracking (alphanumeric, up to 64 characters) | Yes |

## Examples

### Basic Usage

```bash
aws sts assume-role --role-arn arn:aws:iam::123456789012:role/MyRole --role-session-name attacker-session
```

### Advanced Usage

```bash
aws sts assume-role --role-arn arn:aws:iam::123456789012:role/MyRole --role-session-name attacker-session --duration-seconds 3600
```

## Expected Output

Successful execution returns a JSON object with temporary credentials:

```json
{
    "Credentials": {
        "AccessKeyId": "ASIA...",
        "SecretAccessKey": "...",
        "SessionToken": "...",
        "Expiration": "2023-10-01T01:00:00Z"
    },
    "AssumedRoleUser": {
        "Arn": "arn:aws:sts::123456789012:assumed-role/MyRole/attacker-session",
        "AssumedRoleId": "AKIA... :attacker-session"
    }
}
```

Errors include "AccessDenied" if the caller lacks permission to assume the role.

## Related

- [[procedures/Assume-AWS-Role-for-Persistence]]
- [[tools/aws-cli]]
