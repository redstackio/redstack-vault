---
id: b47d8829-bbd4-43fe-81e9-50d04f76df8e
name: ruby-execute-tty-shell
type: command
executor: bash
data: ruby -e 'exec "/bin/sh"'
output: null
created_at: '2019-09-20T19:50:15.364245+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Mac OSx
  - Windows
tags:
  - shell
  - execution
verified: true
validated: true
---

# ruby-execute-tty-shell

## Command

```bash
ruby -e 'exec "/bin/sh"'
```

## Description

This command uses Ruby to execute a TTY shell directly from the command line. It is useful in penetration testing scenarios where Ruby is available on the target system but other shell spawning tools are restricted. The exec function replaces the current process with a new /bin/sh shell, providing interactive access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Executes the following Ruby code string | Yes |
| `'exec "/bin/sh"'` | Ruby code to spawn a /bin/sh shell | Yes |

## Examples

### Basic Usage

```bash
ruby -e 'exec "/bin/sh"'
```

This spawns a basic Bourne shell (/bin/sh) interactively.

### Advanced Usage

For a different shell, modify the exec argument:

```bash
ruby -e 'exec "/bin/bash"'
```

## Expected Output

Upon successful execution, the command drops into an interactive shell prompt, such as:

```
$ whoami
user
$ pwd
/home/user
```

No additional output is produced before the shell starts; success is indicated by the shell prompt appearing.

## Related

- [[tools/Ruby]] (tool for running Ruby scripts and commands)
- [[procedures/Spawn-Reverse-Shell-via-Ruby]] (if used in a procedure context)
