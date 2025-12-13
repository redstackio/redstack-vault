---
data: 'xhr.send(new Blob([aBody]));'
tags:
  - javascript
  - xhr
type: command
executor: javascript
platforms:
  - Web
id: fa143fbd-4780-4806-a9f3-f764a20dce1b
created_at: '2025-12-13T09:00:34.439Z'
updated_at: '2025-12-13T09:00:34.439Z'
verified: false
validated: true
submitted: true
---
# XHR Send Blob

## Command

```javascript
xhr.send(new Blob([aBody]));
```

## Description

Sends the XMLHttpRequest with the body.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `data` | Blob of request body | Yes |

## Examples

### Basic Usage

```javascript
xhr.send(new Blob([body]));
```

## Expected Output

Triggers email change if successful

## Related

- [[procedures/Change-Victim-Email-Using-Extracted-CSRF]]
