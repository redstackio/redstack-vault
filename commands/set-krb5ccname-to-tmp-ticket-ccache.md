---
id: ea9af8f0-d40d-4cce-9da2-96875980f74c
name: set-krb5ccname-to-tmp-ticket-ccache
type: command
executor: bash
data: export KRB5CCNAME=/tmp/ticket.ccache
output: null
created_at: '2023-04-06T03:56:08.524815+00:00'
updated_at: '2023-04-10T20:36:14.401667+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - credential-access
verified: true
validated: true
---

# set-krb5ccname-to-tmp-ticket-ccache

## Command

```bash
export KRB5CCNAME=/tmp/ticket.ccache
```

## Description

This command configures the KRB5CCNAME variable to point to a custom-named ticket cache file (/tmp/ticket.ccache), often used after copying an existing cache. It allows seamless reuse of Kerberos tickets in the current shell session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `export` | Exports variable to environment | Built-in |
| `KRB5CCNAME` | Kerberos cache location variable | Yes |
| `=/tmp/ticket.ccache` | Path to custom cache file | Yes |

## Examples

### Basic Usage

```bash
export KRB5CCNAME=/tmp/ticket.ccache
```

### Advanced Usage

After copy:
```bash
cp /tmp/krb5cc_1000 /tmp/ticket.ccache && export KRB5CCNAME=/tmp/ticket.ccache
```

## Expected Output

Silent success; use `klist` to confirm tickets are loaded.

## Related

- [[procedures/reuse-kerberos-ccache-tickets-from-tmp]]
