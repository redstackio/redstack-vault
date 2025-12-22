---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - evasion
  - file-creation
  - masquerading
validated: true
---

# bash-touch-visually-identical-files

## Code

```bash
# A decoy file with no special characters
touch 'index.php'

# An imposter file with visually identical name
touch $'index\u200D.php'
```

## Description

This bash code snippet creates two empty files that appear visually identical in a Linux terminal or file manager: a decoy 'index.php' and an imposter with a hidden Unicode zero-width joiner (\u200D) inserted. It supports evasion techniques by allowing attackers to hide malicious files among legitimate ones, relying on the invisibility of the Unicode character to fool human reviewers. The code is simple, requiring no external tools, and can be extended to add content to the imposter file for payload delivery.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `index.php` | Base filename for the decoy (customizable to match target legitimate files) | `config.ini` |
| `\u200D` | Unicode escape for zero-width joiner (invisible separator) | N/A (fixed) |
| `.php` | File extension to mimic (adjust for context like .sh for scripts) | `.conf` |

## Usage

Execute this snippet in a bash shell within the target directory to create the files. Follow up by editing the imposter (e.g., `vi $'index\u200D.php'`) to insert malicious code, such as a reverse shell. Ideal for post-exploitation persistence in web servers or user directories. Used in red team exercises to test detection gaps in visual auditing processes. Reference in procedures like [[procedures/Linux-Visually-Identical-File-Names-Evasion]].

## Detection

- File system auditing tools (e.g., Auditd) logging `touch` executions or file creations in monitored directories.
- Unicode-aware scanners or `ls -b` / `file` command revealing non-ASCII characters in filenames.
- Integrity checks using hashes (e.g., Tripwire) that ignore names and detect unexpected files.
- EDR solutions monitoring for anomalous file naming patterns or shell commands with `$''` quoting.

## Related

- [[procedures/Linux-Visually-Identical-File-Names-Evasion]] (procedure utilizing this code)
- [[commands/touch-create-visually-identical-files]] (core command without comments)
