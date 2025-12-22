---
id: 6ddbb863-04bb-44ca-951c-78e01b4370ef
name: hashcat-mutate-wordlist-append-digit
type: command
executor: bash
data: hashcat -a 6 --stdout $_WORDLIST ?d > $_WORDLIST.mutated
output: ''
created_at: '2020-03-18T23:35:23.625297+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - mutation
  - wordlist
verified: true
validated: true
---

# hashcat-mutate-wordlist-append-digit

## Command

```bash
hashcat -a 6 --stdout $_WORDLIST ?d > $_WORDLIST.mutated
```

## Description

Mutates a wordlist by appending a single digit (0-9) to each entry.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a 6 | Append mask attack | Yes |
| --stdout | Output to stdout | Yes |
| $_WORDLIST | Input wordlist | Yes |
| ?d | Digit placeholder | Yes |

## Examples

### Basic Usage

```bash
hashcat -a 6 --stdout words.txt ?d > mutated.txt
```

## Expected Output

Description: Redirected file with mutated entries (no console output).

## Related

- [[procedures/Build-Custom-Password-List-for-Dictionary-Attack]]
- [[tools/Hashcat]]
