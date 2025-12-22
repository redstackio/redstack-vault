---
type: command
executor: bash
data: export KRB5CCNAME=$PWD/$_CCACHE_FILE
output: null
created_at: '2023-04-06T03:56:08.524815+00:00'
updated_at: '2023-04-10T20:36:14.401667+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - environment
verified: true
validated: true
---

# set-krb5ccname-environment-variable

## Command

```bash
export KRB5CCNAME=$PWD/$_CCACHE_FILE
```

## Description

Sets the KRB5CCNAME environment variable to point to the Kerberos credential cache file, allowing tools to use the loaded ticket for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `KRB5CCNAME` | Path to ccache file | Yes |
| `$_CCACHE_FILE` | Filename (e.g., ticket.ccache) | Yes |

## Examples

### Basic Usage

```bash
export KRB5CCNAME=/home/user/ticket.ccache
```

### Advanced Usage

Use $PWD for current directory: `export KRB5CCNAME=$PWD/admin.ccache`

## Expected Output

No output; verify with `echo $KRB5CCNAME`.

## Related

- [[procedures/Forge-and-Use-Golden-Ticket-on-Linux]]
