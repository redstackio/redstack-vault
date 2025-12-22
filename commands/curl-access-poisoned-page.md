---
data: 'curl https://okmedia.insideok.ru/'
tags:
  - verification
  - xss
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: b1f5ca99-a594-4ad9-82c6-d4cc37141fd2
created_at: '2025-12-13T09:00:33.940Z'
updated_at: '2025-12-13T09:00:33.940Z'
verified: false
validated: true
submitted: true
---
# curl-access-poisoned-page

## Command

```bash
curl https://okmedia.insideok.ru/
```

## Description

This command accesses a potentially poisoned web page to verify if the cached response includes the injected XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://okmedia.insideok.ru/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl https://okmedia.insideok.ru/
```

### Advanced Usage

```bash
curl -v https://okmedia.insideok.ru/ | grep "<script>"
```

## Expected Output

HTTP response containing the injected XSS script if the cache is poisoned.

## Related

- [[commands/curl-inject-xss-payload]]
- [[procedures/Verify-Stored-XSS-in-Poisoned-Cache]]
