---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
name: console-log-safeeval
type: command
executor: javascript
data: console.log(safeEval(code));
output: Logs 'pwned' to console via util.log
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.336Z'
platforms:
  - Node.js
tags:
  - rce
  - execution
verified: false
validated: true
submitted: true
---

# console-log-safeeval

## Command

```javascript
console.log(safeEval(code));
```

## Description

Evaluates the malicious code string using safeEval and logs the result, triggering the sandbox escape and RCE in Node.js.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| code | The crafted payload string | Yes |

## Examples

### Basic Usage

```javascript
console.log(safeEval(code));
```

### Advanced Usage

Omit console.log for silent execution if payload returns data.

## Expected Output

Console displays 'pwned' from util.log, confirming RCE success.

## Related

- [[commands/define-malicious-code-nodejs]]
- [[procedures/Execute-Sandbox-Escape-Payload-in-Node.js]]
