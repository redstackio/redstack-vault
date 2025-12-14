---
id: cmd-tail-bashrc
data: tail -n 1 /home/itszn/.bashrc
tags:
  - verification
  - persistence
type: command
output: echo PWNED
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.758Z'
verified: false
validated: true
submitted: true
---
# check-dotfile-modification

## Command

```bash
tail -n 1 /home/itszn/.bashrc
```

## Description

Show last line of .bashrc to confirm modification after escape.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n 1 | Last 1 line | Yes |
| /home/itszn/.bashrc | Target file | Yes |

## Examples

### Basic Usage

```bash
tail -n 1 /home/itszn/.bashrc
```

### Advanced Usage

```bash
tail -n 5 ~/.bashrc
```

## Expected Output

echo PWNED.

## Related

- [[commands/modify-dotfile-post-escape]]
- [[procedures/Verify-Host-Access-After-Escape]]
