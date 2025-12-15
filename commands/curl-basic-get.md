---
id: cmd-curl-basic-get
data: 'curl "https://target.com/search?q=$1" -v'
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.612Z'
verified: false
validated: true
submitted: true
---
# curl-basic-get

## Command

```bash
curl "https://target.com/search?q=$1" -v
```

## Description

Sends a basic GET request to the search endpoint with a query parameter to observe normal behavior or fetch pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$1` | Search query value (e.g., 'test') | Yes |
| `-v` | Verbose output for headers | No |

## Examples

### Basic Usage

```bash
curl "https://target.com/search?q=test" -v
```

### Advanced Usage

```bash
curl "https://target.com/search?q=test" -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

HTTP response with status 200, HTML body containing search results, and verbose headers showing request details.

## Related

- [[Related Procedure]]
