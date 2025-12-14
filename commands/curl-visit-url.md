---
data: curl -L "URL" -o output.html
tags:
  - web-testing
  - oauth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.487Z'
id: 68c90cb9-85cb-47bb-9568-ab5a6d9001f2
verified: false
validated: true
submitted: true
---
# curl-visit-url

## Command

```bash
curl -L "https://example.com/endpoint?param=value" -o output.html
```

## Description

This command uses curl to visit a web URL, following redirects (-L) and saving the output to a file for analysis, commonly used to test OAuth endpoints and observe redirection behavior without a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow HTTP redirects | Yes |
| URL | Target endpoint URL with parameters | Yes |
| `-o output.html` | Save response to file | No |

## Examples

### Basic Usage

```bash
curl -L "https://prans.myshopify.com/admin/oauth/authorize?client_id=616ce3efcd495007438000ad958a6629&scope=a&redirect_uri=https://www.facebook.com/abc" -o redirect_output.html
```

### Advanced Usage

```bash
curl -L -v "https://prans.myshopify.com/admin/oauth/authorize?client_id=616ce3efcd495007438000ad958a6629&scope=read_customers&redirect_uri=http://www.facebook.com/abc/" -o valid_output.html
```

## Expected Output

HTTP response body saved to output.html, including final redirected page content or error messages; verbose mode (-v) shows headers like Location for redirects.

## Related

- [[Related Procedure]]
