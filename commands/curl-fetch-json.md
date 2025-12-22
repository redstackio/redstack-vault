---
id: cmd-curl-fetch-001
data: 'curl "https://target-site.com/?format=json" -o output.json'
tags:
  - recon
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.025Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-json

## Command

```bash
curl "https://target-site.com/?format=json" -o output.json
```

## Description

This command uses curl to send an HTTP GET request to a target URL with a JSON format parameter, downloading the response to a file for analysis in reconnaissance scenarios like information disclosure testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"https://target-site.com/?format=json"` | The full URL including the format parameter to trigger JSON output | Yes |
| `-o output.json` | Saves the response to a specified file | No (but recommended for capture) |

## Examples

### Basic Usage

```bash
curl "https://uber-movement.squarespace.com/?format=json"
```

### Advanced Usage

```bash
curl -s "https://uber-movement.squarespace.com/?format=json" -o disclosed_data.json -H "User-Agent: Mozilla/5.0"
```

> The `-s` flag silences progress output, and `-H` adds a user-agent header to mimic browser requests.

## Expected Output

A JSON-formatted response body containing site data, saved to the output file if specified. Errors may indicate blocked requests or invalid endpoints.

## Related

- [[Related Procedure: Exploit-Squarespace-JSON-Information-Disclosure]]
