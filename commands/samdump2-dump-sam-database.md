---
id: 6f9e02b5-04f5-4d06-b54c-098c5fecc5ed
name: samdump2-dump-sam-database
type: command
executor: bash
data: samdump2 /path/to/SAM/file > samdump.txt
output: null
created_at: '2023-04-06T03:56:28.805574+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - dumping
  - sam
verified: true
validated: true
---

# samdump2-dump-sam-database

## Command

```bash
samdump2 /path/to/SAM/file > samdump.txt
```

## Description

This command dumps hashes from a single SAM file using samdump2, useful for quick extraction without the SYSTEM file (though full NTLM requires BootKey).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/path/to/SAM/file` | Full path to the copied SAM hive | Yes |
| `> samdump.txt` | Redirect output to a text file | Yes |

## Examples

### Basic Usage

```bash
samdump2 SAM > samdump.txt
```

### Advanced Usage

```bash
samdump2 /tmp/SAM -o output.txt
```

## Expected Output

Administrator : : : : :31d6cfe0d16ae931b73c59d7e0c089c0
Guest : : : : :31d6cfe0d16ae931b73c59d7e0c089c0

## Related

- [[procedures/Windows-SAM-and-SYSTEM-Hash-Extraction]]
- [[tools/samdump2]]
