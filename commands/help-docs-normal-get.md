---
id: cmd-help-normal
data: >-
  curl -X GET
  "https://search.usa.gov/help_docs?url=https%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html"
  -H "Host: search.usa.gov" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64;
  x64; rv:65.0) Gecko/20100101 Firefox/65.0" -H "Accept: application/json,
  text/javascript, */*; q=0.01" -H "Accept-Language: ja,en-US;q=0.7,en;q=0.3" -H
  "Accept-Encoding: gzip, deflate, br" -H "Referer:
  https://search.usa.gov/account" -H "X-NewRelic-ID: VgYAV1BRCxABU1JUBAUCXlI="
  -H "X-CSRF-Token:
  /2jDOc6aYEZA5VealIrF44qJZtY0iDiTsALu8HYA+OOIewuKHREwyh6M0wGa2WC9amTPX4vPMjj0YQIjys3nNA=="
  -H "X-Requested-With: XMLHttpRequest" -H "Connection: close" -H "Cookie:
  _ga=GA1.2.924676610.1553290937; _gid=GA1.2.1047460386.1553290937;
  _ga=GA1.3.924676610.1553290937; _gid=GA1.3.1047460386.1553290937;
  _session_id=a0d5ecbfa9404ea9ffad4cb3ea771dea;
  user_credentials=1055608db95b714d9ae2ef05a4e1b83aa138ad5fca67422f02ca795ec2a74179bb15c610dd33f5e6f200be0de0e812a8fe3d59a0027b290b5377ab2a65da1f19%3A%3A5992"
tags:
  - web
  - recon
type: command
output: >-
  HTTP/1.1 200 OK with body containing content from
  https://search.gov/manual/account.html
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.659Z'
verified: false
validated: true
submitted: true
---
# help-docs-normal-get

## Command

```bash
curl -X GET "https://search.usa.gov/help_docs?url=https%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: ja,en-US;q=0.7,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br" -H "Referer: https://search.usa.gov/account" -H "X-NewRelic-ID: VgYAV1BRCxABU1JUBAUCXlI=" -H "X-CSRF-Token: /2jDOc6aYEZA5VealIrF44qJZtY0iDiTsALu8HYA+OOIewuKHREwyh6M0wGa2WC9amTPX4vPMjj0YQIjys3nNA==" -H "X-Requested-With: XMLHttpRequest" -H "Connection: close" -H "Cookie: _ga=GA1.2.924676610.1553290937; _gid=GA1.2.1047460386.1553290937; _ga=GA1.3.924676610.1553290937; _gid=GA1.3.1047460386.1553290937; _session_id=a0d5ecbfa9404ea9ffad4cb3ea771dea; user_credentials=1055608db95b714d9ae2ef05a4e1b83aa138ad5fca67422f02ca795ec2a74179bb15c610dd33f5e6f200be0de0e812a8fe3d59a0027b290b5377ab2a65da1f19%3A%3A5992"
```

## Description

Sends an authenticated GET request to the /help_docs endpoint with a legitimate URL parameter to test normal functionality and retrieve baseline response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `url=...` | Encoded legitimate URL | Yes |
| `-H "Cookie: ..."` | Session cookies for authentication | Yes |
| Other `-H` | Standard headers for mimicking browser | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://search.usa.gov/help_docs?url=https%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" [headers]
```

### Advanced Usage

Add `--verbose` for detailed output:

```bash
curl -v -X GET "https://search.usa.gov/help_docs?url=https%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" [headers]
```

## Expected Output

HTTP/1.1 200 OK response with JSON body containing the fetched manual content, response time under 1s.

## Related

- [[commands/ssrf-localhost-21-test]]
- [[procedures/Send-Normal-Help-Docs-Request]]
