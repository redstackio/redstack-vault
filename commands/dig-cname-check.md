---
data: dig CNAME storybook.lystit.com
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:01.903Z'
id: c0331ab2-272a-4538-b628-4829592c3d5f
verified: false
validated: true
submitted: true
---
# dig-cname-check

## Command

```bash
dig CNAME storybook.lystit.com
```

## Description

Queries DNS for the CNAME record of a subdomain to identify pointers to cloud resources like S3 buckets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `CNAME` | Specifies CNAME query type | Yes |
| `storybook.lystit.com` | Target subdomain | Yes |

## Examples

### Basic Usage

```bash
dig CNAME storybook.lystit.com
```

### Advanced Usage

```bash
dig +short CNAME storybook.lystit.com
```

## Expected Output

DNS response showing 'storybook.lystit.com.s3.amazonaws.com' or similar, indicating S3 pointer.

## Related

- [[Related Procedure: Discover Dangling CNAME Record]]
