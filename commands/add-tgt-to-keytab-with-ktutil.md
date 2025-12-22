---
type: command
executor: bash
data: >-
  ktutil -k $_KEYTAB_FILE add -p "$_USERNAME@$_DOMAIN" -e arcfour-hmac-md5 -w
  "$_NT_HASH" --hex -V 5
tags:
  - kerberos
  - keytab
platforms:
  - Linux
verified: true
validated: true
---

# add-tgt-to-keytab-with-ktutil

## Command

```bash
ktutil -k $_KEYTAB_FILE add -p "$_USERNAME@$_DOMAIN" -e arcfour-hmac-md5 -w "$_NT_HASH" --hex -V 5
```

## Description

This command uses ktutil to create or add to a Kerberos keytab file, storing the principal and NT hash for future ticket generation without interactive prompts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEYTAB_FILE | Output keytab file path | Yes |
| $_USERNAME@$_DOMAIN | Kerberos principal (user@domain) | Yes |
| $_NT_HASH | NTLM hash in hex (without LM) | Yes |
| -e arcfour-hmac-md5 | Encryption type for NT hash | Built-in |
| --hex | Input password as hex | Built-in |
| -V 5 | Key version number | Built-in |

## Examples

### Basic Usage

```bash
ktutil -k ~/mykeys.keytab add -p "tgwynn@LAB.ROPNOP.COM" -e arcfour-hmac-md5 -w "1a59bd44fe5bec39c44c8cd3524dee" --hex -V 5
```

### Advanced Usage

```bash
ktutil -k $KEYTAB add -p "$PRINCIPAL" -e $ETYPE -w "$HASH" --hex -V $KVNO
```

## Expected Output

ktutil: add
Will use the raw keytab key representation
Principal: tgwynn@LAB.ROPNOP.COM
Encryption type: arcfour-hmac-md5
Key version: 5

This confirms the entry was added.

## Related

- [[procedures/OverPass-the-Hash-with-Impacket]]
- [[commands/obtain-tgt-with-kinit]]
