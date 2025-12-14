---
id: cmd-uuid-002
data: open -a Calculator
tags:
  - execution
  - app-launch
type: command
output: null
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.085Z'
verified: false
validated: true
submitted: true
---
# open-calculator

## Command

```bash
open -a Calculator
```

## Description

Launches the Calculator application on macOS using the open command. In the exploit, this is executed via do shell script in AppleScript to prove arbitrary app execution capability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Specifies the application bundle to open | Yes |
| Calculator | Name of the app | Yes |

## Examples

### Basic Usage

```bash
open -a Calculator
```

### Advanced Usage

```bash
open -a "/Applications/Calculator.app"
```

## Expected Output

Calculator app launches on the desktop.

## Related

- [[Related Procedure: Host-Malicious-AppleScript-App-on-NFS-Mount]]
