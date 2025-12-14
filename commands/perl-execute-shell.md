---
id: cmd-perl-execute
data: perl /tmp/shell2.pl
tags:
  - execute
  - reverse-shell
type: command
output: Establishes reverse TCP connection to attacker's listener
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.676Z'
verified: false
validated: true
submitted: true
---
# perl-execute-shell

## Command

```bash
perl /tmp/shell2.pl
```

## Description

Executes a Perl script that spawns a reverse shell connecting back to the attacker's IP and port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/shell2.pl | Path to the Perl reverse shell script | Yes |

## Examples

### Basic Usage

```bash
perl /tmp/shell.pl
```

### Advanced Usage

With error handling: perl -e 'script code' (inline)

## Expected Output

Reverse connection established; stdin/stdout redirected to socket.

## Related

- [[commands/curl-download-shell]]
