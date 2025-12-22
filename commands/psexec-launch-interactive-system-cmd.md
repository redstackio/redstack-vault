---
id: e4f767a9-03ff-460c-a6ac-9bac3748a81b
name: psexec-launch-interactive-system-cmd
type: command
executor: cmd
data: PsExec.exe -i -s cmd.exe
output: null
created_at: '2023-04-06T03:56:30.042797+00:00'
updated_at: '2023-04-10T20:37:35.583509+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - psexec
verified: true
validated: true
---

# psexec-launch-interactive-system-cmd

## Command

```cmd
PsExec.exe -i -s cmd.exe
```

## Description

This command uses PsExec to launch an interactive command prompt (cmd.exe) running under the NT SYSTEM account, escalating privileges from a local administrator context. It is used in post-exploitation to gain full system access for tasks like persistence or credential dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Enables interactive mode, allowing the process to interact with the desktop (useful for spawning windows) | Yes |
| -s | Runs the process in the SYSTEM account context, providing highest privileges | Yes |
| cmd.exe | The target executable to run (command prompt); can be replaced with other binaries like powershell.exe | Yes |

## Examples

### Basic Usage

```cmd
PsExec.exe -i -s cmd.exe
```

### Advanced Usage

```cmd
PsExec.exe -i -s powershell.exe
```
(Launches PowerShell as SYSTEM instead of cmd.)

## Expected Output

The command executes silently or with minimal output, spawning a new command window. Verify success by running `whoami` in the new prompt:
```
Microsoft Windows [Version 10.0.19041.264]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
nt authority\system
```
If failed, error like "Access is denied" or "The system cannot find the file specified" appears.

## Related

- [[procedures/Local-Administrator-to-NT-SYSTEM-Privilege-Escalation]]
- [[tools/PsExec]]
