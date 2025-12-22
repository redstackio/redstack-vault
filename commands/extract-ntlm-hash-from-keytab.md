---
id: cffe8236-b1e3-4e07-833f-12c88e325655
name: extract-ntlm-hash-from-keytab
type: command
executor: bash
data: python3 keytabextract.py $_KEYTAB_FILE
output: null
created_at: '2023-04-06T03:56:08.671205+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - ntlm
  - hash-extraction
verified: true
validated: true
---

# extract-ntlm-hash-from-keytab

## Command

```bash
python3 keytabextract.py $_KEYTAB_FILE
```

## Description

Extracts NTLM hashes from RC4-HMAC keys in a Kerberos keytab file. Fails if no RC4 keys are present.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEYTAB_FILE | Path to the keytab file (e.g., krb5.keytab) | Yes |

## Examples

### Basic Usage

```bash
python3 keytabextract.py krb5.keytab
```

## Expected Output

```
[+] Keytab File successfully imported.
        REALM : DOMAIN
        SERVICE PRINCIPAL : host/computer.domain
        NTLM HASH : 31d6cfe0d16ae931b73c59d7e0c089c0
```

Or error if no RC4: `[!] No RC4-HMAC located. Unable to extract NTLM hashes.`

## Related

- [[procedures/Extract-Service-Principal-Keys-from-Keytab]]
