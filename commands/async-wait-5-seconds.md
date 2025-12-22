---
id: cmd-async-wait-900619
data: 'await new Promise((resolve)=>setTimeout(resolve,5000));'
tags:
  - delay
  - async
type: command
output: 'Resolves after delay, allowing the window to load'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:37.697Z'
verified: false
validated: true
submitted: true
---
# async-wait-5-seconds

## Command

```javascript
await new Promise((resolve)=>setTimeout(resolve,5000));
```

## Description

Asynchronously waits 5 seconds using a Promise and setTimeout to ensure the target window loads before proceeding with postMessage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| delay | Milliseconds to wait (5000) | Yes |

## Examples

### Basic Usage

```javascript
await new Promise((resolve)=>setTimeout(resolve,5000));
```

### Advanced Usage

```javascript
await new Promise((resolve)=>setTimeout(resolve,10000)); // 10 seconds
```

## Expected Output

Promise resolves silently after the delay.

## Related

- [[Related Procedure]]
