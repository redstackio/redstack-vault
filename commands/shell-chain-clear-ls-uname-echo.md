---
id: cmd-shell-chain
data: clear;ls;uname -a;echo RCE in Ruby Language By Black_EyE
tags:
  - recon
  - rce
type: command
output: 'Cleared terminal, directory listing, system details, and echo message'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.860Z'
verified: false
validated: true
submitted: true
---
# shell-chain-clear-ls-uname-echo

## Command

```bash
clear;ls;uname -a;echo RCE in Ruby Language By Black_EyE
```

## Description

This chained bash command clears the terminal, lists directory contents, displays detailed system information, and echoes a custom message. It is used to demonstrate control and gather basic server reconnaissance in RCE scenarios invoked via scripting languages like Ruby.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `clear` | Clears the terminal screen | No |
| `ls` | Lists files and directories | No |
| `uname -a` | Shows kernel version, hostname, architecture | No |
| `echo RCE in Ruby Language By Black_EyE` | Prints the exploitation message | No |

## Examples

### Basic Usage

```bash
clear;ls
```

### Advanced Usage

```bash
clear;ls -la;uname -a;echo "Server Compromised"
```

## Expected Output

Terminal screen clears, followed by output like:

dir1
file.txt
...

Linux server 5.4.0-42-generic #46-Ubuntu x86_64 GNU/Linux

RCE in Ruby Language By Black_EyE

This reveals the server's filesystem and OS details.

## Related

- [[commands/ruby-system-shell-invocation]]
