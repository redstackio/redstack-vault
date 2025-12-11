---
data: open /Applications/Calculator.app
tags:
  - rce
  - macos
type: command
executor: bash
platforms:
  - Mac
id: 3c2c8758-9689-42b5-8fc6-7b1566769796
created_at: '2025-12-11T06:10:22.504Z'
updated_at: '2025-12-11T06:10:22.504Z'
verified: false
validated: true
submitted: true
---
# open-calculator-macos

## Command

```bash
open /Applications/Calculator.app
```

## Description

Opens the Calculator application on macOS to demonstrate remote code execution in the Slack exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/Applications/Calculator.app` | Path to the app | Yes |

## Examples

### Basic Usage

```bash
open /Applications/Calculator.app
```

## Expected Output

Calculator app launches on the victim's macOS system.

## Related

- [[commands/exec-shell-command-nodejs]]
- [[procedures/Execute-RCE-on-Victim-Interaction]]
