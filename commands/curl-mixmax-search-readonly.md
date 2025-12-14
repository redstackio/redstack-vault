---
id: cmd-002
data: >-
  curl "https://app.mixmax.com/dashboard/sequences?q=a+readonly" -H "Cookie:
  your-session-cookie"
tags:
  - web-test
  - attribute-injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.442Z'
verified: false
validated: true
submitted: true
---
# curl-mixmax-search-readonly

## Command

```bash
curl "https://app.mixmax.com/dashboard/sequences?q=a+readonly" -H "Cookie: your-session-cookie"
```

## Description

Sends a request to the Mixmax search endpoint with an attribute injection payload to test for 'readonly' interpretation, useful for validating HTML parsing vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `q=a+readonly` | URL-encoded payload for attribute test | Yes |
| `-H "Cookie: ..."` | Session cookie for authentication | Yes |

## Examples

### Basic Usage

```bash
curl "https://app.mixmax.com/dashboard/sequences?q=a+readonly" -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -v "https://app.mixmax.com/dashboard/sequences?q=a+readonly" -H "Cookie: session=abc123" | grep -i readonly
```

## Expected Output

HTML response showing the input field with 'readonly' attribute applied, e.g., <input value="a" readonly>, preventing edits in the browser.

## Related

- [[Related Procedure: Test-Attribute-Injection-with-Readonly]]
