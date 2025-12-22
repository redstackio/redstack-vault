---
id: uuid-mkdir-1
type: command
executor: bash
data: mkdir -p ~/.config/autostart
output: null
created_at: '2023-04-06T03:56:18.070727+00:00'
updated_at: '2023-04-10T20:34:18.923868+00:00'
platforms:
  - Linux
tags:
  - persistence
  - linux
verified: true
validated: true
---

# mkdir-create-autostart-directory

## Command

```bash
mkdir -p ~/.config/autostart
```

## Description

Creates the user's autostart directory for desktop environment startup files. The -p flag ensures parent directories are created if needed and suppresses errors if the directory already exists. Use this as a prerequisite for placing persistence mechanisms in graphical Linux environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p | Create parent directories as needed and do not error if existing | Yes |
| ~/.config/autostart | Target directory path for user autostart files | Yes |

## Examples

### Basic Usage

```bash
mkdir -p ~/.config/autostart
```

### Advanced Usage

Not applicable; this is a simple directory creation.

## Expected Output

No output on success. If the directory already exists, the command completes silently. Error if insufficient permissions (e.g., "Permission denied").

## Related

- [[procedures/Linux-Backdoor-User-Autostart-File]]
