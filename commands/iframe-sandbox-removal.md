---
id: cmd-iframe-sandbox-remove
data: >-
  setTimeout(function(){ifr =
  document.querySelector('iframe');ifr.style="";ifr.removeAttribute("sandbox");console.log(ifr);},4000)
tags:
  - iframe
  - manipulation
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.834Z'
verified: false
validated: true
submitted: true
---
# iframe-sandbox-removal

## Command

```javascript
setTimeout(function(){ifr = document.querySelector('iframe');ifr.style="";ifr.removeAttribute("sandbox");console.log(ifr);},4000)
```

## Description

After 4 seconds, selects the iframe, removes sandbox attribute, and clears style for manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| timeout | 4000ms delay | Yes |
| selector | 'iframe' query | Yes |

## Examples

### Basic Usage

```javascript
setTimeout(function(){ifr = document.querySelector('iframe');ifr.style="";ifr.removeAttribute("sandbox");console.log(ifr);},4000)
```

## Expected Output

Iframe without sandbox, logged to console.

## Related

- [[procedures/Setup-ClickJacking-Iframe-for-Imgur-Embed]]
