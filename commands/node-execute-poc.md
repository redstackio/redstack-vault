---
id: cmd-node-poc-001
data: node poc-undici-leak.js
name: node-execute-poc
tags:
  - execution
  - poc
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.615Z'
verified: false
validated: true
submitted: true
---
# node-execute-poc

## Command

```bash
node poc-undici-leak.js
```

## Description

Executes a Node.js script (poc-undici-leak.js) that uses the undici library to perform an HTTP request with Proxy-Authorization header, following cross-origin redirects to test for header leakage. Use this in a development environment to demonstrate the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc-undici-leak.js` | The PoC script file path | Yes |

## Examples

### Basic Usage

```bash
node poc-undici-leak.js
```

### Advanced Usage

```bash
node --trace-warnings poc-undici-leak.js
```

## Expected Output

Console logs showing response status (e.g., 200), headers, and body from the redirected endpoint. No errors if redirect succeeds; pair with server logs on port 8182 to see leaked header.

## Related

- [[Related Procedure|procedures/Create-and-Execute-Undici-PoC-Script]]
