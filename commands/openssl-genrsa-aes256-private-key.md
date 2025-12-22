---
type: command
executor: bash
data: openssl genrsa -aes256 -out $_PRIVATE_KEY 4096
output: null
platforms:
  - Linux
tags:
  - cryptography
  - setup
verified: true
validated: true
---

# openssl-genrsa-aes256-private-key

## Command

```bash
openssl genrsa -aes256 -out $_PRIVATE_KEY 4096
```

## Description

This command generates a 4096-bit RSA private key encrypted with AES-256-CBC using a user-provided passphrase. It is used to create secure private keys for SSH authentication in penetration testing environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -aes256 | Encrypts the private key using AES-256-CBC cipher | Yes |
| -out $_PRIVATE_KEY | Output file path for the private key (e.g., id_rsa) | Yes |
| 4096 | Key modulus size in bits (higher is more secure) | Yes |

## Examples

### Basic Usage

```bash
openssl genrsa -aes256 -out id_rsa 4096
```

### Advanced Usage

```bash
openssl genrsa -aes256 -out /path/to/id_rsa 4096
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
Generating RSA private key, 4096 bit long modulus (2 primes)
..................................................................................................................++++
..................................................................................................................++++
e is 65537 (0x010001)
Enter pass phrase for id_rsa:
Verifying - Enter pass phrase for id_rsa:
```

The command generates progress dots during prime generation and prompts for the passphrase. No errors indicate success, and the file is created with encryption.

## Related

- [[procedures/Generate-RSA-Keypair-with-AES256-Encryption]]
- [[tools/openssl]]
