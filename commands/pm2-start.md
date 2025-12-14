---
id: uuid-pm2-start
data: ./pm2 start
tags:
  - setup
  - pm2
type: command
output: Error about missing ecosystem.config.js and empty process table
executor: bash
platforms:
  - Node.js
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.560Z'
verified: false
validated: true
submitted: true
---
# pm2-start

## Command

```bash
./pm2 start
```

## Description

Starts the PM2 daemon, initializing it and checking for configuration files like ecosystem.config.js.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `start` | Command to launch PM2 daemon | Yes |

## Examples

### Basic Usage

```bash
./pm2 start
```

### Advanced Usage

```bash
./pm2 start --no-daemon
```

## Expected Output

PM2 starts with logs: warns about missing config, shows empty process list (┌─────┬──────────┬─────────────┐).

## Related

- [[commands/ln-symlink-pm2]]
- [[procedures/Install-and-Setup-PM2]]
