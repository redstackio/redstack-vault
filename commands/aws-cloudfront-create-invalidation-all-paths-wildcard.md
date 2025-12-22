---
type: command
executor: bash
data: >-
  aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths
  "/*"
output: null
platforms:
  - Cloud
tags:
  - aws
  - cloudfront
  - invalidation
verified: true
validated: true
---

# aws-cloudfront-create-invalidation-all-paths-wildcard

## Command

```bash
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths "/*"
```

## Description

This command creates a wildcard invalidation for an entire AWS CloudFront distribution, clearing all cached objects and forcing a full refresh from the origin. It's ideal for scenarios requiring a complete cache purge, such as after significant origin changes, but consumes high quota (equivalent to 1,000 paths).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --distribution-id | The ID of the CloudFront distribution (e.g., E123ABC456DEF) | Yes |
| --paths | The wildcard path to invalidate all objects ("/*") | Yes |
| $DISTRIBUTION_ID | Environment variable or placeholder for the distribution ID | Yes |

## Examples

### Basic Usage

```bash
aws cloudfront create-invalidation --distribution-id E123ABC456DEF --paths "/*"
```

### Advanced Usage

For scripting, combine with output capture:

```bash
INVALIDATION_ID=$(aws cloudfront create-invalidation --distribution-id E123ABC456DEF --paths "/*" --query 'Invalidation.Id' --output text)
echo "Invalidation ID: $INVALIDATION_ID"
```

## Expected Output

Successful execution returns a JSON response with the invalidation details:

```json
{
    "Invalidation": {
        "Id": "I7G8H9I0J1K2L3",
        "Status": "InProgress",
        "CreateTime": "2023-10-01T12:05:00.000Z",
        "InvalidationBatch": {
            "Paths": {
                "Items": ["/*"],
                "Quantity": 1
            },
            "CallerReference": "cli-20231001T120500"
        }
    }
}
```
Monitor status with get-invalidation for completion.

## Related

- [[commands/aws-cloudfront-create-invalidation-specific-paths]]
- [[procedures/Invalidate-Files-in-AWS-CloudFront-Distribution]]
