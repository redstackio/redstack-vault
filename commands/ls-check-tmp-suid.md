---
data: ls -l /tmp
tags:
  - list
  - suid
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.168Z'
id: d629fad9-1e6a-49c7-b773-b63e01b52d2e
verified: false
validated: true
submitted: true
---
# ls-check-tmp-suid

## Command

```bash
ls -l /tmp
```

## Description

Lists files in /tmp with long format to verify the creation of the SUID evilbash binary after payload execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Long format | Yes |
| /tmp | Directory path | Yes |

## Examples

### Basic Usage

```bash
ls -l /tmp
```

### Advanced Usage

```bash
ls -l /tmp | grep -E 'rws|evilbash'
```

## Expected Output

Shows /tmp/evilbash with permissions like -rwsr-xr-x 1 root root ...

## Related

- [[commands/execute-suid-bash]]
- [[procedures/Execute-SUID-Bash-for-Root-Access]]
