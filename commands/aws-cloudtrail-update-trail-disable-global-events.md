---
id: 21f1fa21-16a3-42bd-a601-4fbef3755104
name: aws-cloudtrail-update-trail-disable-global-events
type: command
executor: bash
data: >-
  aws cloudtrail update-trail --name $_TRAIL_NAME
  --no-include-global-service-events
output: null
created_at: '2023-04-06T03:56:14.157010+00:00'
updated_at: '2023-04-10T20:20:25.401034+00:00'
platforms:
  - AWS
tags:
  - cloudtrail
  - defense-evasion
verified: true
validated: true
---

# aws-cloudtrail-update-trail-disable-global-events

## Command

```bash
aws cloudtrail update-trail --name $_TRAIL_NAME --no-include-global-service-events
```

## Description

This AWS CLI command updates an existing CloudTrail trail to disable the logging of global service events. Global service events include management and control plane activities across AWS that might log attacker reconnaissance or configuration changes related to services like RDS. Use this during defense evasion phases to reduce log verbosity and avoid detection of cross-service actions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--name $_TRAIL_NAME` | The name of the CloudTrail trail to update (e.g., 'rds-monitoring-trail') | Yes |
| `--no-include-global-service-events` | Disables inclusion of global service events in the trail logs | Yes |

## Examples

### Basic Usage

```bash
aws cloudtrail update-trail --name rds-security-trail --no-include-global-service-events
```

### Advanced Usage

```bash
aws cloudtrail update-trail --name rds-security-trail --no-include-global-service-events --s3-bucket-name updated-logs-bucket
```

This example also updates the S3 bucket for logs while disabling global events.

## Expected Output

Successful execution returns a JSON object describing the updated trail:

```json
{
    "Name": "rds-security-trail",
    "IncludeGlobalServiceEvents": false,
    "S3BucketName": "original-bucket",
    "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/rds-security-trail",
    "LogFileValidationEnabled": false
}
```

Look for `"IncludeGlobalServiceEvents": false` to confirm the change. Errors may include `AccessDeniedException` if permissions are lacking or `TrailNotFoundException` if the trail name is invalid.

## Related

- [[procedures/Disable-Global-Service-Events-in-CloudTrail-for-RDS]]
- [[aws-cloudtrail-describe-trails]]
