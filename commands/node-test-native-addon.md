---
data: const addon = require('some-native-addon');
tags:
  - test
  - permissions
  - native
type: command
output: null
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.832Z'
id: 3db85e71-cf06-47e7-a59a-282c74264878
verified: false
validated: true
submitted: true
---
# node-test-native-addon

## Command

```javascript
const addon = require('some-native-addon');
```

## Description

Attempts to load a native addon module to verify permission model restrictions are active.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `module` | Name of the native addon | Yes |

## Examples

### Basic Usage

```javascript
require('binding.gyp-based-addon');
```

## Expected Output

Permission denied error if model is active.

## Related

- [[Related Procedure: Enable-Node.js-Permission-Model]]
