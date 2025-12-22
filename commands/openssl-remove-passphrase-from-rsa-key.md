---
id: d363c224-ae15-4e97-b80e-d9798e118c9d
name: openssl-remove-passphrase-from-rsa-key
type: command
executor: bash
data: openssl rsa -in $_PRIVATE_KEY.enc -out $_PRIVATE_KEY
output: |-
  root@hackers:~# openssl rsa -in id_rsa -out id_rsa_unencrypted
  Enter pass phrase for id_rsa:
  writing RSA key
created_at: '2019-09-16T20:11:43.105485+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - openssl
  - keys
  - credentials
verified: true
validated: true
---

# openssl-remove-passphrase-from-rsa-key

## Command

```bash
openssl rsa -in $_PRIVATE_KEY.enc -out $_PRIVATE_KEY
```

## Description

This command uses OpenSSL to remove the passphrase protection from an encrypted RSA private key by decrypting it with the provided passphrase and writing an unprotected version to a new file. It is typically used when preparing stolen or obtained keys for automated use in security testing or attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PRIVATE_KEY.enc | Path to the input encrypted RSA private key file (PEM format) | Yes |
| $_PRIVATE_KEY | Path to the output file for the unprotected private key | Yes |
| -in | Specifies the input file | Built-in |
| -out | Specifies the output file | Built-in |

## Examples

### Basic Usage

Decrypt a key named 'id_rsa.enc' to 'id_rsa':

```bash
openssl rsa -in id_rsa.enc -out id_rsa
```

### Advanced Usage

Run with verbose output by redirecting stdin if automating passphrase entry (note: passphrase must still be provided interactively or via secure input):

```bash
openssl rsa -in id_rsa.enc -out id_rsa -passin pass:$_PASSPHRASE
```

## Expected Output

The command prompts for the passphrase and confirms writing the key upon success:

```
root@hackers:~# openssl rsa -in id_rsa -out id_rsa_unencrypted
Enter pass phrase for id_rsa:
writing RSA key
```

If the passphrase is incorrect, it will error with 'unable to load Private Key'.

## Related

- [[procedures/Remove-Passphrase-from-RSA-Private-Key]]
