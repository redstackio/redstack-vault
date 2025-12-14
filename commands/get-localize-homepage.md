---
id: cmd-get-localize-homepage
data: 'curl -X GET http://www.localize.io/'
tags:
  - recon
  - web
type: command
output: |-
  HTTP/1.1 200 OK
  ... (HTML content of homepage with sign-in form)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.954Z'
verified: false
validated: true
submitted: true
---
# get-localize-homepage

## Command

```bash
curl -X GET http://www.localize.io/
```

## Description

Sends a GET request to the homepage of localize.io to load the site and confirm the presence of the sign-in form. This is the initial step in reproducing the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `http://www.localize.io/` | Target URL for the homepage | Yes |

## Examples

### Basic Usage

```bash
curl -X GET http://www.localize.io/
```

### Advanced Usage

```bash
curl -X GET http://www.localize.io/ -v
```

> Adds verbose output to see full HTTP headers.

## Expected Output

HTTP 200 response with HTML body containing the site's homepage, including elements like the sign-in form. No errors should occur if the site is accessible.

## Related

- [[Related Procedure|procedures/Trigger-PHP-Trim-Error-for-Path-Disclosure]]
