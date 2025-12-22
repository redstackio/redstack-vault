---
id: 761336b9-4c3c-482a-b7e4-4a7d4469c099
name: samdump2-extract-hashes-from-system-and-sam
type: command
executor: bash
data: samdump2 SYSTEM SAM -o sam.txt
output: null
created_at: '2023-04-06T03:56:28.805760+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - dumping
  - sam
verified: true
validated: true
---

# samdump2-extract-hashes-from-system-and-sam

## Command

```bash
samdump2 SYSTEM SAM -o sam.txt
```

## Description

This command extracts decrypted NTLM hashes from both SYSTEM and SAM files using samdump2, leveraging the BootKey for full hash recovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SYSTEM` | Path to the copied SYSTEM hive file | Yes |
| `SAM` | Path to the copied SAM hive file | Yes |
| `-o sam.txt` | Output file for hashes | Yes |

## Examples

### Basic Usage

```bash
samdump2 SYSTEM SAM -o sam.txt
```

### Advanced Usage

```bash
samdump2 SYSTEM SAM -o /tmp/hashes.txt
```

## Expected Output

Administrator:500:31D6CFE0D16AE931B73C59D7E0C089C0:AAC3B435B51404EEAAC3B435B51404EE:::

## Related

- [[procedures/Windows-SAM-and-SYSTEM-Hash-Extraction]]
- [[tools/samdump2]]
