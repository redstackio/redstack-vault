---
id: cmd-uuid-2
data: >-
  curl -X GET
  "https://downloads.exodus.com/releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone"
  -v
tags:
  - cache-poisoning
  - verification
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.232Z'
verified: false
validated: true
submitted: true
---
# curl-verify-cache

## Command

```bash
curl -X GET "https://downloads.exodus.com/releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone" -v
```

## Description

This command sends a clean HTTP GET request to verify if the Cloudflare cache has been poisoned, expecting a cached 403 instead of the file content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| URL | Target path with cache-buster query param | Yes |
| `-v` | Verbose output for debugging | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://downloads.exodus.com/releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone" -v
```

### Advanced Usage

```bash
curl -X GET "https://target.com/path/to/file.txt?cachebuster=test" -v --max-time 10
```

## Expected Output

HTTP/1.1 403 Forbidden from cache, with CF-Cache-Status: HIT confirming poisoning.

## Related

- [[Related Procedure|procedures/Verify-Cache-Poisoning-Effect]]
