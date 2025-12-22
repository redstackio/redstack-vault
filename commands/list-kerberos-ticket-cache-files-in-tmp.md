---
id: 058c469a-664d-4472-bbff-c03f8a54c027
name: list-kerberos-ticket-cache-files-in-tmp
type: command
executor: bash
data: ls /tmp/ | grep krb5cc
output: |-
  krb5cc_1000
  krb5cc_1569901113
  krb5cc_1569901115
created_at: '2023-04-06T03:56:08.525014+00:00'
updated_at: '2023-04-10T20:36:14.401667+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - discovery
verified: true
validated: true
---

# list-kerberos-ticket-cache-files-in-tmp

## Command

```bash
ls /tmp/ | grep krb5cc
```

## Description

This command lists all files in /tmp that match the Kerberos cache pattern (krb5cc*), revealing potential ticket files for reuse. Use it during post-exploitation to find cached credentials from AD authentications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ls /tmp/` | Lists files in /tmp directory | Built-in |
| `|` | Pipes output to grep | Built-in |
| `grep krb5cc` | Filters for krb5cc files | Built-in |

## Examples

### Basic Usage

```bash
ls /tmp/ | grep krb5cc
```

### Advanced Usage

With timestamps:
```bash
ls -la /tmp/ | grep krb5cc
```

## Expected Output

```
krb5cc_1000
krb5cc_1569901113
krb5cc_1569901115
```

## Related

- [[procedures/reuse-kerberos-ccache-tickets-from-tmp]]
