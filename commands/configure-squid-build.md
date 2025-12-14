---
id: cmd-configure-squid-build-2023
data: ./configure --prefix=$(realpath ../squid-install)
tags:
  - configure
type: command
output: 'Configuration summary, ready for make'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.936Z'
verified: false
validated: true
submitted: true
---
# configure-squid-build

## Command

```bash
./configure --prefix=$(realpath ../squid-install)
```

## Description

Configures the Squid build with a local installation prefix using realpath for absolute path resolution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--prefix` | Installation directory | Yes |
| `$(realpath ../squid-install)` | Resolved path | Yes |

## Examples

### Basic Usage

```bash
./configure --prefix=$(realpath ../squid-install)
```

### Advanced Usage

```bash
./configure --prefix=/opt/squid --enable-ssl
```

## Expected Output

Configuration checks and summary indicating build readiness.

## Related

- [[commands/make-compile-squid]]
- [[procedures/Build-and-Install-Vulnerable-Squid]]
