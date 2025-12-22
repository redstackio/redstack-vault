---
id: cmd-uuid-2
data: >-
  let win = window.open('https://revealjs.com', '_blank'); setTimeout(() =>
  console.log('Window ready'), 2000);
tags:
  - setup
  - window
type: command
output: New window opened with reveal.js
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.184Z'
verified: false
validated: true
submitted: true
---
# open-revealjs-window

## Command

```javascript
let win = window.open('https://revealjs.com', '_blank'); setTimeout(() => console.log('Window ready'), 2000);
```

## Description

Opens a new browser window with the vulnerable reveal.js page, using a timeout to signal readiness.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Target URL | Yes |
| target | Open mode (_blank) | Yes |

## Examples

### Basic Usage

```javascript
window.open('https://revealjs.com', '_blank');
```

### Advanced Usage

```javascript
// With timeout log as above
```

## Expected Output

New tab/window opens; console logs 'Window ready' after 2 seconds.

## Related

- [[Related Procedure|procedures/Load-Vulnerable-reveal.js-Page]]
