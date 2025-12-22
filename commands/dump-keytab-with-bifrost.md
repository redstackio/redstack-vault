---
id: 457e4498-632a-488e-a920-f6f3c2ddde66
name: dump-keytab-with-bifrost
type: command
executor: bash
data: ./bifrost -action dump -source keytab -path $_KEYTAB_PATH
output: null
created_at: '2023-04-06T03:56:08.671490+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - dump
  - keytab
verified: true
validated: true
---

# dump-keytab-with-bifrost

## Command

```bash
./bifrost -action dump -source keytab -path $_KEYTAB_PATH
```

## Description

Dumps the contents of a keytab file using Bifrost for analysis or transfer.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEYTAB_PATH | Path to the keytab file (e.g., test/krb5.keytab) | Yes |
| -action dump | Action to perform dumping | Built-in |
| -source keytab | Source type as keytab | Built-in |
| -path | Path to keytab | Built-in |

## Examples

### Basic Usage

```bash
./bifrost -action dump -source keytab -path test/krb5.keytab
```

## Expected Output

Dumped keytab entries in readable format, including principals and keys.

## Related

- [[procedures/Extract-Service-Principal-Keys-from-Keytab]]
