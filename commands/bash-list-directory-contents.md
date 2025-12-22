---
type: command
executor: bash
data: ls
tags:
  - recon
  - command-injection
platforms:
  - Linux
verified: true
validated: true
---

# bash-list-directory-contents

## Command

```bash
ls
```

## Description

Lists the contents of the current directory in a Bash shell. Used in command injection to perform reconnaissance by enumerating files after injecting into a vulnerable command.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; lists current directory | No |

## Examples

### Basic Usage

```bash
ls
```

### With Options (Variations)

```bash
ls -la
```

## Expected Output

A list of files and directories:
dir1  file.txt  script.sh

## Related

- [[procedures/Command-Injection-Chaining-Commands]]
