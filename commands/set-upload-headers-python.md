---
data: >-
  headers = {'accept': '*/*', 'accept-language':
  'nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5', 'cache-control':
  'no-cache', 'content-type': m.content_type, 'origin': 'https://dust.tt',
  'pragma': 'no-cache', 'priority': 'u=1, i', 'referer':
  'https://dust.tt/w/<workspace_sid>/assistant/new', 'sec-ch-ua': '"Google
  Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"', 'sec-ch-ua-mobile':
  '?0', 'sec-ch-ua-platform': '"macOS"', 'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent':
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML,
  like Gecko) Chrome/135.0.0.0 Safari/537.36'}
tags:
  - headers
  - http
type: command
output: null
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.393Z'
id: 83990383-069f-48d2-bc1a-5890f166bafb
verified: false
validated: true
submitted: true
---
# set-upload-headers-python

## Command

```python
headers = {'accept': '*/*', 'accept-language': 'nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5', 'cache-control': 'no-cache', 'content-type': m.content_type, 'origin': 'https://dust.tt', 'pragma': 'no-cache', 'priority': 'u=1, i', 'referer': 'https://dust.tt/w/<workspace_sid>/assistant/new', 'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"macOS"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
```

## Description

Defines HTTP headers mimicking a browser request for the file upload to avoid detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Various | Standard browser headers including content-type from encoder | Yes |

## Examples

### Basic Usage

```python
headers = {...}  # Full dict as above
```

## Expected Output

No output; creates headers dict.

## Related

- [[commands/post-file-upload-python]]
