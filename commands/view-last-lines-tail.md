---
id: e8b2d4a4-e710-4971-a710-490787d3d807
name: view-last-lines-tail
type: command
executor: bash
data: tail -n $_LINES $_FILE
output: null
created_at: '2023-04-06T03:56:17.742498+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - file-viewing
  - evasion
verified: true
validated: true
---

# View Last Lines with Tail

## Command

```bash
tail -n $_LINES $_FILE
```

## Description

Displays the last portion of a file, useful for inspecting the end of a payload script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n $_LINES | Number of lines to show (default 10) | No |
| $_FILE | Path to the file | Yes |

## Examples

### Basic Usage

```bash
tail -n 5 /tmp/script.sh
```

### Follow Mode

```bash
tail -f /tmp/log.txt
```

## Expected Output

Last lines of the file, e.g.:
```
Payload execution
End of script
```

## Related

- [[procedures/hide-artifacts-using-hidden-files-and-obfuscated-scripts-on-linux]]
