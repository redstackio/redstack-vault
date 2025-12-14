---
id: cmd-uuid-002
data: >-
  curl -v -b cookies.txt
  'http://target/cp/admin_system/general_configuration&S=98be920eacf52890b4b159431a7da8cf'
tags:
  - xss
  - trigger
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:27.062Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-xss

## Command

```bash
curl -v -b cookies.txt 'http://target/cp/admin_system/general_configuration&S=98be920eacf52890b4b159431a7da8cf'
```

## Description

This command fetches an admin page to trigger the execution of a stored XSS payload, using verbose mode to inspect the response for injected script tags.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for headers and response | Yes |
| `-b cookies.txt` | Session cookies | Yes |
| URL | Admin page URL with session hash | Yes |

## Examples

### Basic Usage

```bash
curl -v -b cookies.txt 'http://target/admin/page'
```

### Advanced Usage

Pipe to grep for script tags:

```bash
curl -v -b cookies.txt 'http://target/admin/page' | grep -i script
```

## Expected Output

Full HTTP response including HTML body with injected <script>alert('stored xss')</script>. Look for the payload in the output.

## Related

- [[Related Procedure: Inject-Stored-XSS-Payload-into-ExpressionEngine-General-Configuration]]
