---
id: 2bd706ab-9af5-49d6-b806-40945e6a6620
name: OpenSSL Generate a SHA512-crypt hash
type: command
executor: bash
data: openssl passwd -6 -salt $_SALT $_PASSWORD
output: >-
  $6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/
created_at: '2019-09-30T20:17:07.170333+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - hashing
  - password
verified: true
validated: true
---

# openssl-generate-sha512-crypt-hash

## Command

```bash
openssl passwd -6 -salt $_SALT $_PASSWORD
```

## Description

This command uses OpenSSL to generate a SHA512-crypt (crypt6) password hash with a specified salt and plaintext password. It is used in Linux environments to create hashes compatible with /etc/passwd or /etc/shadow for setting user passwords programmatically.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -6 | Use SHA512-crypt algorithm | Yes |
| -salt $_SALT | Custom salt string (8 characters recommended, alphanumeric) to prevent rainbow table attacks | Yes |
| $_PASSWORD | Plaintext password to hash | Yes |

## Examples

### Basic Usage

```bash
openssl passwd -6 -salt abcdefgh mypassword
```

### Advanced Usage

For scripting, pipe password from stdin or use random salt generation beforehand (e.g., `openssl rand -base64 8` for salt).

```bash
SALT=$(openssl rand -base64 8 | tr -d '/+=' | cut -c1-8)
openssl passwd -6 -salt $SALT mypassword
```

## Expected Output

A single line with the hashed password in the format `$6$SALT$HASH`, e.g.:

```
$6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/
```

This output is ready to insert into /etc/passwd after the first colon of the user entry.

## Related

- [[procedures/Change-Password-in-Writable-Etc-Passwd]]
