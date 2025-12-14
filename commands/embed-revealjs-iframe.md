---
id: cmd-uuid-1
data: >-
  const iframe = document.createElement('iframe'); iframe.id = 'frame';
  iframe.src = 'https://revealjs.com'; iframe.onload = () => setTimeout(() =>
  console.log('Loaded'), 1000); document.body.appendChild(iframe);
tags:
  - setup
  - iframe
type: command
output: Iframe loaded with reveal.js
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.195Z'
verified: false
validated: true
submitted: true
---
# embed-revealjs-iframe

## Command

```javascript
const iframe = document.createElement('iframe'); iframe.id = 'frame'; iframe.src = 'https://revealjs.com'; iframe.onload = () => setTimeout(() => console.log('Loaded'), 1000); document.body.appendChild(iframe);
```

## Description

Creates and appends an iframe to load the vulnerable reveal.js page, with a delayed log to confirm readiness for postMessage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URL of reveal.js | Yes |
| id | Iframe identifier | Yes |
| onload | Callback for load confirmation | No |

## Examples

### Basic Usage

```javascript
const iframe = document.createElement('iframe'); iframe.src = 'https://revealjs.com'; document.body.appendChild(iframe);
```

### Advanced Usage

```javascript
// With ID and onload as above
```

## Expected Output

Console log 'Loaded' after 1 second; iframe displays reveal.js presentation.

## Related

- [[Related Procedure|procedures/Load-Vulnerable-reveal.js-Page]]
