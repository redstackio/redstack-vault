---
id: cmd-build-extconf
data: ./build/extconf_ubuntu.sh
tags:
  - build
  - configure
type: command
output: Configuration output
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.130Z'
verified: false
validated: true
submitted: true
---
# build-extconf

## Command

```bash
./build/extconf_ubuntu.sh
```

## Description

Runs the Ubuntu-specific configuration script for rubyluabridge, generating Makefiles for compilation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./build/extconf_ubuntu.sh` | Config script path | Yes |

## Examples

### Basic Usage

```bash
./build/extconf_ubuntu.sh
```

### Advanced Usage

```bash
cd rubyluabridge && ./build/extconf_ubuntu.sh
```

## Expected Output

Extconf logs, e.g., 'creating Makefile', detecting Lua/Boost paths.

## Related

- [[commands/make-build]]
- [[procedures/Install-rubyluabridge-for-Lua-Extension]]
