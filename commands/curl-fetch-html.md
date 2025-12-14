---
id: cmd-curl-fetch-001
data: |-
  curl -s http://people.uber.com/ > source.html
  cat source.html | grep -i 'yoast\\|wpseo'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.253Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-html

## Command

```bash
curl -s http://people.uber.com/ > source.html
cat source.html | grep -i 'yoast\\|wpseo'
```

## Description

This command fetches the HTML source of a target website silently using curl and saves it to a file, then searches for specific plugin-related strings like Yoast indicators. Use it during web reconnaissance to identify WordPress plugins without interactive browsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `http://people.uber.com/` | Target URL to fetch | Yes |
| `> source.html` | Redirect output to file | Yes |
| `grep -i 'yoast\\|wpseo'` | Case-insensitive search for plugin keywords | Yes |

## Examples

### Basic Usage

```bash
curl -s http://example.com/ | grep -i plugin
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" http://people.uber.com/ > source.html && grep -E 'yoast|wpseo|version' source.html
```

## Expected Output

Lines from the HTML containing matches, e.g., "<!-- Yoast WordPress SEO plugin v2.1.1 -->", indicating plugin presence and version.

## Related

- [[Related Procedure|procedures/Inspect-Website-Source-Code-for-Plugins]]
