---
id: f7b1ef50-6175-4456-9805-c6104b6b9138
name: openssl-generate-sha512-password-hash
type: command
executor: bash
data: openssl passwd -6 -salt $_SALT $_PASSWORD
output: $6$_SALT$hashed_password_output
created_at: '2019-09-16T18:26:12.711397+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Unix
tags:
  - cryptography
  - hashing
  - password
verified: true
validated: true
---

# openssl-generate-sha512-password-hash

## Command

```bash
openssl passwd -6 -salt $_SALT $_PASSWORD
```

## Description

This command generates a SHA512 hashed password in a format compatible with Unix-like systems (e.g., /etc/shadow). It uses the `-6` option to specify the SHA512 algorithm and applies a custom salt for added security against rainbow table attacks. Useful in security testing for creating or verifying password hashes, simulating credential storage, or preparing payloads that require hashed credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SALT | A user-defined salt string (8-16 characters recommended, alphanumeric) to prepend to the hash for uniqueness | Yes |
| $_PASSWORD | The plaintext password to hash | Yes |
| -6 | Specifies SHA512 hashing algorithm (OpenSSL-specific flag) | Built-in |
| -salt | Flag to provide the salt value | Built-in |

## Examples

### Basic Usage

Generate a SHA512 hash for the password "Thisisyourpassword" with salt "16bytesXX16bytes":

```bash
openssl passwd -6 -salt 16bytesXX16bytes Thisisyourpassword
```

### Advanced Usage

Generate a hash with a shorter salt (minimum 8 characters):

```bash
openssl passwd -6 -salt mysalt123 mysecurepass
```

## Expected Output

The command outputs a single line with the hashed password in the format `$6$salt$hash`, where `$6$` indicates SHA512. Example:

```
$6$16bytesXX16bytes$FXuYP0OI7qYB3K6u6.91Blr7rtvjLZmpcuAWuWVnTj4G2nVGny6k5yzaDbV3iQCwoSDMGgXePvFxddnxYkpa5/
```

This can be directly used in password files or compared against stored hashes.

## Related

- [[tools/openssl]] (Parent tool documentation)
- [[procedures/Generate-and-Verify-Password-Hashes]] (Example procedure using this command)
