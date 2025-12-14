---
id: cmd-window-enum-001
data: 'for (let prop in window) { console.log(prop); }'
tags:
  - recon
  - browser
type: command
output: List of global window properties including requestAnimationFrame
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:33.993Z'
verified: false
validated: true
submitted: true
---
# enumerate-window-globals

## Command

```javascript
for (let prop in window) { console.log(prop); }
```

## Description

This JavaScript command iterates over the properties of the global window object in a browser console, logging each to identify available functions, particularly those accepting callbacks for XSS abuse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; runs in console | Yes |

## Examples

### Basic Usage

```javascript
for (let prop in window) { console.log(prop); }
```

### Advanced Usage

```javascript
for (let prop in window) { if (typeof window[prop] === 'function') console.log(prop); }
```

## Expected Output

A list of all enumerable window properties, such as 'requestAnimationFrame', 'mozRequestAnimationFrame', etc., printed to the console.

## Related

- [[Related Procedure: Enumerate-Global-Window-Functions-for-Callback-Abuse]]
