---
type: command
executor: bash
data: touch 'index.php'\ntouch $'index\\u200D.php'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - evasion
  - file-creation
verified: true
validated: true
---

# touch-create-visually-identical-files

## Command

```bash
touch 'index.php'

touch $'index\u200D.php'
```

## Description

This command sequence creates two empty files in the current directory: a standard decoy file and an imposter file with a visually identical name using a Unicode zero-width joiner (\u200D). It is used in evasion scenarios to masquerade malicious files as legitimate ones, exploiting visual inspection flaws in Linux environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'index.php'` | Name of the decoy file (standard filename without special characters) | Yes |
| `$` | Bash ANSI-C quoting for embedding Unicode escape | Built-in |
| `\u200D` | Unicode zero-width joiner escape sequence to insert invisible character | Yes |
| `.php` | File extension (can be customized for target context, e.g., .txt, .sh) | Yes |

## Examples

### Basic Usage

```bash
touch 'index.php'

touch $'index\u200D.php'
```

Creates files that appear identical via `ls` but are distinct technically.

### Advanced Usage

```bash
touch $'important-config.conf'

touch $'important\u200D-config.conf'

# Then add content to imposter
echo 'malicious payload' > $'important\u200D-config.conf'
```

Customizes filenames for specific masquerading scenarios, such as mimicking config files.

## Expected Output

No direct output from `touch` on success (files are created silently). Verify with:

```bash
ls -la
# -rw-r--r-- 1 user user 0 Oct 1 12:00 index.php
# -rw-r--r-- 1 user user 0 Oct 1 12:00 index.php (imposter appears same)

ls -b
# index.php
# index\342\200\215.php (escaped Unicode visible)
```

If files exist already, `touch` updates timestamps without error. Failure outputs 'touch: cannot touch ...: Permission denied'.

## Related

- [[procedures/Linux-Visually-Identical-File-Names-Evasion]] (procedure using this command)
- [[codes/bash-touch-visually-identical-files]] (code snippet with comments)
