---
id: cmd-apt-install-deps
data: sudo apt install liblua5.1-0-dev libboost-dev
tags:
  - apt
  - dependencies
type: command
output: Package installation output
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.133Z'
verified: false
validated: true
submitted: true
---
# apt-install-deps

## Command

```bash
sudo apt install liblua5.1-0-dev libboost-dev
```

## Description

Installs Lua 5.1 development headers and Boost libraries via apt, required for compiling rubyluabridge on Ubuntu.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `liblua5.1-0-dev` | Lua dev package | Yes |
| `libboost-dev` | Boost C++ dev libraries | Yes |

## Examples

### Basic Usage

```bash
sudo apt install liblua5.1-0-dev libboost-dev
```

### Advanced Usage

```bash
sudo apt update && sudo apt install -y liblua5.1-0-dev libboost-dev
```

## Expected Output

Package resolver, download progress, and 'Setting up liblua5.1-0-dev' messages.

## Related

- [[commands/build-extconf]]
- [[procedures/Install-rubyluabridge-for-Lua-Extension]]
