---
type: command
executor: bash
data: hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -O -w 3
output: |-
  hashcat (v6.2.6) starting...

  Session..........: hashcat
  Status...........: Running
  Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
  Hash.Target......: asrep_hashes.txt
  Time.Started.....: 2023-10-01 12:10:00 (5:23:45)
  ...
  Recovered........: 1/1 (100.00%) Digests
  $krb5asrep$23$testuser2@EXAMPLE.COM:password123
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - cracking
  - dictionary
verified: true
validated: true
---

# Hashcat-Dictionary-Attack-on-Hashes

## Command

```bash
hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -O -w 3
```

## Description

Performs a dictionary attack on Kerberos AS-REP hashes using optimized kernels and high workload profile.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 18200 | Hash mode for AS-REP etype 23 | Yes |
| asrep_hashes.txt | Input hash file | Yes |
| /usr/share/wordlists/rockyou.txt | Dictionary file | Yes |
| -O | Use optimized kernels | No |
| -w 3 | High workload for speed | No |

## Examples

### Basic Usage

```bash
hashcat -m 18200 hashes.txt rockyou.txt
```

### Advanced Usage

```bash
hashcat -m 18200 hashes.txt rockyou.txt -r rules/best64.rule --increment
```

With rules and incrementing.

## Expected Output

Cracking progress and recovered passwords.

## Related

- [[procedures/Brute-Force-AS-REP-Hashes-with-Hashcat]]
- [[tools/Hashcat]]
