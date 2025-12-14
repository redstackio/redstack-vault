---
id: cmd-uuid-2
data: 'curl https://s3.amazonaws.com/affirm-prod-www-cms█████████/index.html'
tags:
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.713Z'
verified: false
validated: true
submitted: true
---
# curl-verify-s3-content

## Command

```bash
curl https://s3.amazonaws.com/affirm-prod-www-cms█████████/index.html
```

## Description

Retrieves the index.html file from the claimed S3 bucket to verify takeover and content serving.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | S3 object URL | Yes |

## Examples

### Basic Usage

```bash
curl https://s3.amazonaws.com/affirm-prod-www-cms█████████/index.html
```

### Advanced Usage

```bash
curl -v https://s3.amazonaws.com/affirm-prod-www-cms█████████/index.html
```

## Expected Output

HTML content: <!-- taken over by hackerone.com/ian bugcrowd.com/iangcarroll ian@lhost.sh -->

## Related

- [[Related Procedure|procedures/Verify-Subdomain-Takeover]]
