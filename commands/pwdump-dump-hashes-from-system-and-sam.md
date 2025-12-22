---
id: 5ff86f3f-924c-4f39-adfb-510434e7cb94
name: pwdump-dump-hashes-from-system-and-sam
type: command
executor: bash
data: pwdump SYSTEM SAM > /root/sam.txt
output: null
created_at: '2023-04-06T03:56:28.805695+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - dumping
  - sam
verified: true
validated: true
---

# pwdump-dump-hashes-from-system-and-sam

## Command

```bash
pwdump SYSTEM SAM > /root/sam.txt
```

## Description

This command uses pwdump in offline mode to extract password hashes from copied SYSTEM and SAM registry hive files, outputting in a format suitable for cracking tools like John.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SYSTEM` | Path to the copied SYSTEM hive file | Yes |
| `SAM` | Path to the copied SAM hive file | Yes |
| `> /root/sam.txt` | Redirect output to a hash file | Yes |

## Examples

### Basic Usage

```bash
pwdump SYSTEM SAM > /root/sam.txt
```

### Advanced Usage

```bash
pwdump -u Administrator SYSTEM SAM > admin_hashes.txt
```

## Expected Output

Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

## Related

- [[procedures/Windows-SAM-and-SYSTEM-Hash-Extraction]]
- [[tools/pwdump]]
