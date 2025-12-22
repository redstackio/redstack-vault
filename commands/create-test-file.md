---
id: cmd-uuid-placeholder-003
data: echo "Test upload content" > test.txt
tags:
  - prep
  - file
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.108Z'
verified: false
validated: true
submitted: true
---
# create-test-file

## Command

```bash
echo "Test upload content" > test.txt
```

## Description

This command creates a simple test file for uploading to the vulnerable endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo "Test upload content"` | Content to write | Yes |
| `> test.txt` | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
echo "Hello" > test.txt
```

### Advanced Usage

```bash
cat << EOF > test.txt
Line 1
Line 2
EOF
```

## Expected Output

A new file test.txt with the specified content.

## Related

- [[Related Procedure: Exploit-File-Upload-Memory-Leak]]
