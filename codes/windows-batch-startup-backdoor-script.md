---
id: b8542a1b-6d22-4877-9e14-bffa645d4161
name: windows-batch-startup-backdoor-script
type: code
language: batch
verified: true
created_at: '2023-04-06T03:56:27.811713+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - persistence
  - payload
  - startup
validated: true
---

# windows-batch-startup-backdoor-script

## Code

```batch
start /b C:\Users\%USERNAME%\AppData\Local\Temp\backdoor.exe
```

## Description

A simple Windows batch script designed for placement in the user's Startup folder. It launches a backdoor executable silently in the background upon logon, enabling persistence without user interaction or visible windows.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `%USERNAME%` | Current user's username (environment variable) | Rasta |
| `backdoor.exe` | Path to the backdoor executable | C:\Users\Rasta\AppData\Local\Temp\backdoor.exe |

## Usage

Embed this script into a .bat file in %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup. It executes automatically on user logon. Customize the path to point to your payload. Used in red team operations for maintaining access after initial compromise.

## Detection

- File monitoring in Startup folder for newly created .bat files.
- Process creation events for backdoor.exe spawning from cmd.exe at logon time.
- Behavioral analytics detecting background starts from temp directories.

## Related

- [[procedures/Windows-User-Startup-Folder-Persistence]]
- [[cmd-start-backdoor-executable]]
