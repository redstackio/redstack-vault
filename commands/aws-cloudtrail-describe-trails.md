---
id: ca793cc6-0027-47ed-8feb-65657f53e5ad
name: aws-cloudtrail-describe-trails
type: command
executor: bash
data: aws cloudtrail describe-trails --region $_REGION
output: null
created_at: '2023-04-06T03:56:14.180227+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloudtrail
  - aws
  - logging
verified: true
validated: true
---

# aws-cloudtrail-describe-trails

## Command

```bash
aws cloudtrail describe-trails --region $_REGION
```

## Description

This command retrieves information about one or more CloudTrail trails in the specified AWS region, including details like trail name, ARN, logging status, and configuration flags such as multi-region and global events inclusion. Use it to verify trail existence and settings before or after modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region $_REGION | The AWS region to query (e.g., eu-west-1, us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws cloudtrail describe-trails --region eu-west-1
```

### Advanced Usage

To filter for a specific trail name:

```bash
aws cloudtrail describe-trails --trail-name-list example_trail --region eu-west-1
```

## Expected Output

Successful execution returns JSON with trail details:

```json
{
  "trailList": [
    {
      "Name": "example_trail",
      "IncludeGlobalServiceEvents": true,
      "IsMultiRegionTrail": true,
      "TrailARN": "arn:aws:cloudtrail:eu-west-1:123456789012:trail/example_trail",
      "LogFileValidationEnabled": false
    }
  ]
}
```

Look for configuration flags to confirm status.

## Related

- [[procedures/Disable-CloudTrail-on-Specific-Regions]]
- [[commands/aws-cloudtrail-update-trail-disable-logging]]
