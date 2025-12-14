---
id: cmd-install-rvm
data: 'curl -sSL https://get.rvm.io | bash'
tags:
  - setup
  - ruby
type: command
output: RVM installation script output
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.157Z'
verified: false
validated: true
submitted: true
---
# install-rvm

## Command

```bash
curl -sSL https://get.rvm.io | bash
```

## Description

Downloads and installs Ruby Version Manager (RVM) from the official script, enabling multi-Ruby environment management for building gems like rubyluabridge.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode (no progress) | Yes |
| `-S` | Show errors | Yes |
| `-L` | Follow redirects | Yes |
| `https://get.rvm.io` | RVM install script URL | Yes |

## Examples

### Basic Usage

```bash
curl -sSL https://get.rvm.io | bash
```

### Advanced Usage

```bash
curl -sSL https://get.rvm.io | bash -s stable --ruby
```

## Expected Output

Installation progress, profile additions (e.g., 'To start using RVM you need to run source /etc/profile.d/rvm.sh'), and success confirmation.

## Related

- [[commands/source-rvm]]
- [[procedures/Install-rubyluabridge-for-Lua-Extension]]
