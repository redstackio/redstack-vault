---
data: 'curl -H "X-Forwarded-Host: test.example.com" https://okmedia.insideok.ru/'
tags:
  - header-manipulation
  - testing
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: cabb5a02-76e6-4093-acad-e98360f870e7
created_at: '2025-12-13T09:00:33.952Z'
updated_at: '2025-12-13T09:00:33.952Z'
verified: false
validated: true
submitted: true
---
# curl-set-x-forwarded-host

## Command

```bash
curl -H "X-Forwarded-Host: test.example.com" https://okmedia.insideok.ru/
```

## Description

This command uses curl to send an HTTP request with a custom X-Forwarded-Host header for testing web cache poisoning vulnerabilities by checking if the host is reflected without validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-Forwarded-Host: value"` | Sets the custom host header | Yes |
| `https://okmedia.insideok.ru/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Forwarded-Host: test.example.com" https://okmedia.insideok.ru/
```

### Advanced Usage

```bash
curl -H "X-Forwarded-Host: test.example.com" -v https://okmedia.insideok.ru/
```

## Expected Output

HTTP response potentially including the injected host value in links or content, indicating vulnerability.

## Related

- [[commands/curl-inject-xss-payload]]
- [[procedures/Test-for-Web-Cache-Poisoning-via-Header-Manipulation]]
