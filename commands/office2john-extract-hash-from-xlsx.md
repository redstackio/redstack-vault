---
id: 56531108-238d-46f1-9cd1-64b961db8dc7
name: office2john-extract-hash-from-xlsx
type: command
executor: bash
data: office2john.py $_TARGET_FILE.xlsx
output: >-
  root@kali:/usr/share/john# ./office2john.py /tmp/ccinfo.xlsx 

  ccinfo.xlsx:$office$*2013*100000*256*16*7a8978075d68abb1546e84564ba4e6f7*80c87564a5f646a2e6f8d2e74653e225*08dd6485a452b6c8456c5468321aa10cb548a5aee64264cc68456b68d6826a5d
created_at: '2020-06-25T21:07:47.240186+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - hash-extraction
verified: true
validated: true
---

# office2john-extract-hash-from-xlsx

## Command

```bash
office2john.py $_TARGET_FILE.xlsx
```

## Description

This command uses the office2john.py script from John the Ripper to extract the password hash from a password-protected XLSX file. It is used as the first step in cracking Office document passwords by converting the encrypted file into a hash format that can be fed into cracking tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_FILE.xlsx | Path to the password-protected XLSX file | Yes |

## Examples

### Basic Usage

```bash
office2john.py document.xlsx
```

### Advanced Usage

```bash
python3 /usr/share/john/office2john.py /path/to/protected.xlsx > hash.txt
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:/usr/share/john# ./office2john.py /tmp/ccinfo.xlsx 
ccinfo.xlsx:$office$*2013*100000*256*16*7a8978075d68abb1546e84564ba4e6f7*80c87564a5f646a2e6f8d2e74653e225*08dd6485a452b6c8456c5468321aa10cb548a5aee64264cc68456b68d6826a5d
```

The output is a single line with the filename followed by the hash in John the Ripper format.

## Related

- [[procedures/Brute-Force-Password-Protected-XLSX-File]]
- [[commands/john-brute-force-hash-file]]
