---
id: cmd-001
data: 'dir d:\\TrustHX\\STBKSERM101\\www_app /d/s/f'
tags:
  - discovery
  - file-system
type: command
output: >-
  Directory listing including paths like d:\\TrustHX\\STBKSERM101\\www_app\\bin,
  d:\\TrustHX\\STBKSERM101\\www_app\\common, etc., wrapped in HTML textarea
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:22.941Z'
verified: false
validated: true
submitted: true
---
# dir-directory-listing

## Command

```cmd
dir d:\\TrustHX\\STBKSERM101\\www_app /d/s/f
```

## Description

This Windows command lists files and directories recursively in the specified path, used via webshell to disclose server file system structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| d:\\TrustHX\\STBKSERM101\\www_app | Target directory path | Yes |
| /d | Includes directory names in output | No |
| /s | Recurses into subdirectories | No |
| /f | Displays full pathnames | No |

## Examples

### Basic Usage

```cmd
dir d:\\TrustHX\\STBKSERM101\\www_app /d/s/f
```

### Advanced Usage

Omit flags for simpler listing: dir d:\\path

## Expected Output

Directory listing with subdirs like bin, common, wrapped in HTML from webshell.

## Related

- [[commands/type-source-code-disclosure]]
