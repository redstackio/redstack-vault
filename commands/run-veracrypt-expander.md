---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: '"C:\Program Files\VeraCrypt\VeraCryptExpander.exe"'
tags:
  - uac
  - elevation
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:44.553Z'
verified: false
validated: true
submitted: true
---
# run-veracrypt-expander

## Command

```cmd
"C:\Program Files\VeraCrypt\VeraCryptExpander.exe"
```

## Description

Launches the VeraCryptExpander executable, prompting UAC for elevation, setting up the vulnerable elevated process for the homepage trigger.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | Full path to VeraCryptExpander.exe | Yes |

## Examples

### Basic Usage

```cmd
"C:\Program Files\VeraCrypt\VeraCryptExpander.exe"
```

## Expected Output

UAC prompt appears; upon approval, GUI window opens with Homepage button.

## Related

- [[procedures/Trigger-UAC-Bypass-via-VeraCryptExpander-Homepage]]
