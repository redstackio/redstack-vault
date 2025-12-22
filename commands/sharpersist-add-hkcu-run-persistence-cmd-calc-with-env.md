---
type: command
executor: cmd
data: >-
  SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k
  "hkcurun" -v "Test Stuff" -m add -o env
output: null
platforms:
  - Windows
tags:
  - persistence
  - registry
  - environment
verified: true
validated: true
---

# sharpersist-add-hkcu-run-persistence-cmd-calc-with-env

## Command

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add -o env
```

## Description

This command adds a HKCU Run registry persistence entry to execute `cmd.exe /c calc.exe` and additionally handles environment variables (e.g., outputs or sets them for the persistence context). It's an extension for scenarios needing environmental context in the payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t reg | Persistence type: registry | Yes |
| -c "C:\Windows\System32\cmd.exe" | Executable path | Yes |
| -a "/c calc.exe" | Command arguments | Yes |
| -k "hkcurun" | Registry key target | Yes |
| -v "Test Stuff" | Value name | Yes |
| -m add | Add mode | Yes |
| -o env | Option to manage/output environment variables | Yes |

## Examples

### Basic Usage

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add -o env
```

### Advanced Usage

Use for backdoor with env: Adjust -a to backdoor path; -o env may log vars for debugging.

## Expected Output

`Persistence added. Environment variables: [list of vars].` Verify registry entry includes env context if applicable.

## Related

- [[procedures/windows-simple-user-registry-persistence]]
- [[tools/sharpersist]]
