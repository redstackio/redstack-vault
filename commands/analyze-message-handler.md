---
data: >-
  function c(inst, type, payload){switch(type){case
  ze.DIALOG_CHANGE:if(d(payload)){g(inst) p(inst, payload)...
tags:
  - analysis
  - handler
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.410Z'
id: 0b1616ad-53d9-4e31-8d75-b390a86f25bd
verified: false
validated: true
submitted: true
---
# analyze-message-handler

## Command

```javascript
function c(inst, type, payload){switch(type){case ze.DIALOG_CHANGE:if(d(payload)){g(inst) p(inst, payload)...
```

## Description

Defines the message processing function that switches on type and calls validation, reset, and update functions for dialog changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| inst | Instance object | Yes |
| type | Message type (e.g., ze.DIALOG_CHANGE) | Yes |
| payload | Data object | Yes |

## Examples

### Basic Usage

```javascript
function c(inst, type, payload){switch(type){case ze.DIALOG_CHANGE:if(d(payload)){g(inst) p(inst, payload)...
```

## Expected Output

Function definition; call with params to process payload.

## Related

- [[Related Procedure: Analyze-Shopify-Digital-Wallets-JavaScript]]
