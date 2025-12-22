---
data: Object.prototype
tags:
  - prototype
  - inspection
type: command
executor: javascript
platforms:
  - Web
id: 97d6236e-6053-4a8b-9942-3bf690250463
created_at: '2025-12-13T23:56:20.392Z'
updated_at: '2025-12-13T23:56:20.392Z'
verified: false
validated: true
submitted: true
---
# Check Object Prototype

## Command

```javascript
Object.prototype
```

## Description

Displays the Object prototype in the browser console to check for polluted properties, used after visiting a URL with potentially polluting parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | N/A |

## Examples

### Basic Usage

```javascript
Object.prototype
```

## Expected Output

Object prototype with added properties like ggg: 'aaa' if pollution occurred.

## Related

- [[procedures/Discover-Prototype-Pollution-in-Wistia-Script]]
- [[procedures/Test-Prototype-Pollution]]
