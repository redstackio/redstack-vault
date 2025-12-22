---
data: unzip echo_vakzz.jpg.zip
tags:
  - file-extraction
type: command
executor: bash
platforms:
  - Linux
id: 40dd97b0-91dc-4c9f-a73a-eb47753f7efc
created_at: '2025-12-11T03:47:58.270Z'
updated_at: '2025-12-11T03:47:58.270Z'
verified: false
validated: true
submitted: true
---
# unzip-poc-file

## Command

```bash
unzip echo_vakzz.jpg.zip
```

## Description

Extracts the contents of the ZIP file containing the PoC DjVu image for GitLab RCE exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo_vakzz.jpg.zip` | The ZIP file to extract | Yes |

## Examples

### Basic Usage

```bash
unzip echo_vakzz.jpg.zip
```

## Expected Output

Extracts echo_vakzz.jpg to the current directory.

## Related

- [[procedures/Prepare-Malicious-DjVu-PoC-File]]
