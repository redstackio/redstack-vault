---
type: command
executor: cmd
data: 'wmic startup get caption,command'
output: null
platforms:
  - Windows
tags:
  - enumeration
  - startup
verified: true
validated: true
---

# list-startup-programs-wmic

## Command

```cmd
wmic startup get caption,command
```

## Description

Uses WMIC to list startup programs with their captions and commands, covering various autostart locations for persistence enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| startup | WMIC class for startup programs | Built-in |
| get caption,command | Fields: name and execution command | Yes |

## Examples

### Basic Usage

```cmd
wmic startup get caption,command
```

### Advanced Usage

Format table:

```cmd
wmic startup get caption,command /format:table
```

## Expected Output

```
Caption                       Command
MyApp                         C:\Program Files\MyApp\app.exe
```

Table of startup items; success if no WMI errors.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
