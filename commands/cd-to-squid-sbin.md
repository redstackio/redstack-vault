---
id: cmd-cd-to-squid-sbin-2023
data: cd ../squid-install/sbin/
tags:
  - navigation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.908Z'
verified: false
validated: true
submitted: true
---
# cd-to-squid-sbin

## Command

```bash
cd ../squid-install/sbin/
```

## Description

Navigates to the sbin directory containing the installed Squid binary for execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `../squid-install/sbin/` | Target path | Yes |

## Examples

### Basic Usage

```bash
cd ../squid-install/sbin/
```

### Advanced Usage

```bash
cd ../squid-install/sbin/ && ./squid --version
```

## Expected Output

Path change; binary accessible.

## Related

- [[commands/make-install-squid]]
- [[procedures/Build-and-Install-Vulnerable-Squid]]
