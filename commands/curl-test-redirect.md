---
id: cmd-curl-test-redirect
data: 'curl -v "https://shop.starbucks.de/?param=>cofee" 2>&1 | grep Location'
tags:
  - web-testing
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.388Z'
verified: false
validated: true
submitted: true
---
# curl-test-redirect

## Command

```bash
curl -v "https://shop.starbucks.de/?param=>cofee" 2>&1 | grep Location
```

## Description

Sends a GET request with a malformed parameter to test for open redirect behavior, extracting the redirect Location from verbose output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show headers | Yes |
| URL | Target URL with malformed param | Yes |
| `2>&1 | grep Location` | Pipe to filter redirect header | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://example.com/?test=>malformed" 2>&1 | grep Location
```

### Advanced Usage

```bash
curl -v -L "https://target/?param=>cofee" 2>&1 | grep -E 'Location|HTTP'
```

## Expected Output

Lines like: `< Location: https://unexpected-redirect.com`

## Related

- [[Related Procedure]]
