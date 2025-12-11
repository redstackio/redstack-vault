---
id: ff777505-7f66-414e-b317-bd6600478d94
type: command
executor: bash
data: mkdir ./d3209c811fee407218bff7cb3b4333e6
output: null
created_at: '2025-12-11T03:48:05.900Z'
updated_at: '2025-12-11T03:48:05.900Z'
platforms:
  - Linux
tags:
  - directory-creation
verified: false
validated: true
submitted: true
---

# mkdir-create-upload-dir

## Command

```bash
mkdir ./d3209c811fee407218bff7cb3b4333e6
```

## Description

Create a directory with the upload secret hash as name, used in preparing the structure for a malicious tar file to exploit the symlink vulnerability in GitLab imports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./d3209c811fee407218bff7cb3b4333e6` | Directory path using the noted upload secret hash | Yes |

## Examples

### Basic Usage

```bash
mkdir ./d3209c811fee407218bff7cb3b4333e6
```

## Expected Output

Creates the directory without output if successful.

## Related

- [[procedures/Create-Malicious-Tar-File-with-Symlinks]]
- [[commands/ln-symlink-passwd]]
