---
id: 35418129-6db0-4200-babf-9da2688d3366
name: ciscot7-decrypt-password
type: command
executor: bash
data: python3 ciscot7.py -d -p $_ENCRYPTED_PASSWORD
output: 'Decrypted password: secrets!'
created_at: '2019-12-18T20:24:02.189332+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - decryption
  - credentials
  - cisco
  - type-7
verified: true
validated: true
---

# ciscot7-decrypt-password

## Command

```bash
python3 ciscot7.py -d -p $_ENCRYPTED_PASSWORD
```

## Description

This command decrypts a Cisco IOS Type 7 obfuscated password using a Python script that implements the known XOR-based reversal algorithm. It takes a hexadecimal string from Cisco configurations and outputs the plaintext password, aiding in credential recovery during network penetration testing or auditing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENCRYPTED_PASSWORD | The Type 7 encrypted password as a hex string (e.g., 01000307490e121c60) | Yes |
| -d | Decrypt mode flag | Yes |
| -p | Flag to specify the password input | Yes |

## Examples

### Basic Usage

Decrypt a sample Type 7 password:

```bash
python3 ciscot7.py -d -p 01000307490e121c60
```

### Advanced Usage

Run in a script or with piped input (if script supports):

```bash
# Assuming script reads from stdin, though primary is flag-based
echo "01000307490e121c60" | python3 ciscot7.py -d
```

## Expected Output

When successful, the command prints the decrypted plaintext password to stdout:

```
Decrypted password: secrets!
```

No output indicates an invalid hex string; check input format.

## Related

- [[procedures/decrypt-cisco-type-7-password]] (if procedure exists)
- [[tools/Cisco-Type-7-Password-Decrypter]]
