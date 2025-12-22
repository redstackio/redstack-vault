---
type: command
executor: bash
data: kinit -t $_KEYTAB_FILE "$_USERNAME@$_DOMAIN"
tags:
  - kerberos
  - ticket
platforms:
  - Linux
verified: true
validated: true
---

# obtain-tgt-with-kinit

## Command

```bash
kinit -t $_KEYTAB_FILE "$_USERNAME@$_DOMAIN"
```

## Description

This command uses kinit to obtain a Kerberos TGT from the KDC using a keytab file, automating authentication for scripts or tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEYTAB_FILE | Path to the keytab file | Yes |
| $_USERNAME@$_DOMAIN | Kerberos principal | Yes |
| -t | Use keytab for authentication | Built-in |

## Examples

### Basic Usage

```bash
kinit -t ~/mykeys.keytab "tgwynn@LAB.ROPNOP.COM"
```

### Advanced Usage

```bash
kinit -t $KEYTAB "$PRINCIPAL" -k -f
```

## Expected Output

kinit: /tmp/krb5cc_1000 initial ticket is correctly configured

No errors indicate success, with TGT in default cache.

## Related

- [[procedures/OverPass-the-Hash-with-Impacket]]
- [[commands/add-tgt-to-keytab-with-ktutil]]
