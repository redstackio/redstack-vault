---
data: >-
  while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" -qO- |
  grep "cyberjutsu.io"; echo "ping my payload..." ;done
tags:
  - web-cache-poisoning
  - verification
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 3c860976-27f2-4e91-87b1-1b7239394c7b
created_at: '2025-12-13T09:00:34.103Z'
updated_at: '2025-12-13T09:00:34.103Z'
verified: false
validated: true
submitted: true
---
# wget-cache-verification-loop

## Command

```bash
while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" -qO- | grep "cyberjutsu.io"; echo "ping my payload..." ;done
```

## Description

Repeatedly sends HTTP GET requests to the target URL and checks the response for the injected domain to confirm cache poisoning, looping indefinitely.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `while true; do ... done` | Loops indefinitely to continuously check | Yes |
| `-qO-` | Quiet mode, outputs response to stdout | Yes |
| `| grep "cyberjutsu.io"` | Searches the response for the string 'cyberjutsu.io' to verify poisoning | Yes |

## Examples

### Basic Usage

```bash
while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" -qO- | grep "cyberjutsu.io"; echo "ping my payload..." ;done
```

### Advanced Usage

```bash
while true; do wget "https://target.com/path" -qO- | grep "evil.com"; echo "checking..." ; sleep 1; done
```

## Expected Output

If poisoned, outputs lines containing 'cyberjutsu.io'; echoes 'ping my payload...' for status.

## Related

- [[procedures/Verify-Cache-Poisoning-Success]]
- [[tools/wget]]
- [[tools/grep]]
