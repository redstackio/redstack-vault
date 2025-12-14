---
id: cmd-nonprod-001
data: >-
  aws devicefarm get-account-settings --region us-west-2 --endpoint-url
  https://nonprod.devicefarm.us-west-2.amazonaws.com
tags:
  - aws
  - devicefarm
  - non-production
  - silent
type: command
output: JSON if permitted or error; no CloudTrail log
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.634Z'
verified: false
validated: true
submitted: true
---
# aws-devicefarm-get-account-settings-non-production

## Command

```bash
aws devicefarm get-account-settings --region us-west-2 --endpoint-url https://nonprod.devicefarm.us-west-2.amazonaws.com
```

## Description

Retrieves AWS Device Farm account settings via a non-production endpoint, bypassing CloudTrail logging while still checking IAM permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | Specifies the AWS region (e.g., us-west-2) | Yes |
| `--endpoint-url` | Overrides to non-production URL (e.g., https://nonprod.devicefarm.us-west-2.amazonaws.com) | Yes |

## Examples

### Basic Usage

```bash
aws devicefarm get-account-settings --region us-west-2 --endpoint-url https://nonprod.devicefarm.us-west-2.amazonaws.com
```

### With Different Endpoint

```bash
aws devicefarm get-account-settings --region us-west-2 --endpoint-url https://nonprod2.devicefarm.us-west-2.amazonaws.com
```

## Expected Output

JSON response if access allowed, or {"Error": {"Code": "AccessDenied", "Message": "User is not authorized"}}; no CloudTrail log even after 10+ minutes.

## Related

- [[commands/aws-devicefarm-get-account-settings-production]]
- [[procedures/Test-Non-Production-Endpoint-for-Silent-API-Calls]]
