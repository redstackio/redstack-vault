---
id: 0506271c-77f4-4d11-830e-fbd2284d213f
name: aws-cloudtrail-update-trail-single-region
type: command
executor: bash
data: >-
  aws cloudtrail update-trail --name $_TRAIL_NAME
  --no-include-global-service-events --no-is-multi-region-trail --region
  $_REGION --profile $_PROFILE_NAME
output: null
created_at: '2023-04-06T03:56:09.750264+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - cloud
  - defense-evasion
verified: true
validated: true
---

# aws-cloudtrail-update-trail-single-region

## Command

```bash
aws cloudtrail update-trail --name $_TRAIL_NAME --no-include-global-service-events --no-is-multi-region-trail --region $_REGION --profile $_PROFILE_NAME
```

## Description

This command updates an AWS CloudTrail trail to operate in a single region only, disabling multi-region and global event logging to limit audit coverage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --name $_TRAIL_NAME | Name of the trail to update (e.g., cloudgoat_trail) | Yes |
| --no-include-global-service-events | Exclude global services from logging | Yes |
| --no-is-multi-region-trail | Disable multi-region trail status | Yes |
| --region $_REGION | Target AWS region (e.g., eu-west-1) | Yes |
| --profile $_PROFILE_NAME | AWS CLI profile with update permissions | Yes |

## Examples

### Basic Usage

```bash
aws cloudtrail update-trail --name cloudgoat_trail --no-include-global-service-events --no-is-multi-region-trail --region eu-west-1 --profile administrator
```

### For US East Region

```bash
aws cloudtrail update-trail --name my-trail --no-include-global-service-events --no-is-multi-region-trail --region us-east-1 --profile default
```

## Expected Output

{
    "Name": "cloudgoat_trail",
    "IncludeGlobalServiceEvents": false,
    "IsMultiRegionTrail": false,
    "HomeRegion": "eu-west-1",
    ...
}

Confirms the trail is now single-region. Errors include region mismatches or permission issues.

## Related

- [[procedures/Disable-CloudTrail-on-AWS]]
- [[commands/aws-cloudtrail-update-trail-no-global-events]]
