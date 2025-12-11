---
data: Object.keys(window)
tags:
  - javascript
  - recon
type: command
executor: javascript
platforms:
  - Web
id: 4b10d9fa-41cd-4c9e-a4d2-215e1ee2668f
created_at: '2025-12-11T06:10:17.653Z'
updated_at: '2025-12-11T06:10:17.653Z'
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

Lists properties of the window object to compare contexts and identify privileged APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) |  | No |

## Examples

### Basic Usage

```javascript
Object.keys(window)
```

## Expected Output

Array of window property names.

## Related

- [[procedures/Abuse-OEMBED-for-JavaScript-Injection]]
