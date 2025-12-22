---
type: command
executor: bash
data: kinit -kt $_KEYTAB_PATH $_PRINCIPAL@$_REALM
output: null
tags:
  - kerberos
  - ccache
  - tgt
platforms:
  - Linux
  - macOS
  - Windows
verified: true
validated: true
---

# kinit-generate-tgt-from-keytab

## Command

```bash
kinit -kt $_KEYTAB_PATH $_PRINCIPAL@$_REALM
```

## Description

This command uses kinit to authenticate with a keytab file and obtain a Ticket Granting Ticket (TGT), storing it in the default CCACHE file for subsequent Kerberos operations like service access or ticket reuse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -kt | Use keytab for authentication (keytab file) | Yes |
| $_KEYTAB_PATH | Path to the keytab file | Yes |
| $_PRINCIPAL@$_REALM | Service principal and realm (e.g., host/server@EXAMPLE.COM) | Yes |

## Examples

### Basic Usage

```bash
kinit -kt /etc/krb5.keytab host/server.example.com@EXAMPLE.COM
```

### Specify CCACHE Location

```bash
KRB5CCNAME=/tmp/custom.ccache kinit -kt /etc/krb5.keytab host/server.example.com@EXAMPLE.COM
```

## Expected Output

kinit: /etc/krb5.keytab initial ticket granted

> No errors indicate success; use `klist` to verify the TGT in CCACHE.

## Related

- [[procedures/Extract-and-Reuse-Kerberos-Tickets-from-Keytab]]
