---
id: new-uuid-5
name: hashcat-identify-hash
type: command
executor: bash
data: hashcat --identify asrep_hashes.txt
output: |
  Hashfile 'asrep_hashes.txt':
  Kerberos 5 AS-REP Pre-Auth etype 23: 1 hash
created_at: '2023-01-01T00:00:00+00:00'
updated_at: '2023-06-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - hashcat
  - identification
verified: true
validated: true
---

# hashcat-identify-hash

## Command

```bash
hashcat --identify asrep_hashes.txt
```

## Description

Identifies hash types in a file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --identify | Identify mode | Yes |
| asrep_hashes.txt | Input file | Yes |

## Examples

### Basic Usage

```bash
hashcat --identify hashes.txt
```

## Expected Output

Hash type and mode info.
