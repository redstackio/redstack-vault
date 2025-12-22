---
id: 548a754c-21e7-4e16-bcdb-a3734aded035
name: john-crack-asrep
type: command
executor: bash
data: john --format=krb5asrep --wordlist=$_WORDLIST $_HASH_FILE
output: null
created_at: '2023-04-06T03:56:04.983858+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
platforms:
  - Linux
  - Windows
tags:
  - cracking
  - john
verified: true
validated: true
---

# john-crack-asrep

## Command

```bash
john --format=krb5asrep --wordlist=$_WORDLIST $_HASH_FILE
```

## Description

Cracks AS-REP hashes using John the Ripper in dictionary mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --format=krb5asrep | Kerberos AS-REP format | Yes |
| --wordlist=$_WORDLIST | Dictionary file | Yes |
| $_HASH_FILE | Input hashes | Yes |

## Examples

### Basic Usage

```bash
john --format=krb5asrep --wordlist=passwords_kerb.txt hashes.asreproast
```

## Expected Output

Guesses and progress; use 'john --show' for results.

## Related

- [[procedures/Kerberos-AS-REP-Roasting-Attack]]
- [[tools/John-the-Ripper]]
