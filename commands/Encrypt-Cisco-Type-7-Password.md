---
id: 34533ddb-6ab6-4db2-aec1-95a8abb48363
name: Encrypt-Cisco-Type-7-Password
type: command
executor: bash
data: python ciscot7.py -e -p '$_PASSWORD'
output: |-
  root@kali:~/Documents/ciscot7# python ciscot7.py -e -p 'secrets!'
  Encrypted password: 03175e08140a355f0f
created_at: '2020-03-12T21:23:02.213528+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cisco
  - encryption
verified: true
validated: true
---

# Encrypt-Cisco-Type-7-Password

## Command

```bash
python ciscot7.py -e -p '$_PASSWORD'
```

## Description

This command invokes the ciscot7.py Python script to encrypt a plaintext password using the Cisco Type 7 algorithm. It generates a hexadecimal string suitable for use in Cisco IOS configuration files. Use this during red team engagements to prepare obfuscated passwords for network device manipulation or testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -e | Encrypt mode (as opposed to -d for decrypt) | Yes |
| -p | Plaintext password to encrypt (quoted if special chars) | Yes |
| $_PASSWORD | The actual password value to substitute | Yes |
| ciscot7.py | Path to the script (assumed in current directory) | Yes |

## Examples

### Basic Usage

```bash
python ciscot7.py -e -p 'admin123'
```

### Advanced Usage

For passwords with spaces or specials:

```bash
python ciscot7.py -e -p 'p@ssw0rd!'
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~/Documents/ciscot7# python ciscot7.py -e -p 'secrets!'
Encrypted password: 03175e08140a355f0f
```

The output shows the encrypted hex string, which can be copied for config use. No errors if password is valid.

## Related

- [[commands/Encrypt-Cisco-Type-7-Password]] (this command)
- [[commands/Encrypt-Cisco-Type-7-Password]]
- [[tools/ciscot7]]
