---
id: uuid-ln-symlink
data: ln -s ./node_modules/pm2/bin/pm2 pm2
tags:
  - setup
  - symlink
type: command
output: 'Symlink created, verifiable with ls -l'
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.563Z'
verified: false
validated: true
submitted: true
---
# ln-symlink-pm2

## Command

```bash
ln -s ./node_modules/pm2/bin/pm2 pm2
```

## Description

Creates a symbolic link to the PM2 executable in the current directory for easy access without specifying full paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Symbolic link flag | Yes |
| `./node_modules/pm2/bin/pm2` | Source path to PM2 binary | Yes |
| `pm2` | Target link name | Yes |

## Examples

### Basic Usage

```bash
ln -s ./node_modules/pm2/bin/pm2 pm2
```

### Advanced Usage

```bash
ln -sf ./node_modules/pm2/bin/pm2 pm2  # Force overwrite if exists
```

## Expected Output

No output on success; use 'ls -l pm2' to confirm link points to binary.

## Related

- [[commands/npm-install-pm2]]
- [[procedures/Install-and-Setup-PM2]]
