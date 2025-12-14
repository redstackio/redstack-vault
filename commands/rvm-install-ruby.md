---
id: cmd-rvm-install-ruby
data: rvm install 2.7.4
tags:
  - ruby
  - install
type: command
output: Installation progress and success message
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.141Z'
verified: false
validated: true
submitted: true
---
# rvm-install-ruby

## Command

```bash
rvm install 2.7.4
```

## Description

Installs Ruby version 2.7.4 using RVM, matching GitLab's embedded Ruby for compatible gem building.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `2.7.4` | Ruby version to install | Yes |

## Examples

### Basic Usage

```bash
rvm install 2.7.4
```

### Advanced Usage

```bash
rvm install 2.7.4 --with-openssl-dir=/path
```

## Expected Output

Download, compile progress, and 'To use: rvm 2.7.4' message.

## Related

- [[commands/source-rvm]]
- [[procedures/Install-rubyluabridge-for-Lua-Extension]]
