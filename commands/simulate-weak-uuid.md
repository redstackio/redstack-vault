---
id: cmd-simulate-weak-uuid
data: >-
  const fs = require('fs'); const tokens = []; for (let i = 0; i < 1000; i++) {
  const token = Math.random().toString(36).substring(2) +
  Date.now().toString(36); tokens.push(token); }
  fs.writeFileSync('predicted_tokens.txt', tokens.join('\n'));
  console.log('Generated 1000 predicted tokens.');
tags:
  - crypto
  - simulation
type: command
output: Generated 1000 predicted tokens.
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.748Z'
verified: false
validated: true
submitted: true
---
# simulate-weak-uuid

## Command

```javascript
const fs = require('fs');
const tokens = [];
for (let i = 0; i < 1000; i++) {
  const token = Math.random().toString(36).substring(2) + Date.now().toString(36);
  tokens.push(token);
}
fs.writeFileSync('predicted_tokens.txt', tokens.join('\n'));
console.log('Generated 1000 predicted tokens.');
```

## Description

This Node.js script simulates the weak UUID generation from joola.io's common.uuid() method, producing a file of predictable tokens for brute-force testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i < 1000` | Number of tokens to generate | No (default 1000) |
| `Date.now()` | Incorporates timestamp for realism | Yes |

## Examples

### Basic Usage

```javascript
node -e "const fs = require('fs'); const tokens = []; for (let i = 0; i < 1000; i++) { const token = Math.random().toString(36).substring(2) + Date.now().toString(36); tokens.push(token); } fs.writeFileSync('predicted_tokens.txt', tokens.join('\n'));"
```

### Advanced Usage

```javascript
node -e "const crypto = require('crypto'); const weak = () => Math.random().toString(36).substring(2); console.log('Weak:', weak()); console.log('Secure:', crypto.randomUUID());"
```

## Expected Output

File 'predicted_tokens.txt' created with lines of tokens like 'abc123def4561699123456789'. Console: 'Generated 1000 predicted tokens.'

## Related

- [[Related Procedure: Brute-Force-Predictable-Auth-Tokens]]
