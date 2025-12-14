---
id: cmd-source-rvm
data: source /etc/profile.d/rvm.sh
tags:
  - setup
  - environment
type: command
output: 'No output, loads environment variables'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.154Z'
verified: false
validated: true
submitted: true
---
# source-rvm

## Command

```bash
source /etc/profile.d/rvm.sh
```

## Description

Loads the RVM initialization script into the current shell session, making rvm commands available immediately without restarting the terminal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/profile.d/rvm.sh` | Path to RVM profile script | Yes |

## Examples

### Basic Usage

```bash
source /etc/profile.d/rvm.sh
```

### Advanced Usage

```bash
. /etc/profile.d/rvm.sh  # Alternative dot syntax
```

## Expected Output

No visible output; verify with `rvm --version` showing RVM details.

## Related

- [[commands/install-rvm]]
- [[procedures/Install-rubyluabridge-for-Lua-Extension]]
