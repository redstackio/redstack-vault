---
id: uuid-placeholder-c1
data: 'curl -v "https://target.com/nonexistent-page" -H "User-Agent: Mozilla/5.0"'
tags:
  - http
  - recon
type: command
output: |-
  HTTP/1.1 404 Not Found
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.223Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-404

## Command

```bash
curl -v "https://target.com/nonexistent-page" -H "User-Agent: Mozilla/5.0"
```

## Description

Triggers a 404 error on the target DNN site to invoke deserialization handling. Use for initial vulnerability probing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| URL | Target non-existent path | Yes |
| `-H` | Custom header | No |

## Examples

### Basic Usage

```bash
curl -v "https://target.com/test"
```

### Advanced Usage

```bash
curl -v --max-time 10 "https://target.com/nonexistent" -H "User-Agent: Test"
```

## Expected Output

Verbose HTTP exchange ending in 404 status, with no server errors.

## Related

- [[Related Procedure: Trigger-DNN-Deserialization-on-404-Page]]
