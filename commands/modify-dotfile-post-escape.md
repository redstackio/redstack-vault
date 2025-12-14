---
id: cmd-append-bashrc-escape
data: echo 'echo PWNED' >> /home/itszn/.bashrc
tags:
  - escape-verification
  - persistence
type: command
output: 'Success, adds line'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.763Z'
verified: false
validated: true
submitted: true
---
# modify-dotfile-post-escape

## Command

```bash
echo 'echo PWNED' >> /home/itszn/.bashrc
```

## Description

Append to .bashrc after escape to confirm dotfile access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| >> /home/itszn/.bashrc | Append to file | Yes |

## Examples

### Basic Usage

```bash
echo 'echo PWNED' >> /home/itszn/.bashrc
```

### Advanced Usage

```bash
echo 'malicious' >> ~/.profile
```

## Expected Output

Success, adds line without error.

## Related

- [[commands/check-dotfile-modification]]
- [[procedures/Verify-Host-Access-After-Escape]]
