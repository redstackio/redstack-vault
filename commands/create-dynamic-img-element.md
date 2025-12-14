---
data: >-
  var demo=document.createElement("img");
  demo.src="https://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg";
  document.body.innerHTML=""; demo.width="1000"; demo.height="1000";
  document.body.appendChild(demo);
tags:
  - csp-bypass
  - image-injection
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:17.950Z'
id: f19bfa62-eb88-43c7-89c5-dad04e895f15
verified: false
validated: true
submitted: true
---
# create-dynamic-img-element

## Command

```javascript
var demo=document.createElement("img"); demo.src="https://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg"; document.body.innerHTML=""; demo.width="1000"; demo.height="1000"; document.body.appendChild(demo);
```

## Description

This JavaScript command, executed in the browser console, dynamically creates an img element, sets its source to an external URL, clears the document body for visibility, configures dimensions, and appends it to the body, bypassing CSP restrictions on static img tags.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | External image URL (e.g., https://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg) | Yes |
| innerHTML | Value to set body.innerHTML ("" clears content) | Yes |
| width/height | Pixel dimensions for the image (1000) | Yes |

## Examples

### Basic Usage

```javascript
var demo=document.createElement("img"); demo.src="https://example.com/image.jpg"; document.body.appendChild(demo);
```

### Advanced Usage

```javascript
var demo=document.createElement("img"); demo.src="https://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg"; document.body.innerHTML=""; demo.width="1000"; demo.height="1000"; document.body.appendChild(demo);
```

## Expected Output

The external image loads and displays on the page at the specified size, with no CSP blocking errors in the console.

## Related

- [[Related Procedure|procedures/Inject-Dynamic-Image-for-CSP-Bypass]]
