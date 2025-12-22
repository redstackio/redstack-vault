---
type: command
executor: javascript
data: element.innerHTML
tags:
  - dom-manipulation
  - xss
platforms:
  - Web
verified: true
validated: true
---

# get-element-innerHTML

## Command

```javascript
element.innerHTML
```

## Description

This JavaScript command accesses the innerHTML property of a DOM element, retrieving or setting its HTML content. Use it in browser console or scripts to inspect or inject HTML during XSS testing, enabling tag recreation to bypass sanitizers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `element` | The DOM element reference (e.g., document.getElementById('id')) | Yes |
| `.innerHTML` | Property to get/set the HTML content inside the element | Built-in |

## Examples

### Basic Usage

```javascript
var el = document.getElementById('target');
console.log(el.innerHTML);
```

### Advanced Usage

```javascript
var el = document.getElementById('target');
el.innerHTML = '<script>alert(1)</script>';
```

## Expected Output

The command returns a string containing the HTML markup inside the element, e.g., "<p>Existing content</p>". When setting, it updates the DOM and may trigger parsing/execution if scripts are involved.

## Related

- [[procedures/Mutated-XSS-with-HTML-Tag-Recreation-and-DOMPurify-Bypass]]
