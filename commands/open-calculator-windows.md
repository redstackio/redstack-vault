---
data: calc
tags:
  - rce
  - windows
type: command
executor: cmd
platforms:
  - Windows
id: df8002f2-81a3-490d-b3c5-42ab5557fdf8
created_at: '2025-12-11T06:10:22.494Z'
updated_at: '2025-12-11T06:10:22.494Z'
verified: false
validated: true
submitted: true
---
# open-calculator-windows

## Command

```cmd
calc
```

## Description

Opens the Calculator on Windows to demonstrate remote code execution in the Slack exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```cmd
calc
```

## Expected Output

Calculator app launches on the victim's Windows system.

## Related

- [[commands/exec-shell-command-nodejs]]
- [[procedures/Execute-RCE-on-Victim-Interaction]]
