---
data: 'top.postMessage(e.data,''*'');'
tags:
  - postmessage
type: command
executor: javascript
platforms:
  - Web
id: ee78dee3-3ab0-4bd8-9174-1dbf59d00c4a
created_at: '2025-12-11T06:10:22.319Z'
updated_at: '2025-12-11T06:10:22.319Z'
verified: false
validated: true
submitted: true
---
# top-postmessage-relay

## Command

```javascript
top.postMessage(e.data,'*');
```

## Description

Sends a message to the top window to relay data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```javascript
top.postMessage({key: 'value'},'*');
```

## Expected Output

Message received by top window.

## Related

- [[procedures/Exploit-XSS-to-Steal-OAuth-Tokens]]
