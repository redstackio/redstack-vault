---
id: 21f1fa21-16a3-42bd-a601-4fbef3755104
name: aws-cloudtrail-update-trail-no-global-events
type: command
executor: bash
data: >-
  aws cloudtrail update-trail --name $_TRAIL_NAME
  --no-include-global-service-events --profile $_PROFILE_NAME
output: null
created_at: '2023-04-06T03:56:14.157010+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - cloud
  - defense-evasion
verified: true
validated: true
---

# aws-cloudtrail-update-trail-no-global-events

## Command

```bash
aws cloudtrail update-trail --name $_TRAIL_NAME --no-include-global-service-events --profile $_PROFILE_NAME
```

## Description

This command updates an AWS CloudTrail trail to disable logging of global service events (e.g., IAM, STS), reducing the scope of audited activities while keeping regional logging active.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --name $_TRAIL_NAME | The name of the CloudTrail trail to update (e.g., cloudgoat_trail) | Yes |
| --no-include-global-service-events | Flag to exclude global service events from logging | Yes |
| --profile $_PROFILE_NAME | AWS CLI profile with cloudtrail:UpdateTrail permissions | Yes |

## Examples

### Basic Usage

```bash
aws cloudtrail update-trail --name cloudgoat_trail --no-include-global-service-events --profile administrator
```

### Combined with Other Flags

```bash
aws cloudtrail update-trail --name my-trail --no-include-global-service-events --s3-bucket-name secure-bucket --profile default
```

## Expected Output

{
    "Name": "cloudgoat_trail",
    "IncludeGlobalServiceEvents": false,
    "S3BucketName": "...",
    ...
}

The response shows the updated trail configuration. Errors may include "InsufficientPermissions" or "TrailNotProvided".

## Related

- [[procedures/Disable-CloudTrail-on-AWS]]
- [[commands/aws-cloudtrail-update-trail-single-region]]
