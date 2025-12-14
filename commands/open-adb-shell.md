---
data: adb shell
tags:
  - adb
  - shell-access
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:40.068Z'
id: 2e738406-5cf7-4db1-ae3b-e8371caef225
verified: false
validated: true
submitted: true
---
# open-adb-shell

## Command

```bash
adb shell
```

## Description

Opens an interactive shell on the connected Android device for executing commands like 'content query'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters | No |

## Examples

### Basic Usage

```bash
adb shell
```

### Advanced Usage

```bash
adb -s <serial> shell
```

## Expected Output

Device shell prompt, e.g., 'shell@device:/ $'

## Related

- [[commands/list-adb-devices]]
