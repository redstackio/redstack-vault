---
id: cmd-uuid-2
data: |-
  @echo off
  START C:\Windows\NOTEPAD.EXE
tags:
  - rce
  - batch
type: command
output: Opens Notepad application on Windows
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.226Z'
verified: false
validated: true
submitted: true
---
# rce-batch-payload

## Command

```batch
@echo off
START C:\Windows\NOTEPAD.EXE
```

## Description

Batch script payload that suppresses command echoing and launches Notepad.exe, demonstrating RCE when executed as a disguised file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @echo off | Suppresses command echoing in console | Yes |
| START | Initiates execution of the specified program | Yes |
| C:\Windows\NOTEPAD.EXE | Path to Notepad executable for PoC | Yes |

## Examples

### Basic Usage

Save as .bat and run.

```batch
@echo off
START C:\Windows\NOTEPAD.EXE
```

### Advanced Usage

Replace Notepad with other commands for real malware.

```batch
@echo off
START calc.exe
```

## Expected Output

Notepad application window opens silently.

## Related

- [[commands/malicious-php-torrent-server]]
