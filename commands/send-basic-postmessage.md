---
data: >-
  window.postMessage({type:"DigitalWalletsDialog:change",digitalWalletsDialog:true,payload:{title:"placeholder",button:"placeholder"}},"*");
tags:
  - postmessage
  - test
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.403Z'
id: 2ed0fe7f-9617-4fdb-b297-d6730f70751b
verified: false
validated: true
submitted: true
---
# send-basic-postmessage

## Command

```javascript
window.postMessage({type:"DigitalWalletsDialog:change",digitalWalletsDialog:true,payload:{title:"placeholder",button:"placeholder"}},"*");
```

## Description

Sends a basic postMessage to test dialog change with title and button.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| type | "DigitalWalletsDialog:change" | Yes |
| digitalWalletsDialog | true | Yes |
| payload.title | Dialog title | Yes |
| payload.button | Button text | Yes |
| targetOrigin | "*" for any | Yes |

## Examples

### Basic Usage

```javascript
window.postMessage({type:"DigitalWalletsDialog:change",digitalWalletsDialog:true,payload:{title:"placeholder",button:"placeholder"}},"*");
```

## Expected Output

Dialog updates with placeholders.

## Related

- [[Related Procedure: Test-Legitimate-PostMessage-Payloads]]
