---
data: >-
  this._messageHandler=function(event){if(event.data){if(event.data.type &&
  event.data.digitalWalletsDialog){c(i, event.data.type, event.data.payload);}}}
  this._localWindow.addEventListener("message",this._messageHandler)
tags:
  - postmessage
  - listener
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.413Z'
id: 3c9f4c38-2462-4b07-8848-5b1ef9e38ff3
verified: false
validated: true
submitted: true
---
# initialize-postmessage-handler

## Command

```javascript
this._messageHandler=function(event){if(event.data){if(event.data.type && event.data.digitalWalletsDialog){c(i, event.data.type, event.data.payload);}}} this._localWindow.addEventListener("message",this._messageHandler)
```

## Description

Initializes a postMessage event listener that processes events without origin validation, calling handler c on matching data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| event | Message event object | Yes |
| data.type | Type string (e.g., DigitalWalletsDialog:change) | Yes |
| data.digitalWalletsDialog | Boolean flag | Yes |
| data.payload | Payload object | Yes |

## Examples

### Basic Usage

```javascript
this._messageHandler=function(event){if(event.data){if(event.data.type && event.data.digitalWalletsDialog){c(i, event.data.type, event.data.payload);}}} this._localWindow.addEventListener("message",this._messageHandler)
```

### Advanced Usage

Integrate into page load script for automatic setup.

## Expected Output

Sets up listener; no visible output, but events trigger c function.

## Related

- [[Related Procedure: Analyze-Shopify-Digital-Wallets-JavaScript]]
