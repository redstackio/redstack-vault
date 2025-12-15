---
id: cmd-make-compile-squid-2023
data: make -j$(nproc)
tags:
  - compile
type: command
output: Compiled binaries
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.931Z'
verified: false
validated: true
submitted: true
---
# make-compile-squid

## Command

```bash
make -j$(nproc)
```

## Description

Compiles Squid source using parallel jobs based on CPU cores for efficient building.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-j` | Parallel jobs | Yes |
| `$(nproc)` | Number of processors | Yes |

## Examples

### Basic Usage

```bash
make -j$(nproc)
```

### Advanced Usage

```bash
make -j4 clean all
```

## Expected Output

Compilation progress; binaries in current directory.

## Related

- [[commands/make-install-squid]]
- [[procedures/Build-and-Install-Vulnerable-Squid]]
