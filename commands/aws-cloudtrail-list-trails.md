---
type: command
executor: bash
data: aws cloudtrail list-trails
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - AWS
  - CloudTrail
  - Discovery
verified: true
validated: true
---

# aws-cloudtrail-list-trails

## Command

```bash
aws cloudtrail list-trails
```

## Description

This command lists all CloudTrail trails in the current AWS account or profile, returning metadata such as trail names, ARNs, home regions, and inclusion flags for management events. Use it during cloud reconnaissance to discover logging configurations without retrieving actual logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This command has no required parameters; it queries all trails by default. | No |
| `--max-items` | Limits the number of trails returned (default: 100). | No |
| `--starting-token` | Token for pagination if more than the max items exist. | No |
| `--region` | Specifies the AWS region (defaults to default region). | No |

## Examples

### Basic Usage

```bash
aws cloudtrail list-trails
```

### Paginated Usage

```bash
aws cloudtrail list-trails --max-items 50 --starting-token eyJhIjoiVG9rZW4ifQ==
```

### Filtered Output with jq

```bash
aws cloudtrail list-trails | jq '.Trails[] | select(.IsMultiRegionTrail == true) | .Name'
```

## Expected Output

Successful execution returns JSON like:

```json
{
    "Trails": [
        {
            "Name": "default-trail",
            "IncludeGlobalServiceEvents": true,
            "IsMultiRegionTrail": true,
            "HomeRegion": "us-east-1",
            "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/default-trail"
        }
    ],
    "IsTruncated": false
}
```

Look for the `Trails` array; an empty array indicates no trails are configured.

## Related

- [[procedures/List-AWS-CloudTrail-Trails]] (procedure that uses this command)
- [[commands/aws-cloudtrail-describe-trails]] (related command for detailed trail info)
