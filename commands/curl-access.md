---
data: 'curl -k http://datacafe-cert.starbucks.com/'
tags:
  - http
  - access
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:01.960Z'
id: cc2821fb-e371-499c-acc4-43ce1d4c10cb
verified: false
validated: true
submitted: true
---
# curl-access

## Command

```bash
curl -k http://datacafe-cert.starbucks.com/
```

## Description

Fetches content from the subdomain to verify takeover, ignoring SSL for HTTPS tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure SSL | No |
| `URL` | Subdomain endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://sub.target.com/
```

### Advanced Usage

```bash
curl -k -L https://sub.target.com/ > content.html
```

## Expected Output

Custom content from the claimed service.

## Related

- [[commands/curl-verify]]
