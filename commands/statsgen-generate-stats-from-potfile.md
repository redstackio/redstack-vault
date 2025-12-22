---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: statsgen-generate-stats-from-potfile
type: command
executor: bash
data: python2 statsgen.py ../hashcat.potfile -o hashcat.mask
output: null
created_at: '2023-04-06T03:56:04.096865+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - mask-generation
  - statistics
verified: true
validated: true
---

# statsgen-generate-stats-from-potfile

## Command

```bash
python2 statsgen.py $_POTFILE_PATH -o $_MASK_FILE
```

## Description

Runs statsgen.py from the iphelix/pack to analyze a Hashcat .potfile and generate a base mask file capturing password patterns like length distributions and character frequencies. Use after previous cracking sessions to inform custom attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POTFILE_PATH | Path to the Hashcat potfile (e.g., ../hashcat.potfile) | Yes |
| -o $_MASK_FILE | Output file for the generated mask (e.g., hashcat.mask) | Yes |

## Examples

### Basic Usage

```bash
python2 statsgen.py ../hashcat.potfile -o hashcat.mask
```

### With Full Path

```bash
python2 statsgen.py /path/to/hashcat.potfile -o /path/to/hashcat.mask
```

## Expected Output

Processing potfile...
Generated mask file: hashcat.mask
(Statistical output on patterns, e.g., common lengths: 8-12 chars)

## Related

- [[procedures/Crack-NTLM-Hashes-with-Hashcat]]
- [[commands/maskgen-generate-custom-mask]]
