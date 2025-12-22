---
id: 19d59dda-7054-44b5-81b4-de2d8072e3e1
name: hashcat-find-hash-mode-from-example-hashes
type: command
executor: bash
data: hashcat --example-hashes | grep -C 2 $_VALUE
output: >-
  root@kali:~# hashcat --example-hashes | grep -C 2 '\$6\$'


  MODE: 1800

  TYPE: sha512crypt $6$, SHA512 (Unix)

  HASH:
  $6$72820166$U4DVzpcYxgw7MVVDGGvB2/H5lRistD5.Ah4upwENR5UtffLR4X4SxSzfREv8z6wVl0jRFX40/KnYVvK4829kD1
created_at: '2019-09-24T22:00:40.484250+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - hashcracking
  - credential-access
verified: true
validated: true
---

# hashcat-find-hash-mode-from-example-hashes

## Command

```bash
hashcat --example-hashes | grep -C 2 $_VALUE
```

## Description

This command searches Hashcat's built-in database of example hashes to identify the correct mode number for a given hash type, such as those from Linux /etc/shadow. Use it when manually identifying algorithms like MD5 ($1$) or SHA-512 ($6$).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VALUE | Hash identifier pattern to search for (e.g., '\$6\$' for SHA-512) | Yes |
| --example-hashes | Displays Hashcat's example hashes (built-in flag) | Yes |
| grep -C 2 | Shows 2 lines of context around matches for better readability | Yes |

## Examples

### Basic Usage

```bash
hashcat --example-hashes | grep -C 2 '\$6\$'
```

### Advanced Usage

```bash
hashcat --example-hashes | grep -C 2 '\$1\$' | head -5
```

> Limits output to first 5 matches for MD5 hashes.

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# hashcat --example-hashes | grep -C 2 '\$6\$'

MODE: 1800
TYPE: sha512crypt $6$, SHA512 (Unix)
HASH: $6$72820166$U4DVzpcYxgw7MVVDGGvB2/H5lRistD5.Ah4upwENR5UtffLR4X4SxSzfREv8z6wVl0jRFX40/KnYVvK4829kD1
```

This shows the mode (1800), type, and example hash.

## Related

- [[procedures/Brute-Force-Shadow-Hashes]]
- [[commands/hashcat-brute-force-password-hashes]]
