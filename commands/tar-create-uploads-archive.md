---
id: ab60d15f-3193-41a2-bcf3-22b9e410048e
type: command
executor: bash
data: tar cvzf uploads.tar.gz ./d3209c811fee407218bff7cb3b4333e6
output: null
created_at: '2025-12-11T03:48:05.894Z'
updated_at: '2025-12-11T03:48:05.894Z'
platforms:
  - Linux
tags:
  - archive
verified: false
validated: true
submitted: true
---

# tar-create-uploads-archive

## Command

```bash
tar cvzf uploads.tar.gz ./d3209c811fee407218bff7cb3b4333e6
```

## Description

Archive the directory with symlinks into uploads.tar.gz, generating the malicious tar for proxy serving during group import.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `c` | Create archive | Yes |
| `v` | Verbose | No |
| `z` | Gzip | Yes |
| `f` | File name | Yes |
| `uploads.tar.gz` | Output file | Yes |
| `./d3209c811fee407218bff7cb3b4333e6` | Input directory | Yes |

## Examples

### Basic Usage

```bash
tar cvzf uploads.tar.gz ./d3209c811fee407218bff7cb3b4333e6
```

## Expected Output

Verbose output listing archived files, creates the gzipped tar file.

## Related

- [[procedures/Create-Malicious-Tar-File-with-Symlinks]]
- [[commands/mkdir-create-upload-dir]]
