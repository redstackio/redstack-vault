---
id: cmd-ruby-system
data: |-
  # Hello World Program in Ruby
  system "clear;ls;uname -a;echo RCE in Ruby Language By Black_EyE";
tags:
  - rce
  - shell
type: command
output: >-
  Cleared screen, directory listing, system information (e.g., Linux kernel
  details), and 'RCE in Ruby Language By Black_EyE'
executor: ruby
platforms:
  - Ruby
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.873Z'
verified: false
validated: true
submitted: true
---
# ruby-system-shell-invocation

## Command

```ruby
# Hello World Program in Ruby
system "clear;ls;uname -a;echo RCE in Ruby Language By Black_EyE";
```

## Description

This Ruby command uses the built-in system function to execute a chain of shell commands on the host OS, demonstrating RCE by running OS-level operations from within a Ruby script. Use it in environments where Ruby has access to system calls, such as unsandboxed online interpreters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `system` | Ruby method to invoke shell command | Yes |
| `"clear;ls;uname -a;echo RCE in Ruby Language By Black_EyE"` | Chained shell commands: clear screen, list directory, show system info, echo message | Yes |

## Examples

### Basic Usage

```ruby
system "ls"
```

### Advanced Usage

```ruby
system "clear;ls -la;uname -a;echo 'Exploitation Successful'"
```

## Expected Output

The command executes the shell chain: screen clears, followed by a listing of current directory contents (e.g., bin, etc folders on Linux), detailed system information (e.g., "Linux hostname 5.4.0-42-generic #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020 x86_64 GNU/Linux"), and the printed message "RCE in Ruby Language By Black_EyE". In a console, this reveals server environment details.

## Related

- [[commands/shell-chain-clear-ls-uname-echo]]
