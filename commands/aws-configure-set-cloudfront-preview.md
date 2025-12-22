---
id: 5c30e18b-9756-401b-9cc8-b755323946d9
type: command
executor: bash
data: |
  aws configure set preview.cloudfront true
output: null
created_at: '2020-07-31T04:25:16.114313+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - cloudfront
  - configuration
verified: true
validated: true
---

# aws-configure-set-cloudfront-preview

## Command

```bash
aws configure set preview.cloudfront true
```

## Description

This command configures the AWS CLI to enable preview (beta) features for the CloudFront service, allowing access to experimental options or enhanced output in subsequent CloudFront commands. It modifies the local AWS configuration file without affecting the AWS account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `preview.cloudfront` | Sets the preview flag for CloudFront to true (enables beta features) | Yes |
| `true` | Boolean value to activate previews | Yes |

## Examples

### Basic Usage

```bash
aws configure set preview.cloudfront true
```

### Verify Configuration

```bash
aws configure get preview.cloudfront
```

## Expected Output

No direct output on success; the configuration is silently updated. Verification command outputs: `true` if enabled.

## Related

- [[procedures/List-AWS-CloudFront-Distributions]] (procedure that uses this command)
- [[tools/AWS-CLI]]
