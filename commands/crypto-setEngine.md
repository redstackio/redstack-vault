---
data: >-
  const crypto = require('crypto'); crypto.setEngine('path/to/malicious_engine',
  'bind_fn');
tags:
  - crypto
  - bypass
  - openssl
type: command
output: null
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.837Z'
id: 995005df-9273-4c44-9643-222f2ac26fe0
verified: false
validated: true
submitted: true
---
# crypto-setEngine

## Command

```javascript
const crypto = require('crypto');
crypto.setEngine('path/to/malicious_engine', 'bind_fn');
```

## Description

Sets a custom OpenSSL engine for crypto operations in Node.js, loading arbitrary native code via the specified engine path and bind function, bypassing permission restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `engine` | Path or identifier of the OpenSSL engine library | Yes |
| `bind_fn` | Name of the bind function in the engine | Yes |

## Examples

### Basic Usage

```javascript
crypto.setEngine('/path/to/engine.so', 'my_bind_fn');
```

### Advanced Usage

```javascript
crypto.setEngine('dynamic', { path: '/custom/engine', bind_function: 'init' });
```

## Expected Output

Engine loads silently; no errors if permissions allow (which they do for engines). Subsequent crypto calls use the engine.

## Related

- [[Related Procedure: Load-Arbitrary-OpenSSL-Engine-via-crypto.setEngine]]
