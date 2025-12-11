---
data: 'parent.window.onmessage=function(e){...};'
tags:
  - postmessage
  - listener
type: command
executor: javascript
platforms:
  - Web
id: 770fa63b-6196-4ee8-9454-33dff7c8966b
created_at: '2025-12-11T06:10:22.315Z'
updated_at: '2025-12-11T06:10:22.315Z'
verified: false
validated: true
submitted: true
---
# parent-onmessage-listener

## Command

```javascript
parent.window.onmessage=function(e){...};
```

## Description

Sets up a message listener on the parent window.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```javascript
parent.window.onmessage=function(e){console.log(e.data);};
```

## Expected Output

Handles incoming messages.

## Related

- [[procedures/Exploit-XSS-to-Steal-OAuth-Tokens]]
