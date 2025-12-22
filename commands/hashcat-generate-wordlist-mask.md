---
id: 3c89f835-61ef-426a-8cd3-854091fc0f61
name: hashcat-generate-wordlist-mask
type: command
executor: bash
data: hashcat -a 3 --stdout $_MASK > $_OUTPUT_FILE
output: null
created_at: '2019-10-18T01:13:22.970030+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - password cracking
  - brute force
verified: true
validated: true
---

# hashcat-generate-wordlist-mask

## Command

```bash
hashcat -a 3 --stdout $_MASK > $_OUTPUT_FILE
```

## Description

This command uses Hashcat to generate a wordlist based on a specified mask pattern in brute-force mode, outputting all combinations to a file via stdout redirection. It is ideal for creating custom dictionaries when the password structure is partially known, avoiding the need for pre-built wordlists.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a 3 | Sets attack mode to brute-force (dictionary attack with masks) | Yes |
| --stdout | Outputs generated candidates to stdout instead of cracking hashes | Yes |
| $_MASK | The mask pattern defining password structure (e.g., ?d?s?b?a for digit-special-byte-alphanumeric) | Yes |
| > $_OUTPUT_FILE | Redirects output to a file (e.g., wordlist.txt); use absolute path for large files | Yes |

## Examples

### Basic Usage

Generate a simple 4-character wordlist with digits and lowercase:

```bash
hashcat -a 3 --stdout ?d?d?l?l > pin_wordlist.txt
```

### Advanced Usage

For the example mask covering mixed characters:

```bash
hashcat -a 3 --stdout ?d?s?b?a > custom_mask_wordlist.txt
```

Add --increment to generate incrementally if the full keyspace is too large:

```bash
hashcat -a 3 --stdout --increment ?d?d?d?d > incremental_pins.txt
```

## Expected Output

The command produces a plain text file with one candidate per line. For mask ?d?s?b?a, success looks like:

```
0!00?
0!00a
0!00b
0!00c
...
9~＀Z
9~！[
9~＂\
9~＃]
```

Progress is shown in the terminal (e.g., "Candidates: 10/10000000"), and the file size indicates completion (e.g., ~7.7M lines for the example mask).

## Related

- [[procedures/Generate-Wordlist-Using-Mask-Hashcat]]
- [[codes/Hashcat-Mask-Character-Definitions]]
