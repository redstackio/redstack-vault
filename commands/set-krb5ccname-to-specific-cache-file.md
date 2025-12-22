---
id: 46774b61-2760-4c02-96ad-3a7790a3818e
name: set-krb5ccname-to-specific-cache-file
type: command
executor: bash
data: export KRB5CCNAME=/tmp/krb5cc_1569901115
output: null
created_at: '2023-04-06T03:56:08.525130+00:00'
updated_at: '2023-04-10T20:36:14.401667+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - credential-access
verified: true
validated: true
---

# set-krb5ccname-to-specific-cache-file

## Command

```bash
export KRB5CCNAME=/tmp/krb5cc_1569901115
```

## Description

This command sets the KRB5CCNAME environment variable to a specific Kerberos ticket cache file in /tmp, enabling reuse of existing tickets for AD authentication. Replace the path with the target cache file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `export` | Sets environment variable for the session | Built-in |
| `KRB5CCNAME` | Variable name for ticket cache path | Yes |
| `=/tmp/krb5cc_1569901115` | Path to the cache file (placeholder) | Yes |

## Examples

### Basic Usage

```bash
export KRB5CCNAME=/tmp/krb5cc_1000
```

### Advanced Usage

With verification:
```bash
export KRB5CCNAME=/tmp/krb5cc_1569901115 && echo $KRB5CCNAME
```

## Expected Output

No output on success; verify with `echo $KRB5CCNAME` showing the path.

## Related

- [[procedures/reuse-kerberos-ccache-tickets-from-tmp]]
