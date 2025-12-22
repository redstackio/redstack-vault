---
id: cmd-make-install-squid-2023
data: make install
tags:
  - install
type: command
output: Installed files in squid-install/
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.919Z'
verified: false
validated: true
submitted: true
---
# make-install-squid

## Command

```bash
make install
```

## Description

Installs the compiled Squid files to the configured prefix directory.

## Parameters

None specific beyond Makefile targets.

## Examples

### Basic Usage

```bash
make install
```

### Advanced Usage

```bash
make install DESTDIR=/tmp/staging
```

## Expected Output

Installation progress; files copied to `squid-install/`.

## Related

- [[commands/make-compile-squid]]
- [[procedures/Build-and-Install-Vulnerable-Squid]]
