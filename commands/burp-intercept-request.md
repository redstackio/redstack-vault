---
id: cmd-burp-intercept-001
data: >-
  # Burp Suite GUI action: Enable proxy intercept and modify request parameter
  with SQL payload
tags:
  - proxy
  - intercept
  - sqli
type: command
output: null
executor: gui
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.095Z'
verified: false
validated: true
submitted: true
---
# burp-intercept-request

## Command

```bash
# GUI: Burp Suite > Proxy > Intercept: Turn On, submit request, edit param to include payload like ' OR 1=1 --, then Forward
```

## Description

Intercepts HTTP requests in Burp Suite to manually test for SQL injection by injecting payloads and observing server responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Intercept Toggle | Enable/disable request interception | Yes |
| Payload | SQL fragment to inject (e.g., ' OR 1=1 --) | Yes |
| Forward | Release the intercepted request | Yes |

## Examples

### Basic Usage

```bash
# Turn on intercept, inject payload, forward request
```

### Advanced Usage

```bash
# Use Repeater tab for repeated testing: Send to Repeater, modify, send
```

## Expected Output

Server response changes, such as error pages for invalid SQL or altered content for successful injection.

## Related

- [[Related Procedure: Identify-SQL-Injection-Endpoint]]
