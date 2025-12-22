---
type: command
executor: bash
data: tar -I '$_PROGRAM_COMMAND' -cf $_OUTPUT_ARCHIVE $_FILES
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - injection
  - input
  - tar
verified: true
validated: true
---

# tar-input-program-injection

## Command

```bash
tar -I '$_PROGRAM_COMMAND' -cf $_OUTPUT_ARCHIVE $_FILES
```

## Description

Uses a custom input filter program, injectable to run commands before TAR processes the input stream.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I | Specify input filter program | Yes |
| $_PROGRAM_COMMAND | Command to run as filter (e.g., cat or sh -c 'id') | Yes |
| -c | Create mode | Yes |
| -f | Output archive | Yes |
| $_OUTPUT_ARCHIVE | Archive path | Yes |
| $_FILES | Input files | Yes |

## Examples

### Basic Usage

```bash
tar -I 'cat' -cf out.tar files/
```

### Advanced Usage

```bash
tar -I 'sh -c "echo injected | cat"' -cf out.tar files/
```

## Expected Output

Archive created with filtered input; injected command output may appear in logs.

## Related

- [[procedures/TAR-Argument-Injection]]
