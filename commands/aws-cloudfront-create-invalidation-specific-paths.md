---
type: command
executor: bash
data: >-
  aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths
  "$FILE_PATH" "$FILE_PATH_2"
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

# aws-cloudfront-create-invalidation-specific-paths

## Command

```bash
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths "$FILE_PATH" "$FILE_PATH_2"
```

## Description

This command creates an invalidation for specific file paths in a CloudFront distribution, forcing the CDN to refresh those objects from the origin. Use it when you need to update targeted cached content, such as modified web pages or assets, without affecting the entire cache.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --distribution-id | The ID of the CloudFront distribution (e.g., E123ABC456DEF) | Yes |
| --paths | Space-separated list of paths to invalidate (e.g., "/index.html" "/error.html"), each starting with / and quoted if containing spaces | Yes |
| $DISTRIBUTION_ID | Environment variable or placeholder for the distribution ID | Yes |
| $FILE_PATH | Placeholder for the first path to invalidate | Yes |
| $FILE_PATH_2 | Placeholder for an additional path (optional; command supports multiple) | No |

## Examples

### Basic Usage

```bash
aws cloudfront create-invalidation --distribution-id E123ABC456DEF --paths "/index.html" "/error.html"
```

### Advanced Usage

```bash
aws cloudfront create-invalidation --distribution-id E123ABC456DEF --paths "/images/logo.png" "/css/style.css" "/js/script.js"
```

## Expected Output

Successful execution returns a JSON response indicating the invalidation creation:

```json
{
    "Invalidation": {
        "Id": "I2A1B2C3D4E5F6",
        "Status": "InProgress",
        "CreateTime": "2023-10-01T12:00:00.000Z",
        "InvalidationBatch": {
            "Paths": {
                "Items": ["/index.html", "/error.html"],
                "Quantity": 2
            },
            "CallerReference": "cli-20231001T120000"
        }
    }
}
```
The status will update to "Completed" once processed.

## Related

- [[commands/aws-cloudfront-create-invalidation-all-paths-wildcard]]
- [[procedures/Invalidate-Files-in-AWS-CloudFront-Distribution]]
