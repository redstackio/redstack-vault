---
data: >-
  window.postMessage({ type: "DigitalWalletsDialog:change",
  digitalWalletsDialog: true, payload: { title: "placeholder", button:
  "placeholder", lineItems: [{name: "product",amount: "$13.37",message: "added
  to cart" }], },}, "*");
tags:
  - postmessage
  - lineitems
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.398Z'
id: 8a658851-66a3-4d42-86e7-34d6cee21610
verified: false
validated: true
submitted: true
---
# send-lineitems-postmessage

## Command

```javascript
window.postMessage({ type: "DigitalWalletsDialog:change", digitalWalletsDialog: true, payload: { title: "placeholder", button: "placeholder", lineItems: [{name: "product",amount: "$13.37",message: "added to cart" }], },}, "*");
```

## Description

Sends postMessage with lineItems to test product table rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| lineItems | Array of item objects | Yes |
| name | Product name | Yes |
| amount | Price string | Yes |
| message | Status message | Yes |

## Examples

### Basic Usage

```javascript
window.postMessage({ type: "DigitalWalletsDialog:change", digitalWalletsDialog: true, payload: { title: "placeholder", button: "placeholder", lineItems: [{name: "product",amount: "$13.37",message: "added to cart" }], },}, "*");
```

## Expected Output

Table with product row rendered.

## Related

- [[Related Procedure: Test-Legitimate-PostMessage-Payloads]]
