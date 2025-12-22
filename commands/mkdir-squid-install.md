---
id: cmd-mkdir-squid-install-2023
data: mkdir squid-install
tags:
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.962Z'
verified: false
validated: true
submitted: true
---
# mkdir-squid-install

## Command

```bash
mkdir squid-install
```

## Description

Creates a directory for installing the compiled Squid binary, isolating it from system paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `squid-install` | Directory name | Yes |

## Examples

### Basic Usage

```bash
mkdir squid-install
```

### Advanced Usage

```bash
mkdir -p squid-install/bin
```

## Expected Output

Silent success; directory ready for use.

## Related

- [[commands/configure-squid-build]]
- [[procedures/Build-and-Install-Vulnerable-Squid]]
