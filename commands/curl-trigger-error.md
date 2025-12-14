---
id: 123e4567-e89b-12d3-a456-426614174002
name: curl-trigger-error
type: command
executor: bash
data: 'curl -v "https://api.wwm-dev.autodesk.com/invalid_endpoint"'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.139Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - reconnaissance
  - web-testing
verified: false
validated: true
submitted: true
---

# curl-trigger-error

## Command

```bash
curl -v "https://api.wwm-dev.autodesk.com/invalid_endpoint"
```

## Description

This command uses curl to send a GET request to an invalid endpoint on a Django-based web application, triggering a 500 error to check for debug mode exposure. The -v flag enables verbose output for inspecting headers and response body. Use it during reconnaissance to detect misconfigurations that leak sensitive information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show headers and details | Yes |
| URL | Target endpoint (e.g., /invalid_endpoint) | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://target.com/invalid_path"
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" -X GET "https://target.com/nonexistent" --max-time 10
```

## Expected Output

A verbose HTTP response with status 500, followed by HTML content if debug mode is on. Look for Django debug page elements: yellow error box, stack trace, settings info (e.g., "DEBUG: True"), and installed packages. Example snippet: "Template-loader postmortem... Django tried loading these templates..."

## Related

- [[Related Procedure|procedures/Discover-Django-Debug-Mode-Information-Disclosure]]
