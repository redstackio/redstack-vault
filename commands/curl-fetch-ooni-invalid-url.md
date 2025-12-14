---
data: 'curl https://explorer.ooni.torproject.org//x'
tags:
  - reconnaissance
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e3fca511-fa01-4a78-952f-ecc13335b89d
created_at: '2025-12-14T17:26:12.115Z'
updated_at: '2025-12-14T17:26:12.115Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-ooni-invalid-url

## Command

```bash
curl https://explorer.ooni.torproject.org//x
```

## Description

This command uses curl to send a GET request to an invalid URL path on the OONI Explorer web application, triggering a 404 error that discloses the full server file path. It is used for initial reconnaissance to uncover internal system details via information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://explorer.ooni.torproject.org//x` | The target invalid URL (base domain + duplicated slash + arbitrary endpoint) | Yes |

## Examples

### Basic Usage

```bash
curl https://explorer.ooni.torproject.org//x
```

### Advanced Usage

```bash
curl -v https://explorer.ooni.torproject.org//x | grep -i "path"
```

This verbose version shows headers and filters for path-related output.

## Expected Output

A 404 Not Found response with an error message in the body, such as:

```
<html>
<head><title>404 Not Found</title></head>
<body>
<h1>Not Found</h1>
<p>The requested URL /x was not found on this server: /full/server/path/to/webroot//x</p>
</body>
</html>
```

Look for absolute paths like "/usr/local/..." indicating the server's filesystem structure.

## Related

- [[Related Procedure|procedures/Trigger-Full-Path-Disclosure-via-Invalid-URL]]
