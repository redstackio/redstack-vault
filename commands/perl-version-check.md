---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: perl-version-check
type: command
executor: bash
data: perl -v && netstat -tuln | grep 51337
output: null
created_at: '2023-04-06T03:56:08.747540+00:00'
updated_at: '2023-04-10T20:21:16.647403+00:00'
platforms:
  - Linux
  - Unix
tags:
  - prerequisite-check
  - perl
verified: true
validated: true
---

# perl-version-check

## Command

```bash
perl -v && netstat -tuln | grep 51337
```

## Description

This command checks if Perl is installed on the target system and verifies if port 51337 is already in use. Use it as a prerequisite before deploying a bind shell to ensure compatibility and avoid port conflicts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs standard checks | No |

## Examples

### Basic Usage

```bash
perl -v && netstat -tuln | grep 51337
```

### Advanced Usage

On systems without netstat, use `ss -tuln | grep 51337` instead.

## Expected Output

Perl version information followed by either empty output (port free) or listener details if in use:

```
This is perl 5, version 30, subversion 0 (v5.30.0) built for x86_64-linux-gnu-thread-multi
...

(no output if port free)
```

## Related

- [[procedures/Create-Perl-Bind-Shell]]
- [[commands/perl-bind-shell-listener]]
