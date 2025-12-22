---
type: command
executor: bash
data: openssl rsa -in $_PRIVATE_KEY -pubout -out $_PUBLIC_KEY
output: null
platforms:
  - Linux
tags:
  - cryptography
  - setup
verified: true
validated: true
---

# openssl-rsa-extract-public-key

## Command

```bash
openssl rsa -in $_PRIVATE_KEY -pubout -out $_PUBLIC_KEY
```

## Description

This command extracts the public key from an AES-256 encrypted RSA private key file, prompting for the passphrase. The public key is output in PEM format for use in SSH authorized_keys files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -in $_PRIVATE_KEY | Input file path of the encrypted private key (e.g., id_rsa) | Yes |
| -pubout | Outputs the public key instead of decrypting | Yes |
| -out $_PUBLIC_KEY | Output file path for the public key (e.g., id_rsa.pub) | Yes |

## Examples

### Basic Usage

```bash
openssl rsa -in id_rsa -pubout -out id_rsa.pub
```

### Advanced Usage

```bash
openssl rsa -in /path/to/id_rsa -pubout -out /path/to/id_rsa.pub
```

## Expected Output

```
Enter pass phrase for id_rsa:
writing RSA key
```

The command prompts for the passphrase and confirms writing the public key. The output file should contain the public key without errors.

## Related

- [[procedures/Generate-RSA-Keypair-with-AES256-Encryption]]
- [[tools/openssl]]
