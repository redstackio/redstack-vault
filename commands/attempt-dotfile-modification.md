---
id: cmd-attempt-bashrc-append
data: echo 'echo PWNED' >> /home/itszn/.bashrc
tags:
  - confinement-test
  - permission-denied
type: command
output: './tls/s: 20: ./tls/s: cannot create /home/itszn/.bashrc: Permission denied'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.793Z'
verified: false
validated: true
submitted: true
---
# attempt-dotfile-modification

## Command

```bash
echo 'echo PWNED' >> /home/itszn/.bashrc
```

## Description

Attempt to append to .bashrc dotfile inside snap to demonstrate container restriction.

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
echo 'test' >> ~/.profile
```

## Expected Output

Permission denied due to confinement.

## Related

- [[commands/attempt-system-file-read]]
- [[procedures/Demonstrate-Snap-Container-Restrictions]]
