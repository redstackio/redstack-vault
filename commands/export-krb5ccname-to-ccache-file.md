---
id: 5a4a21ec-34c4-4cea-b5c2-827e9951615b
name: export-krb5ccname-to-ccache-file
type: command
executor: bash
data: export KRB5CCNAME="$(pwd)/Administrator.ccache"
output: 'root@kali:~# export KRB5CCNAME="$(pwd)/Administrator.ccache"'
created_at: '2020-06-24T05:08:26.192345+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - environment
verified: true
validated: true
---

# export-krb5ccname-to-ccache-file

## Command

```bash
export KRB5CCNAME="$(pwd)/Administrator.ccache"
```

## Description

This command sets the KRB5CCNAME environment variable to specify a custom Kerberos credential cache file for use with Impacket tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $(pwd)/Administrator.ccache | Path to the ccache file (current dir + filename) | Yes |

## Examples

### Basic Usage

```bash
export KRB5CCNAME="$(pwd)/Administrator.ccache"
```

### Advanced Usage

Set for a different path:
```bash
export KRB5CCNAME="/tmp/ticket.ccache"
```

## Expected Output

No verbose output; verify with `echo $KRB5CCNAME` showing the path.

```
root@kali:~# export KRB5CCNAME="$(pwd)/Administrator.ccache"
```

## Related

- [[procedures/Create-Golden-Ticket-and-Launch-Windows-SYSTEM-Shell-from-Linux]]
