---
id: 15b7f116-7551-412b-8448-6619dc9d8240
name: hashcat-crack-asrep-hash
type: command
executor: bash
data: hashcat -m 18200 -a 0 $_HASH_FILE.txt $_WORDLIST.txt --force
output: null
created_at: '2023-01-12T00:17:16.435315+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - hashcat
  - cracking
verified: true
validated: true
---

# hashcat-crack-asrep-hash

## Command

```bash
hashcat -m 18200 -a 0 $_HASH_FILE.txt $_WORDLIST.txt --force
```

## Description

This command cracks Kerberos AS-REP hashes using Hashcat in dictionary mode (-a 0), targeting mode 18200 for krb5asrep format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 18200 | Hash mode for AS-REP (krb5asrep) | Yes |
| -a 0 | Attack mode: straight dictionary | Yes |
| $_HASH_FILE.txt | Input file with hashes | Yes |
| $_WORDLIST.txt | Dictionary wordlist | Yes |
| --force | Ignore warnings (e.g., OpenCL) | No |

## Examples

### Basic Usage

```bash
hashcat -m 18200 -a 0 hashes.txt rockyou.txt
```

### Advanced Usage

With rules: `hashcat -m 18200 -a 0 hashes.txt rockyou.txt -r rules/best64.rule`

## Expected Output

`Session..........: hashcat
Status...........: Cracked
username:password123
`

Use `hashcat --show hashes.txt` for results.

## Related

- [[procedures/Crack-AS-REP-Hash-Using-Hashcat-or-John]]
- [[tools/Hashcat]]
