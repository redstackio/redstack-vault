---
id: d0a77568-8751-435e-a7e7-102256247007
name: hashcat-crack-mode-18200
type: command
executor: bash
data: >-
  hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -r
  /usr/share/hashcat/rules/best64.rule
output: |-
  Session..........: hashcat
  Status...........: Cracked
  Recovered........: 1/1 (100.00%) Digests
  ...
created_at: '2020-01-20T20:42:02.727182+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - hashcat
  - cracking
verified: true
validated: true
---

# hashcat-crack-mode-18200

## Command

```bash
hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

## Description

Cracks Kerberos AS-REP hashes with dictionary and rules.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 18200 | AS-REP mode | Yes |
| asrep_hashes.txt | Hash file | Yes |
| rockyou.txt | Wordlist | Yes |
| -r best64.rule | Rules file | No |

## Examples

### Basic Usage

```bash
hashcat -m 18200 hashes.txt rockyou.txt
```

## Expected Output

Cracking progress and recovered passwords.
