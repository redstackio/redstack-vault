---
data: >-
  aws cloudfront create-distribution --distribution-config
  file://dist-config.json
tags:
  - aws
  - cloudfront
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: e2026901-ce94-4e0d-a2b8-ae004a70f8c7
created_at: '2025-12-14T04:38:49.835Z'
updated_at: '2025-12-14T04:38:49.835Z'
verified: false
validated: true
submitted: true
---
# aws-cloudfront-create-distribution

## Command

```bash
aws cloudfront create-distribution --distribution-config file://dist-config.json
```

## Description

Creates a new CloudFront distribution with specified config, including aliases for subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file://dist-config.json | Path to JSON config file with origins and aliases | Yes |

## Examples

### Basic Usage

```bash
aws cloudfront create-distribution --distribution-config '{"Aliases":{"Items":["cdn.grab.com"]}}'
```

### Advanced Usage

```bash
aws cloudfront create-distribution --distribution-config file://full-config.json
```

## Expected Output

{"Distribution":{"Id":"E123ABC","Status":"InProgress"}}

## Related

- [[Related Procedure]]
