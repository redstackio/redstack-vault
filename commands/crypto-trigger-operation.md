---
data: >-
  const hash = crypto.createHash('sha256').update('data').digest();
  console.log(hash);
tags:
  - crypto
  - execution
  - trigger
type: command
output: null
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.835Z'
id: 35f717a2-16ca-47e1-9617-052c3b6b85ec
verified: false
validated: true
submitted: true
---
# crypto-trigger-operation

## Command

```javascript
const hash = crypto.createHash('sha256').update('data').digest();
console.log(hash);
```

## Description

Performs a cryptographic hash operation to trigger the loaded OpenSSL engine, executing its native bind_fn and any arbitrary code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `algorithm` | Hash algorithm (e.g., 'sha256') | Yes |
| `data` | Input data to hash | Yes |

## Examples

### Basic Usage

```javascript
crypto.createHash('sha256').update('test').digest('hex');
```

### Advanced Usage

```javascript
crypto.createHash('md5').update(Buffer.from('data')).digest();
```

## Expected Output

Binary hash buffer printed or logged; native code side effects may appear in console or system behavior.

## Related

- [[Related Procedure: Achieve-Arbitrary-Code-Execution-Bypassing-Permissions]]
