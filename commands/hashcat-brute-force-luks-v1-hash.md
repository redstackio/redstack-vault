---
type: command
executor: bash
data: hashcat -m 14600 $_HASH $_WORDLIST
output: |-
  root@kali:~# hashcat -m 14600 hash rockyou.txt  

  hashcat (v5.0.0) starting...

  Hashes: 1 digests; 1 unique digests, 1 unique salts
  Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
  Rules: 1

  Minimum password length supported by kernel: 0
  Maximum password length supported by kernel: 256

  Dictionary cache hit:
  * Filename..: rockyou.txt
  * Passwords.: 14344385
  * Bytes.....: 139921507
  * Keyspace..: 14344385
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - hashcat
  - luks
verified: true
validated: true
---

# hashcat-brute-force-luks-v1-hash

## Command

```bash
hashcat -m 14600 $_HASH $_WORDLIST
```

## Description

This command launches a dictionary attack on a LUKS v1 header hash using Hashcat's mode 14600 (LUKS). It tests passphrases from the wordlist against the encrypted key slots, potentially recovering the plaintext passphrase for unlocking the volume.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 14600 | Hash mode for LUKS v1 | Built-in |
| $_HASH | Path to the extracted LUKS header file | Yes |
| $_WORDLIST | Path to the dictionary wordlist file | Yes |

## Examples

### Basic Usage

```bash
hashcat -m 14600 luks_header.bin rockyou.txt
```

### Advanced Usage

```bash
hashcat -m 14600 luks_header.bin rockyou.txt --rules best64 -O
```

## Expected Output

```
root@kali:~# hashcat -m 14600 hash rockyou.txt  

hashcat (v5.0.0) starting...

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Dictionary cache hit:
* Filename..: rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385
```

On success, it will display the cracked passphrase; otherwise, it shows progress and statistics.

## Related

- [[procedures/Brute-Force-and-Mount-LUKS1-Encrypted-Filesystem]]
