---
type: command
executor: bash
data: cryptsetup luksOpen $_FILE.img $_CRYPT
output: |-
  root@kali:~# cryptsetup luksOpen backup.img crypt-backup
  Enter passphrase for backup.img:
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cryptography
  - luks
  - decryption
verified: true
validated: true
---

# cryptsetup-luksOpen-encrypted-volume

## Command

```bash
cryptsetup luksOpen $_FILE.img $_CRYPT
```

## Description

This command opens a LUKS-encrypted device or image using the provided passphrase, decrypting it and creating a mapped device in /dev/mapper/ under the specified name. It is the key step to access the plaintext contents after passphrase recovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE.img | Path to the LUKS-encrypted image or device | Yes |
| $_CRYPT | Name for the unlocked mapper device (e.g., crypt-backup) | Yes |

## Examples

### Basic Usage

```bash
cryptsetup luksOpen backup.img crypt-data
```

### Advanced Usage

```bash
cryptsetup luksOpen --key-file keyfile.txt /dev/sda1 unlocked-vol
```

## Expected Output

```
root@kali:~# cryptsetup luksOpen backup.img crypt-backup
Enter passphrase for backup.img:
```

After entering the correct passphrase, it returns to the prompt without errors; the device is now available at /dev/mapper/crypt-backup.

## Related

- [[procedures/Brute-Force-and-Mount-LUKS1-Encrypted-Filesystem]]
