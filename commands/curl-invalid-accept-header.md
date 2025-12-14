---
data: 'curl -H "Accept: invalid/mime" -v http://www.rockstargames.com/index'
tags:
  - recon
  - web
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a06bf9f3-305c-4824-809d-bdc1d54506ae
created_at: '2025-12-14T17:26:22.749Z'
updated_at: '2025-12-14T17:26:22.749Z'
verified: false
validated: true
submitted: true
---
# curl-invalid-accept-header

## Command

```bash
curl -H "Accept: invalid/mime" -v http://www.rockstargames.com/index
```

## Description

This curl command sends an HTTP GET request to the target /index endpoint with a custom invalid Accept header to trigger an Apache server error that discloses the webroot path. Use it during web reconnaissance to identify information disclosure vulnerabilities in server configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Accept: invalid/mime"` | Sets a malformed MIME type in the Accept header to force content negotiation failure | Yes |
| `-v` | Enables verbose output to display full request/response headers and body | No (recommended for debugging) |
| `http://www.rockstargames.com/index` | Target URL endpoint | Yes (replace with actual target) |

## Examples

### Basic Usage

```bash
curl -H "Accept: invalid/mime" http://www.rockstargames.com/index
```

### Advanced Usage

```bash
curl -H "Accept: invalid/mime" -v -k https://target.com/index --output response.html
```

> Adds -k for HTTPS (ignore certs), saves output to file for analysis.

## Expected Output

A server error response (e.g., HTTP/1.1 406 Not Acceptable) with body text including the full path, such as: "AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error. Use 'LimitInternalRecursion' to increase the limit if necessary. Use 'LogLevel debug' to get a backtrace." followed by path details like "/usr/local/apache2/htdocs/index.html No such file or directory".

## Related

- [[Related Procedure|procedures/Trigger-Apache-Path-Disclosure-with-Invalid-Accept-Header]]
