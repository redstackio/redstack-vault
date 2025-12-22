---
id: cmd-curl-xss-test
data: 'curl -i "https://█████████/test-path"'
tags:
  - web
  - testing
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.387Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss-reflection

## Command

```bash
curl -i "https://█████████/test-path"
```

## Description

This command uses curl to send a GET request to a non-existent path on the target website and displays the full HTTP response, including headers and body, to verify if the path is reflected unsanitized in the 404 error page. It is useful for initial reconnaissance of reflection vulnerabilities before crafting XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `"https://█████████/test-path"` | The target URL with a test path to check for reflection | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://█████████/test-path"
```

### Advanced Usage

```bash
curl -i -s "https://█████████/<svg onload=alert('XSS')>" | grep -i "svg"
```

This pipes the output to grep to search for the injected payload, confirming reflection.

## Expected Output

A 404 Not Found response with headers like `HTTP/1.1 404 Not Found` followed by the HTML body containing the echoed path, e.g., `<p>The requested path /test-path was not found</p>`. If unsanitized, malicious tags like `<svg>` will appear raw in the body.

## Related

- [[Related Procedure|procedures/Exploit-Reflected-XSS-in-404-Error-Page]]
