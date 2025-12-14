---
id: cmd-001
data: >-
  curl "https://app.mixmax.com/dashboard/sequences?q=a+POSSIBLEVECTOR" -H
  "Cookie: your-session-cookie"
tags:
  - web-test
  - xss-payload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.444Z'
verified: false
validated: true
submitted: true
---
# curl-mixmax-search-possiblevector

## Command

```bash
curl "https://app.mixmax.com/dashboard/sequences?q=a+POSSIBLEVECTOR" -H "Cookie: your-session-cookie"
```

## Description

This command accesses the Mixmax Sequences dashboard search endpoint with a truncation test payload, simulating the request to observe HTML parsing issues. Use it to fetch the response for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `q=a+POSSIBLEVECTOR` | URL-encoded search query payload | Yes |
| `-H "Cookie: ..."` | Authentication header with session cookie | Yes |

## Examples

### Basic Usage

```bash
curl "https://app.mixmax.com/dashboard/sequences?q=a+POSSIBLEVECTOR" -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -v "https://app.mixmax.com/dashboard/sequences?q=a+POSSIBLEVECTOR" -H "Cookie: session=abc123" -o response.html
```

## Expected Output

HTML response where the search input reflects only 'a', with truncation evident in the parsed structure. Look for unquoted value in <input value="a POSSIBLEVECTOR"> becoming <input value="a" POSSIBLEVECTOR>.

## Related

- [[Related Procedure: Test-Search-Truncation-with-POSSIBLEVECTOR]]
