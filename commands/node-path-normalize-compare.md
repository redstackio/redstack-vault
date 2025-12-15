---
data: >-
  const path = require('path');
  console.log(path.normalize('CON:../../secret.txt'));
  console.log(path.join('\\\\server\\share\\uploads','CON:../../secret.txt'));
tags:
  - comparison
  - normalize
type: command
output: |-
  .\\CON:..\\..\\secret.txt
  \\\\server\\share\\secret.txt
executor: javascript
platforms:
  - Windows
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.234Z'
id: 2d6848e5-4caa-4fff-883c-594b37b16871
verified: false
validated: true
submitted: true
---
# node-path-normalize-compare

## Command

```javascript
const path = require('path');
console.log(path.normalize('CON:../../secret.txt'));
console.log(path.join('\\\\server\\share\\uploads','CON:../../secret.txt'));
```

## Description

Compares path normalization for regular vs. UNC paths to highlight the fix inconsistency.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input | Path with device and traversal | Yes |
| base | UNC base path | Yes |

## Examples

### Basic Usage

```javascript
path.normalize('CON:../../secret.txt')
```

### Advanced Usage

```javascript
path.join('\\\\server\\public', 'PRN:../config.txt')
```

## Expected Output

Safe prefix for regular; escaped for UNC.

## Related

- [[commands/node-path-join-unc-test]]
