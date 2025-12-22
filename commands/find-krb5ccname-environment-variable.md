---
id: 8c2ffe73-3209-4142-b8a1-ddb8bf2f618a
name: find-krb5ccname-environment-variable
type: command
executor: bash
data: env | grep KRB5CCNAME
output: null
created_at: '2023-04-06T03:56:08.524695+00:00'
updated_at: '2023-04-10T20:36:14.401667+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - credential-access
verified: true
validated: true
---

# find-krb5ccname-environment-variable

## Command

```bash
env | grep KRB5CCNAME
```

## Description

This command displays the current KRB5CCNAME environment variable, which specifies the location of the Kerberos ticket cache file. Use it to identify if and where active Kerberos tickets are stored, typically in /tmp on Linux systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `env` | Prints all environment variables | Built-in |
| `|` | Pipes output to next command | Built-in |
| `grep KRB5CCNAME` | Filters for the KRB5CCNAME variable | Built-in |

## Examples

### Basic Usage

```bash
env | grep KRB5CCNAME
```

### Advanced Usage

Combine with echo for verification:
```bash
echo $KRB5CCNAME || env | grep KRB5CCNAME
```

## Expected Output

If set:
```
KRB5CCNAME=FILE:/tmp/krb5cc_1000
```

If not set, no output.

## Related

- [[procedures/reuse-kerberos-ccache-tickets-from-tmp]]
