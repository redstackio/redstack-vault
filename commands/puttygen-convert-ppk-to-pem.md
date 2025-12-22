---
id: 666616da-b594-46b2-964d-717c731df471
type: command
executor: bash
data: puttygen $_KEY.ppk -O private-openssh -o $_KEY.pem
output: null
created_at: '2020-02-28T19:44:43.267568+00:00'
updated_at: '2023-05-30T19:46:57.361580+00:00'
platforms:
  - Linux
tags:
  - convert
  - ssh
  - keys
verified: true
validated: true
---

# puttygen-convert-ppk-to-pem

## Command

```bash
puttygen $_KEY.ppk -O private-openssh -o $_KEY.pem
```

## Description

This command uses puttygen to convert a PuTTY private key file (.ppk) to OpenSSH private key format (.pem). It is useful for preparing keys for use with Linux SSH clients during remote access operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEY.ppk | Input file path to the PuTTY private key (base name with .ppk extension) | Yes |
| -O private-openssh | Output format specifier for OpenSSH private key | Yes |
| -o $_KEY.pem | Output file path for the converted PEM key (base name with .pem extension) | Yes |

## Examples

### Basic Usage

```bash
puttygen mykey.ppk -O private-openssh -o mykey.pem
```

### Advanced Usage

If the input key has a passphrase, the command will prompt for it interactively.

## Expected Output

On success, no output is produced, but the .pem file is created. Example terminal interaction:

```
root@kali:~# puttygen private.ppk -O private-openssh -o private.pem
Enter passphrase for key "private.ppk": 
(Enter passphrase if set)
root@kali:~# ls -la private.pem
-rw------- 1 root root 1675 Oct  1 12:00 private.pem
```

## Related

- [[tools/puttygen]]
