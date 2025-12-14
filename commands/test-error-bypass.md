---
data: result =u(new Error("'\"<b>")); result.message;
tags:
  - bypass
  - error
type: command
output: '"''"<b>\"'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.386Z'
id: 5847bb87-e59d-484c-8ef9-b6543aaa5610
verified: false
validated: true
submitted: true
---
# test-error-bypass

## Command

```javascript
result =u(new Error("'\"<b>")); result.message;
```

## Description

Tests bypass on Error object with non-enumerable message.

## Parameters

None specific.

## Examples

### Basic Usage

```javascript
result =u(new Error("'\"<b>")); result.message;
```

## Expected Output

Unescaped: "'"<b>\"

## Related

- [[Related Procedure: Identify-Escaping-Function-Bypass]]
