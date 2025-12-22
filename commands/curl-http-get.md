---
data: 'curl http://www.cyberlynx.lu/'
tags:
  - http
  - probe
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.215Z'
id: 28c2a70f-9112-4b12-b612-9c568c0deca1
verified: false
validated: true
submitted: true
---
# curl-http-get

## Command

```bash
curl http://www.cyberlynx.lu/
```

## Description

This command sends an HTTP GET request to retrieve the full response body from a target URL, allowing inspection of error pages or content to identify hosting platforms like unclaimed Wix sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | Target endpoint (e.g., http://www.cyberlynx.lu/) | Yes |

## Examples

### Basic Usage

```bash
curl http://www.cyberlynx.lu/
```

### Advanced Usage

```bash
curl -v http://www.cyberlynx.lu/  # Verbose output with headers
```

## Expected Output

<!DOCTYPE html>
<html>
<head>
<title>404 - Page Not Found</title>
</head>
<body>
<h1>This site’s been launched...</h1>
<!-- Wix unclaimed page content -->

HTML indicating availability for registration on Wix.

## Related

- [[commands/curl-http-head]]
- [[procedures/Detect-and-Confirm-Subdomain-Takeover-on-Wix]]
