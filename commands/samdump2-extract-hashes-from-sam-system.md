---
id: 8fa3ca35-c8fb-491a-8876-7705e80cf1f5
name: samdump2-extract-hashes-from-sam-system
type: command
executor: bash
data: samdump2 $_SYSTEM_FILE $_SAM_FILE > $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:55:58.670490+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-access
  - windows
verified: true
validated: true
---

# samdump2-extract-hashes-from-sam-system

## Command

```bash
samdump2 $_SYSTEM_FILE $_SAM_FILE > $_OUTPUT_FILE
```

## Description

This command uses samdump2 to extract NTLM password hashes from Windows SAM and SYSTEM registry hive files obtained via LFI or other means. It decrypts the hashes using the boot key from the SYSTEM file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SYSTEM_FILE | Path to the SYSTEM hive file (e.g., system) | Yes |
| $_SAM_FILE | Path to the SAM hive file (e.g., sam) | Yes |
| $_OUTPUT_FILE | Output file for hashes (e.g., hashes.txt) | Yes |

## Examples

### Basic Usage

```bash
samdump2 system sam > hashes.txt
```

### Advanced Usage

```bash
samdump2 ./hives/system ./hives/sam > extracted_hashes.txt
```

## Expected Output

A text file with lines in the format:

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

Each line shows username, RID, LM hash, NT hash, and other fields. Empty LM/NT hashes indicate blank passwords.

## Related

- [[procedures/Windows-LFI-to-RCE-via-Credentials-Files]]
- [[commands/hashcat-crack-ntlm-hashes]]
