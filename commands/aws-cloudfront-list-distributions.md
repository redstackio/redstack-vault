---
data: >-
  aws cloudfront list-distributions --query
  'DistributionList.Items[?contains(Aliases.Items, `$1`)].Id' --output text
tags:
  - aws
  - cloudfront
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: f5a092dd-4709-4128-9f3d-383f05c7e378
created_at: '2025-12-14T04:38:49.841Z'
updated_at: '2025-12-14T04:38:49.841Z'
verified: false
validated: true
submitted: true
---
# aws-cloudfront-list-distributions

## Command

```bash
aws cloudfront list-distributions --query 'DistributionList.Items[?contains(Aliases.Items, `$1`)].Id' --output text
```

## Description

Lists AWS CloudFront distributions and filters for those associated with a specific alias (CNAME), helping verify ownership.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $1 | Alias/CNAME (e.g., cdn.grab.com) | Yes |

## Examples

### Basic Usage

```bash
aws cloudfront list-distributions --query 'DistributionList.Items[?contains(Aliases.Items, `cdn.grab.com`)].Id'
```

### Advanced Usage

```bash
aws cloudfront list-distributions --max-items 10
```

## Expected Output

Empty or distribution ID if associated.

## Related

- [[Related Procedure]]
