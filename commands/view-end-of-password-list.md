---
id: cmd-view-password-end
data: tail 10k_most_common.txt
tags:
  - wordlist
  - inspection
type: command
output: |-
  shoes
  howie
  hevnm4
  hugohugo
  eighty
  epson
   evangeli
  eeeee1
  eyphed
  Geniaal2!!
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.771Z'
verified: false
validated: true
submitted: true
---
# view-end-of-password-list

## Command

```bash
tail 10k_most_common.txt
```

## Description

Displays the last 10 lines of a password file to inspect and confirm appended entries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 10k_most_common.txt | Path to the password file | Yes |

## Examples

### Basic Usage

```bash
tail 10k_most_common.txt
```

### Advanced Usage

Show last 5 lines:

```bash
tail -5 10k_most_common.txt
```

## Expected Output

shoes
howie
hevnm4
hugohugo
eighty
epson
 evangeli
eeeee1
eyphed
Geniaal2!!

## Related

- [[commands/count-passwords-in-dictionary]]
- [[procedures/Prepare-Password-Dictionary]]
