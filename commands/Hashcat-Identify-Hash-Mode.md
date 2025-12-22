---
type: command
executor: bash
data: hashcat --example-hashes | grep -i krb5asrep
output: |-
  18200 | Kerberos 5, etype 23, AS-REP
  Example: $krb5asrep$23$User@REALM:8ca9148088e75c5c7b4d6e0d1f2a3b4c...
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hashcat
  - identification
verified: true
validated: true
---

# Hashcat-Identify-Hash-Mode

## Command

```bash
hashcat --example-hashes | grep -i krb5asrep
```

## Description

Queries Hashcat's built-in examples to find matching hash modes by keyword search.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --example-hashes | Display example hashes/modes | Yes |
| grep -i krb5asrep | Search for Kerberos AS-REP | Yes |

## Examples

### Basic Usage

```bash
hashcat --example-hashes | grep ntlm
```

NTLM mode search.

### Advanced Usage

```bash
hashcat --help | grep mode
```

List all modes.

## Expected Output

Mode numbers and examples for matching types.

## Related

- [[procedures/Identify-Password-Hash-Type-with-Hashcat]]
- [[tools/Hashcat]]
