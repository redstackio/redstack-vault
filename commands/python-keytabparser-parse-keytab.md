---
type: command
executor: bash
data: python KeytabParser.py $_KEYTAB_PATH
output: null
tags:
  - kerberos
  - keytab
  - parse
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# python-keytabparser-parse-keytab

## Command

```bash
python KeytabParser.py $_KEYTAB_PATH
```

## Description

This command executes the KeytabParser script to parse a Kerberos keytab file, displaying details like principals, key versions, encryption types, and potential crackable keys for credential reuse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEYTAB_PATH | Path to the keytab file (e.g., /etc/krb5.keytab) | Yes |

## Examples

### Basic Usage

```bash
python KeytabParser.py /etc/krb5.keytab
```

### With Output Redirection

```bash
python KeytabParser.py /etc/krb5.keytab > keytab_parse.txt
```

## Expected Output

Keytab version: 0x502
Principal: host/server.example.com@EXAMPLE.COM
KVNO: 2
Encryption: aes256-cts-hmac-sha1-96
Key: 0x...

> Output lists all entries in the keytab with details for analysis.

## Related

- [[procedures/Extract-and-Reuse-Kerberos-Tickets-from-Keytab]]
