---
data: echo 'test' > testfile.txt
tags:
  - prep
  - file
type: command
output: File testfile.txt created with content 'test'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.434Z'
id: d3ea1eda-4a08-4057-a83c-9d2377c29395
verified: false
validated: true
submitted: true
---
# echo-create-testfile

## Command

```bash
echo 'test' > testfile.txt
```

## Description

Creates a simple text file for use in Telerik upload tests during version identification. Benign content avoids detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `>` | Redirect output to file | Yes |
| `'test'` | Content to write | Yes |
| `testfile.txt` | Output filename | Yes |

## Examples

### Basic Usage

```bash
echo 'test' > testfile.txt
```

### Advanced Usage

```bash
echo 'payload' > custom.txt
```

## Expected Output

File created successfully; verify with `cat testfile.txt` showing 'test'.

## Related

- [[procedures/Identify-Vulnerable-Telerik-Version]]
