---
data: Object.keys(window)
tags:
  - inspection
  - javascript
type: command
executor: javascript
platforms:
  - Web
id: 92bc305b-ac0c-40eb-9abf-d78327d19136
created_at: '2025-12-14T00:11:25.287Z'
updated_at: '2025-12-14T00:11:25.287Z'
verified: false
validated: true
submitted: true
---
# object-keys-window

## Command

```javascript
Object.keys(window)
```

## Description

Dumps all properties of the window object to compare with normal Chrome, used in embedded contexts like codepen.io.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```javascript
Object.keys(window)
```

## Expected Output

Array of window property names, highlighting Steam-specific additions.

## Related

- [[procedures/Escalating-with-Steam-URI-Schemes]]
