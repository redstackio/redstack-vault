---
id: cmd-create-policy-file
data: |-
  cat > policy.json << EOF
  {
    "experimental-policy": {
      "default": "disallow",
      "allow-fs-read": ["*"]
    }
  }
  EOF
tags:
  - nodejs
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-09-12T00:00:00Z'
updated_at: '2025-12-14T17:29:28.397Z'
verified: false
validated: true
submitted: true
---
# create-policy-file

## Command

```bash
cat > policy.json << EOF
{
  "experimental-policy": {
    "default": "disallow",
    "allow-fs-read": ["*"]
  }
}
EOF
```

## Description

This command creates a JSON policy file for Node.js's experimental permission model, setting default to disallow but permitting fs-read operations, which is necessary to demonstrate the fs.lstat bypass vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cat` | Standard output redirection tool | Yes |
| `> policy.json` | Specifies the output file | Yes |
| `<< EOF` | Here-document delimiter for multi-line input | Yes |

## Examples

### Basic Usage

```bash
cat > policy.json << EOF
{
  "experimental-policy": {
    "default": "disallow",
    "allow-fs-read": ["*"]
  }
}
EOF
```

### Advanced Usage

To restrict to specific paths, modify the allow-fs-read array:

```bash
cat > policy.json << EOF
{
  "experimental-policy": {
    "default": "disallow",
    "allow-fs-read": ["/tmp/*"]
  }
}
EOF
```

## Expected Output

No console output; creates policy.json file with the specified content. Verify with `cat policy.json` to see the JSON structure.

## Related

- [[Related Procedure]]
